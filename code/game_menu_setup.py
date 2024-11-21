import pygame
import sys
import random
from level import Level

# Initialize pygame
pygame.init()

# audi menu

pygame.mixer.init()
menu_music=pygame.mixer.Sound("../audio/Menu.mp3")
menu_music.play(loops=-1)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game Menu')

# Load background images
background_images = [
    pygame.image.load("../graphics/backgrounds/Kotek1.jpg").convert(),
    pygame.image.load("../graphics/backgrounds/Kotek2.jpg").convert(),
    pygame.image.load("../graphics/backgrounds/Kotek4.jpg").convert()
]

# Colors and Fonts
WHITE = (255, 255, 255)
BLUE = (70, 130, 180)
RED = (255, 99, 71)
LIGHT_BLUE = (135, 206, 235)
FONT = pygame.font.Font(None, 48)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

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
    menu_music.stop()
    print("Game Started")
    pygame.display.set_caption('Game')
    main_loop()

def load_stats():
    print("Loading Stats...")
    # Placeholder function for loading stats

def save_game():
    print("Game Saved...")
    # Placeholder logic for saving game data

def load_game():
    print("Game Loaded...")
    # Placeholder logic for loading game data

def graphics_settings():
    print("Opening Graphics Settings...")
    # Placeholder logic for graphical settings

def sound_settings():
    print("Opening Sound Settings...")
    # Placeholder logic for sound settings

def trade_items():
    print("Trading Items...")
    # Placeholder logic for trading items

def options():
    print("Opening Options...")
    running = True
    buttons = [
        Button("GRAPHICS", (SCREEN_WIDTH // 2, 150), graphics_settings, BLUE, (200, 80)),
        Button("SOUND", (SCREEN_WIDTH // 2, 250), sound_settings, RED, (200, 80)),
        Button("SAVE", (SCREEN_WIDTH // 2, 350), save_game, GREEN, (200, 80)),
        Button("LOAD", (SCREEN_WIDTH // 2, 450), load_game, ORANGE, (200, 80)),
        Button("BACK", (SCREEN_WIDTH // 2, 550), lambda: exit_options(), LIGHT_BLUE, (200, 80))
    ]

    def exit_options():
        nonlocal running
        running = False

    background_change_time = 0  # Tracks the time since the last background change
    background_interval = 5000  # Interval in milliseconds (e.g., 5000ms = 5 seconds)
    current_background = random.choice(background_images)  # Initialize with a random background

    while running:
        # Get current time
        current_time = pygame.time.get_ticks()

        # Check if enough time has passed to change the background
        if current_time - background_change_time > background_interval:
            current_background = random.choice(background_images)
            background_change_time = current_time

        # Display the current background
        screen.blit(pygame.transform.scale(current_background, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        
        text_surface = FONT.render("Options Menu", True, WHITE)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.is_clicked(event)

        # Draw buttons
        for button in buttons:
            button.draw(screen)

        pygame.display.flip()

# Main game loop
def main_loop():
    level = Level()
    clock = pygame.time.Clock()
    running = True
    trade_button = Button("TRADE ITEMS", (SCREEN_WIDTH - 150, 50), trade_items, ORANGE, (200, 80))

    while running:
        dt = clock.tick(60) / 1000  # Limit frame rate to 60 FPS and get delta time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            trade_button.is_clicked(event)  # Check for trading button click
        
        # Update level
        level.run(dt)
        
        # Draw the game screen
        screen.fill((0, 0, 0))  # Fill screen with black (or any background for the game)
        level.all_sprites.custom_draw(level.player)
        
        # Draw the trade button
        trade_button.draw(screen)

        pygame.display.flip()

# Creating buttons for main menu
buttons = [
    Button("START", (400, 100), start_game, BLUE, (200, 100)),
    Button("OPTIONS", (300, 300), options, RED, (150, 75)),
    Button("LOAD STATS", (500, 300), load_stats, LIGHT_BLUE, (150, 75))
]

# Main loop with background change delay
def main():
    menu_music.play(loops=-1)
    background_change_time = 0  # Tracks the time since the last background change
    background_interval = 5000  # Interval in milliseconds (e.g., 5000ms = 5 seconds)
    current_background = random.choice(background_images)  # Initialize with a random background

    while True:
        # Get current time
        current_time = pygame.time.get_ticks()

        # Check if enough time has passed to change the background
        if current_time - background_change_time > background_interval:
            current_background = random.choice(background_images)
            background_change_time = current_time

        # Display the current background
        screen.blit(pygame.transform.scale(current_background, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))

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