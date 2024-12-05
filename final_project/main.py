import pygame
from src.controller import Controller  # Import your controller

def main():
    pygame.init()
    # Create an instance of your Controller object
    game_controller = Controller()
    # Call your mainloop
    game_controller.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
