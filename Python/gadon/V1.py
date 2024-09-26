import pygame
from pygame.locals import *
import csv
import random



# Initialize Pygame
pygame.init()
pygame.key.init()

# Select three random flags
random_flags = random.sample(flags, 3)

# Read the CSV file
flags = []
with open('/Users/pietroviolo/Documents/Github/demography_game/Data/countries.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        flags.append({'name': row['name'], 'population': float(row['population']), 'iso2': row['iso2']})

# Select three random flags
random_flags = random.sample(flags, 3)

# Load the flag images
flag_images = {}
for flag in flags:
    flag_images[flag['iso2']] = pygame.image.load(f"/Users/pietroviolo/Documents/Github/demography_game/flags/{flag['iso2']}.png")

# Create the screen
screen = pygame.display.set_mode((2000, 500))
pygame.display.set_caption('Demography Game')

# Main game loop
running = True
while running:
    # Check for events
    if not pygame.event.get():
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected = random_flags[0]
            elif event.key == pygame.K_2:
                selected = random_flags[1]
            elif event.key == pygame.K_3:
                selected = random_flags[2]
            else:
                selected = None

            if selected:
                max_population = max(flag['population'] for flag in flags)
                if selected['population'] == max_population:
                    print('Correct!')
                else:
                    print('Incorrect.')
                    print(f'The highest population is {max_population}')
    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the flags on the screen
    for i, flag in enumerate(random_flags):
        screen.blit(flag_images[flag['iso2']], (i * 200, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

