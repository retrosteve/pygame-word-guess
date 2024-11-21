import pygame
import random


def get_display_text(word, guessed_letters):
    display_text = ""
    for letter in word:
        if letter in guessed_letters:
            display_text += letter
        else:
            display_text += "_"
    return display_text


def display_word(word, guessed_letters):
    text = font.render(get_display_text(word, guessed_letters), True, white)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2))


pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Word Guessing Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Font
font = pygame.font.Font(None, 36)

# Word list
words = ["python", "javascript", "java", "c++", "ruby"]

word = random.choice(words)
incorrect_guesses = 0
guessed_letters = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name:
                if key_name.isalpha():
                    letter = key_name
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if key_name not in word:
                            incorrect_guesses += 1

    # Game logic and rendering
    screen.fill(black)
    display_word(word, guessed_letters)

    # Display incorrect guesses
    incorrect_text = font.render(f"Incorrect Guesses: {incorrect_guesses}", True, white)
    screen.blit(incorrect_text, (10, 10))

    # Check win/lose conditions
    if "_" not in get_display_text(word, guessed_letters):
        win_text = font.render("You Win!", True, white)
        screen.blit(win_text, (width // 2 - win_text.get_width() // 2, height // 2))
        running = False
    elif incorrect_guesses >= 6:
        lose_text = font.render("You Lose!", True, white)
        screen.blit(lose_text, (width // 2 - lose_text.get_width() // 2, height // 2))
        running = False

    pygame.display.flip()

pygame.quit()
