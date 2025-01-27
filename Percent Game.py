import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Percentage Game with Menu")
clock = pygame.time.Clock()

# Define colors
pink = (255, 192, 203)
black = (0, 0, 0)
white = (255, 255, 255)

# Set up fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Game states
game_state = "menu"  # Start in the menu
running = True
user_input = ""
score = 0
feedback = ""

# Function to generate random question
def randNumPercentAndAnswer():
    num = math.ceil(random.randint(1, 200) / 5) * 5  # Random number rounded to the nearest 5
    percent = math.ceil(random.randint(10, 90) / 10) * 10  # Random percentage rounded to the nearest 5
    answer = num * (percent / 100)  # Calculate the percentage of the number
    return num, percent, round(answer, 2)

# Draw the menu screen
def draw_menu():
    screen.fill(pink)

    # Render title
    title_text = font.render("Percentage Game", True, black)
    screen.blit(title_text, (180, 100))

    # Render menu options
    start_text = small_font.render("Press SPACE to Start", True, black)
    screen.blit(start_text, (220, 300))

    quit_text = small_font.render("Press Q to Quit", True, black)
    screen.blit(quit_text, (250, 400))

# Draw the game screen
def draw_game(num, percent, user_input, score, feedback):
    screen.fill(pink)

    # Render the question
    question_text = font.render(f"What is {percent}% of {num}?", True, black)
    screen.blit(question_text, (50, 50))

    # Render user input
    input_text = font.render(user_input, True, black)
    screen.blit(input_text, (50, 150))

    # Render feedback
    feedback_text = small_font.render(feedback, True, black)
    screen.blit(feedback_text, (50, 250))

    # Render score
    score_text = small_font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (50, 350))

# Main game variables
num, percent, correct_answer = randNumPercentAndAnswer()

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == "menu":
                # Menu controls
                if event.key == pygame.K_SPACE:  # Start the game
                    game_state = "game"
                elif event.key == pygame.K_q:  # Quit the game
                    running = False
            elif game_state == "game":
                # Game controls
                if event.key == pygame.K_RETURN:  # Check answer
                    if user_input:
                        if user_input.isdigit():  # Ensure the input is a number
                            if float(user_input) == correct_answer:
                                feedback = "Correct!"
                                score += 1
                                num, percent, correct_answer = randNumPercentAndAnswer()
                            else:
                                feedback = "Incorrect! Try again."
                        else:
                            if user_input == "q":
                                running = False
                            feedback = "Invalid input: No letters allowed!"
                        user_input = ""  # Reset input
                elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                    user_input = user_input[:-1]
                else:  # Add typed characters to user input
                    user_input += event.unicode

    # Update screen based on game state
    if game_state == "menu":
        draw_menu()
    elif game_state == "game":
        draw_game(num, percent, user_input, score, feedback)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()