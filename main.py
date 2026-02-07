import pygame
import sys

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
DARK_GRAY = (100, 100, 100)

# Fonts
title_font = pygame.font.SysFont("arial", 60)
button_font = pygame.font.SysFont("arial", 40)

# Button class
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()

        # Hover effect
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, DARK_GRAY, self.rect)
        else:
            pygame.draw.rect(surface, GRAY, self.rect)

        # Draw text
        text_surface = button_font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Create buttons
start_button = Button("Start Game", 300, 250, 200, 60)
quit_button = Button("Quit", 300, 350, 200, 60)

# Main menu loop
def main_menu():
    while True:
        screen.fill(BLACK)

        # Draw title
        title = title_font.render("MY GAME", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        # Draw buttons
        start_button.draw(screen)
        quit_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if start_button.is_clicked(event):
                print("Game Started!")  # Replace with game loop

            if quit_button.is_clicked(event):
                pygame.quit()
                sys.exit()

        pygame.display.flip()

# Run menu
main_menu()