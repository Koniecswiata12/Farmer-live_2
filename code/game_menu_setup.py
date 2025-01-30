import pygame
import sys
import random
from level import Level

# Initialize pygame
pygame.init()

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
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
RED = (255, 99, 71)
LIGHT_BLUE = (135, 206, 235)
FONT = pygame.font.Font(None, 48)

# Player inventory data
player_inventory = {
    "animals": 0,
    "fields": 0
}

# Generic Button class (unchanged for other buttons)
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

# Styled Button class (specific for "Więcej Zwierząt" and "Więcej Pól")
class StyledButton:
    def __init__(self, text, pos, callback, size):
        self.text = text
        self.pos = pos
        self.callback = callback
        self.size = size
        self.rect = pygame.Rect(pos[0] - size[0] // 2, pos[1] - size[1] // 2, size[0], size[1])

    def draw(self, surface):
        # Outer border (white)
        pygame.draw.rect(surface, WHITE, self.rect, border_radius=10)
        
        # Inner background (black)
        inner_rect = self.rect.inflate(-6, -6)  # Slightly smaller rect for inner background
        pygame.draw.rect(surface, BLACK, inner_rect, border_radius=8)
        
        # Render text
        text_surface = FONT.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()


# Functions for menu and gameplay
def start_game():
    print("Game Started")
    show_selection_menu()


def show_selection_menu():
    """Show the selection menu to choose between adding animals or fields."""
    running = True

    # Create buttons for the selection menu
    buttons = [
        StyledButton("Więcej Zwierząt", (200, 300), add_animals, (200, 50)),
        StyledButton("Więcej Pól", (600, 300), add_fields, (200, 50))
    ]

    while running:
        screen.fill((0, 0, 0))  # Clear the screen with black

        # Display title
        title_text = FONT.render("WYBIERZ", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        screen.blit(title_text, title_rect)

        # Draw buttons
        for button in buttons:
            button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.is_clicked(event)

        pygame.display.flip()


def add_animals():
    """Add random animals to the player's inventory."""
    added_animals = random.randint(1, 5)
    player_inventory["animals"] += added_animals
    print(f"Added {added_animals} animals. Total animals: {player_inventory['animals']}")
    return_to_main_game()


def add_fields():
    """Add random fields to the player's inventory."""
    added_fields = random.randint(1, 3)
    player_inventory["fields"] += added_fields
    print(f"Added {added_fields} fields. Total fields: {player_inventory['fields']}")
    return_to_main_game()


def return_to_main_game():
    """Return to the main game loop after selection."""
    main_loop()


def load_options():
    print("Loading Options...")
    running = True

    # Lista opcji do wyświetlenia
    options = ["GRAPHICS", "SOUND", "SAVE", "LOAD", "BACK"]

    # Pozycje i rozmiary (jeśli potrzebne)
    panel_width = 400
    panel_height = 350
    panel_x = (SCREEN_WIDTH - panel_width) // 2
    panel_y = (SCREEN_HEIGHT - panel_height) // 2

    # Tytuł
    title_text = FONT.render("OPTIONS MENU", True, WHITE)
    title_x = panel_x + (panel_width - title_text.get_width()) // 2
    title_y = panel_y + 30

    # Parametry wyświetlania opcji
    button_height = 50
    start_y = title_y + 80
    spacing = 10

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Czarne tło bez obramowań
        screen.fill(BLACK)

        # Wyświetlanie napisu "OPTIONS MENU"
        screen.blit(title_text, (title_x, title_y))

        # Wyświetlanie opcji jako tekst bez obramowań
        current_y = start_y
        for option_text in options:
            text_surface = FONT.render(option_text, True, WHITE)
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, current_y + button_height // 2))
            screen.blit(text_surface, text_rect)
            current_y += button_height + spacing

        pygame.display.flip()



def show_stats():
    print("Opening Stats Menu...")
    running = True

    stats_data = {
        "PIENIĄDZE": "1200",
        "ILOŚĆ PÓL": f"{player_inventory['fields']}",
        "ZEBRANE WARZYWA": "320",
        "ŚREDNIA ZEBRANYCH PLONÓW DZIENNIE": "30",
        "ILOŚĆ ZWIERZĄT": f"{player_inventory['animals']}",
        "ŚREDNIE DZIENNE ZAROBKI": "500"
    }

    while running:
        screen.fill((0, 0, 0))
        title_text = FONT.render("STATYSTYKI", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

        y_offset = 150
        for key, value in stats_data.items():
            text_surface = FONT.render(f"{key}: {value}", True, WHITE)
            screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, y_offset))
            y_offset += 50

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        pygame.display.flip()


def main_loop():
    """Main gameplay loop."""
    # Placeholder Level class
    level = Level()
    clock = pygame.time.Clock()
    running = True

    while running:
        dt = clock.tick(60) / 1000  # Delta time for frame updates

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape key to return to the menu
                    running = False

        # Update and draw game elements
        screen.fill((0, 0, 0))  # Clear screen
        level.run(dt)
        pygame.display.flip()


def main():
    background_change_time = 0
    background_interval = 5000
    current_background = random.choice(background_images)

    buttons = [
        Button("START", (400, 100), start_game, BLUE, (200, 75)),
        Button("LOAD OPTIONS", (400, 250), load_options, RED, (200, 50)),
        Button("STATYSTYKI", (400, 400), show_stats, LIGHT_BLUE, (200, 50))
    ]

    while True:
        current_time = pygame.time.get_ticks()
        if current_time - background_change_time > background_interval:
            current_background = random.choice(background_images)
            background_change_time = current_time

        screen.blit(pygame.transform.scale(current_background, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.is_clicked(event)

        for button in buttons:
            button.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()