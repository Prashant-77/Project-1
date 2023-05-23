import pygame
import time
import random
pygame.init()
width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock, Paper, Scissors")
font = pygame.font.Font(None, 72)
watermark_font = pygame.font.SysFont("Arial", 46, bold=True)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WATERMARK_COLOR = (0, 0, 0, 178)  
player_score = 0
computer_score = 0
result = ""
def draw_text(text, x, y, color=BLACK, font_size=72, center=True):
    font = pygame.font.Font(None, font_size)
    surface = font.render(text, True, color)
    if center:
        rect = surface.get_rect(center=(x, y))
    else:
        rect = surface.get_rect(topleft=(x, y))
    window.blit(surface, rect)
def determine_winner(player_choice, computer_choice):
    global player_score, computer_score
    if player_choice == computer_choice:
        return "Tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        player_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"
button_width = 150
button_height = 80
button_padding = 10
rock_button = pygame.Rect(
    button_padding, height - button_height - button_padding,
    button_width, button_height
)
paper_button = pygame.Rect(
    rock_button.right + button_padding, height - button_height - button_padding,
    button_width, button_height
)
scissors_button = pygame.Rect(
    paper_button.right + button_padding, height - button_height - button_padding,
    button_width, button_height
)
rectangle_width = 50
rectangle_height = 150
rectangle_x = width - rectangle_width - 20
rectangle_y = height - rectangle_height - 20
fill_percentage = 0
window.fill((255, 255, 255))
running = True
start_time = time.time()
winner_declared = False
winner_start_time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                if rock_button.collidepoint(mouse_pos):
                    player_choice = "rock"
                    start_time = time.time()
                    fill_percentage = 0
                    winner_declared = False
                    computer_choice = random.choice(["rock", "paper", "scissors"])
                    result = determine_winner(player_choice, computer_choice)
                    if result == "You win!":
                        player_score += 5
                    elif result == "Computer wins!":
                        computer_score += 1
                elif paper_button.collidepoint(mouse_pos):
                    player_choice = "paper"
                    start_time = time.time()
                    fill_percentage = 0
                    winner_declared = False
                    computer_choice = random.choice(["rock", "paper", "scissors"])
                    result = determine_winner(player_choice, computer_choice)
                    if result == "You win!":
                        player_score += 5
                    elif result == "Computer wins!":
                        computer_score += 1
                elif scissors_button.collidepoint(mouse_pos):
                    player_choice = "scissors"
                    start_time = time.time()
                    fill_percentage = 0
                    winner_declared = False
                    computer_choice = random.choice(["rock", "paper", "scissors"])
                    result = determine_winner(player_choice, computer_choice)
                    if result == "You win!":
                        player_score += 1
                    elif result == "Computer wins!":
                        computer_score += 1
    elapsed_time = time.time() - start_time
    if not winner_declared:
        if elapsed_time < 1:
            fill_percentage = int(elapsed_time * 100 / 1)
        else:
            fill_percentage = 100
    filled_height = (rectangle_height * fill_percentage) // 100

    # Set the color based on the fill percentage
    if fill_percentage <= 20:
        fill_color = (255, 0, 0)  # Red color
    elif fill_percentage <= 40:
        fill_color = (255, 165, 0)  # Orange color
    elif fill_percentage <= 60:
        fill_color = (255, 255, 0)  # Yellow color
    elif fill_percentage <= 80:
        fill_color = (0, 255, 0)  # Green color
    else:
        fill_color = (0, 0, 255)  # Blue color

    # Clear the window
    window.fill(WHITE)

    # Draw buttons
    pygame.draw.rect(window, RED, rock_button)
    pygame.draw.rect(window, GREEN, paper_button)
    pygame.draw.rect(window, BLUE, scissors_button)

    # Draw button labels
    draw_text("Rock", rock_button.centerx, rock_button.centery, WHITE, font_size=24)
    draw_text("Paper", paper_button.centerx, paper_button.centery, WHITE, font_size=24)
    draw_text("Scissors", scissors_button.centerx, scissors_button.centery, WHITE, font_size=24)

    # Draw scores
    draw_text("Player: " + str(player_score), width - 250, 20, BLACK, font_size=72, center=False)
    draw_text("Computer: " + str(computer_score), width - 335, 60, BLACK, font_size=72, center=False)

    # Draw the filled portion of the rectangle on the window
    pygame.draw.rect(window, fill_color, (rectangle_x, rectangle_y + rectangle_height - filled_height, rectangle_width, filled_height))

    # Draw the outline of the rectangle on the window
    pygame.draw.rect(window, fill_color, (rectangle_x, rectangle_y, rectangle_width, rectangle_height), 1)

    # Draw watermark
    watermark_text = watermark_font.render("Made by Prashant Prakash", True, WATERMARK_COLOR)
    window.blit(watermark_text, (15, 15))

    # Draw the winner if a result is available
    if result:
        if not winner_declared:
            draw_text(result, width // 2, height // 2, BLACK)
            if elapsed_time > 1:
                winner_start_time = time.time()
                winner_declared = True
        else:
            elapsed_winner_time = time.time() - winner_start_time
            if elapsed_winner_time > 1:
                result = ""  # Reset the result after 2 seconds

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
