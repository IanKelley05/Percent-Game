import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Percentage Game with Menu")
clock = pygame.time.Clock()

# Define colors
blue = (65, 100, 190)
pink = (255, 192, 203)
black = (0, 0, 0)
white = (255, 255, 255)
backgroundColor = blue

# Set up fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Game states
game_state = "menu"  # Start in the menu
running = True
user_input = ""
score = 0
feedback = ""

# Function to generate random question without math library
def randNumPercentAndAnswer():
    num = ((random.randint(1, 200) + 4) // 5) * 5  # Round to the nearest 5
    percent = ((random.randint(10, 90) + 9) // 10) * 10  # Round to the nearest 10
    answer = num * (percent / 100)  # Calculate the percentage of the number
    return num, percent, round(answer, 2)

# Draw the menu screen
def draw_menu():
    screen.fill(backgroundColor)

    # Render title
    title_text = font.render("Percentage Game", True, black)
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, 100))
    screen.blit(title_text, title_rect)

    # Render "Press SPACE to Start" text
    start_text = small_font.render("Press SPACE to Start", True, black)
    start_rect = start_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(start_text, start_rect)

    # Render "Press Q to Quit" text
    quit_text = small_font.render("Press Q to Quit", True, black)
    quit_rect = quit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
    screen.blit(quit_text, quit_rect)

# Draw the game screen
def draw_game(num, percent, user_input, score, feedback):
    screen.fill(backgroundColor)

    # Render the question
    question_text = font.render(f"What is {percent}% of {num}?", True, black)
    question_rect = question_text.get_rect(center=(screen.get_width() // 2, 100))
    screen.blit(question_text, question_rect)

    # Render user input
    input_text = font.render(user_input, True, black)
    input_rect = input_text.get_rect(center=(screen.get_width() // 2, 200))
    screen.blit(input_text, input_rect)

    # Render feedback
    feedback_text = small_font.render(feedback, True, black)
    feedback_rect = feedback_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 100))
    screen.blit(feedback_text, feedback_rect)

    # Render score
    score_text = small_font.render(f"Score: {score}", True, black)
    score_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 100))
    screen.blit(score_text, score_rect)

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
                                feedback = f"Incorrect! The answer is {correct_answer:.2f}. Try again."
                        else:
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