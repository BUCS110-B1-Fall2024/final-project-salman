import pygame
import random
import urllib.request
import json
from src.snake import Snake
from src.food import Food

class FunFactAPI:
    def __init__(self, api_url="https://uselessfacts.jsph.pl/random.json?language=en"):
        self.api_url = api_url

    def get_fun_fact(self):
        try:
            with urllib.request.urlopen(self.api_url) as response:
                data = json.loads(response.read().decode())
                return data['text']
        except Exception as e:
            return f"Error: {str(e)}"


class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake(400, 300)
        self.food = Food(200, 200)
        self.running = True
        self.score = 0 
        self.font = pygame.font.Font(None, 36) 


        self.food_size = 15
        self.snake_segment_size = 20
        self.wall_padding = 30 


        self.fun_fact_api = FunFactAPI()

    def draw_score(self):
        """
        Draws the current score on the screen.
        """
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))  

    def display_game_over(self):
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, (255, 0, 0))
        self.screen.fill((255, 255, 255)) 
        self.screen.blit(text, (400 - text.get_width() // 2, 300 - text.get_height() // 2)) 
        
        fun_fact = self.fun_fact_api.get_fun_fact()
        fact_font = pygame.font.Font(None, 20)
        fact_text = fact_font.render(f"Fun Fact: {fun_fact}", True, (0, 0, 255))
        self.screen.blit(fact_text, (50, 400))  
        
        pygame.display.flip()
        pygame.time.wait(5000)  

    def is_food_too_close(self):
        food_x, food_y = self.food.position
        for segment in self.snake.body:
            snake_x, snake_y = segment
            if abs(food_x - snake_x) < 50 and abs(food_y - snake_y) < 50:
                return True
        return False

    def mainloop(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                        self.snake.set_direction("UP")
                    elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                        self.snake.set_direction("DOWN")
                    elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                        self.snake.set_direction("LEFT")
                    elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                        self.snake.set_direction("RIGHT")

  
            self.snake.move()


            snake_head_rect = pygame.Rect(
                self.snake.body[0][0],
                self.snake.body[0][1],
                self.snake_segment_size,
                self.snake_segment_size,
            )
            food_rect = pygame.Rect(
                self.food.position[0],
                self.food.position[1],
                self.food_size,
                self.food_size,
            )

            if snake_head_rect.colliderect(food_rect):
                self.snake.grow()
                self.score += 1
      
                while True:
                    new_x = random.randint(self.wall_padding, 780 - self.food_size)
                    new_y = random.randint(self.wall_padding, 580 - self.food_size)
                    self.food.relocate(new_x, new_y)
                    if not self.is_food_too_close(): 
                        break


            head_x, head_y = self.snake.body[0]
            if (
                head_x < self.wall_padding
                or head_x >= 800 - self.wall_padding
                or head_y < self.wall_padding
                or head_y >= 600 - self.wall_padding
                or self.snake.body[0] in self.snake.body[1:]
            ):
                self.running = False
                self.display_game_over()

           
            self.screen.fill((0, 0, 0))  
            pygame.draw.rect(self.screen, (255, 255, 255), (self.wall_padding, self.wall_padding, 800 - 2 * self.wall_padding, 600 - 2 * self.wall_padding), 5)  # Smaller walls
            for segment in self.snake.body:
                pygame.draw.rect(
                    self.screen, (0, 255, 0), (*segment, self.snake_segment_size, self.snake_segment_size)
                )  
            pygame.draw.rect(
                self.screen, (255, 0, 0), (*self.food.position, self.food_size, self.food_size)
            ) 

           
            self.draw_score()

        
            pygame.display.flip()
            self.clock.tick(200 + self.score // 2)  

        pygame.quit()
