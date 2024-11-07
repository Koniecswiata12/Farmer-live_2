import pygame
import sys
from level import Level
from overlay import Overlay

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game Menu')

# Colors and Fonts
WHITE = (255, 255, 255)
BLUE = (70, 130, 180)
RED = (255, 99, 71)
LIGHT_BLUE = (135, 206, 235)
FONT = pygame.font.Font(None, 48)

# Button class
class Button:
    def __init__(self, text, pos, callback, color, size):
        self.text = text
        self.pos = pos
        self.callback = callback
        self.size = size
        self.color = color
        self.rect = pygame.Rect(pos[0] - size[0] // 2, pos[1] - size[1] // 2, size[0], size[1])

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)
        text_surface = FONT.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

# Functions for button actions
def start_game():
    print("Game Started")
    pygame.display.set_caption('Game')
    main_loop()

def load_stats():
    print("Loading Stats...")
    # This is where you would load player stats

def options():
    print("Opening Options...")
    # This is where the options menu would be handled

# Main game loop
def main_loop():
    level = Level()
    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60) / 1000  # Limit frame rate to 60 FPS and get delta time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        
        # Update level
        level.run(dt)
        
        # Draw the game screen
        screen.fill((0, 0, 0))  # Fill screen with black (or any background for the game)
        level.all_sprites.custom_draw(level.player)
        pygame.display.flip()

# Creating buttons as in the image
buttons = [
    Button("START", (400, 100), start_game, BLUE, (200, 100)),
    Button("OPTIONS", (300, 300), options, RED, (150, 75)),
    Button("LOAD STATS", (500, 300), load_stats, LIGHT_BLUE, (150, 75))
]

# Main loop
def main():
    while True:
        screen.fill((173, 216, 230))  # Light blue background as in the image
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.is_clicked(event)
        
        # Draw buttons
        for button in buttons:
            button.draw(screen)

        # Update display
        pygame.display.flip()

if __name__ == "__main__":
    main()