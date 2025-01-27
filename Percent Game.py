import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Percentage Game")
clock = pygame.time.Clock()
running = True

# Define colors
pink = (255, 192, 203)
black = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Game variables
score = 0
user_input = ""
feedback = ""  # Initialize feedback to an empty string

# Function to generate a random question
def randNumPercentAndAnswer():
    num = math.ceil(random.randint(1, 200) / 5) * 5  # Random number rounded to the nearest 5
    percent = math.ceil(random.randint(10, 90) / 10) * 10  # Random percentage rounded to the nearest 5
    answer = num * (percent / 100)  # Calculate the percentage of the number
    return num, percent, answer

# Generate the first question
num, percent, correct_answer = randNumPercentAndAnswer()

# Function to draw everything
def draw():
    # Draw background
    screen.fill(pink)

    # Render the question
    question_text = font.render(f"What is {percent}% of {num}?", True, black)
    screen.blit(question_text, (50, 50))

    # Render the user input
    input_text = font.render(user_input, True, black)
    screen.blit(input_text, (50, 150))

    # Render the feedback
    feedback_text = small_font.render(feedback, True, black)
    screen.blit(feedback_text, (50, 250))

    # Render the score
    score_text = small_font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (50, 350))

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Check answer when Enter is pressed
                try:
                    # Convert user input to float and check if it's correct
                    if float(user_input) == correct_answer:
                        feedback = "Correct!"
                        score += 1
                    else:
                        feedback = f"Incorrect! The answer was {correct_answer:.2f}"
                except ValueError:
                    feedback = "Invalid input. Please enter a number."
                # Reset for the next question
                user_input = ""
                num, percent, correct_answer = randNumPercentAndAnswer()  # Generate new question
            elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                user_input = user_input[:-1]
            else:  # Add typed characters to user input
                user_input += event.unicode

    # Draw everything
    draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
