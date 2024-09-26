import pygame
import random
import csv

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Demography Game")

font = pygame.font.Font(None, 100)

flags_dir = "/Users/pietroviolo/Documents/Github/demography_game/flags/"
data_file = '/Users/pietroviolo/Documents/Github/demography_game/Data/countries.csv'

countries = []

# Flame emoji
flame = pygame.image.load(flags_dir + "flame.png")
new_size = (100, 100)
flame = pygame.transform.scale(flame, new_size)


# Crown emoji
crown = pygame.image.load(flags_dir + "crown.png")
new_size = (110, 130)
crown = pygame.transform.scale(crown, new_size)


with open(data_file, encoding = 'utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        countries.append({
            "name": row[0],
            "population": float(row[1]),
            "iso2": row[2]
        })

def draw_flags(flags):
    x = 500
    for flag in flags:
        flag_image = pygame.image.load(flags_dir + flag["iso2"] + ".png")
        screen.blit(flag_image, (x, 500))
        x += 650

def draw_text(text, x, y):
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (x, y))
    
    
    
def start_loop():
    flags = []
    while len(flags) < 3:
        country = random.choice(countries)
        if country not in flags:
            flags.append(country)

    max_population = 0
    for flag in flags:
        if flag["population"] > max_population:
            max_population = flag["population"]
            
    highest_population = max_population

    
    screen.fill((82, 138, 235)) # blue
    draw_text(flags[0]['name'], 500, 400) # Pays 1
    draw_text(flags[1]['name'], 1150, 400) # Pays 2
    draw_text(flags[2]['name'], 1800, 400) # Pays 3
    draw_text("Streak: " + str(counter), 1100, 1000) # Counter
    draw_text("Score le plus élevé d'aujourd'hui: " + str(counter), 700, 1200) # Highest counter
    
    # update display
    pygame.display.update()
    draw_flags(flags)
    screen.blit(flame, (970, 970))
    screen.blit(crown, (550, 1150))
    pygame.display.update()
  
  
  


# Main game loop

counter = 0
start_loop()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                draw_text(str(highest_population), 500, 500)
                pygame.display.update()
                draw_text(str(flags[0]['name']), 200, 500)
                pygame.display.update()
                pygame.time.wait(2000) 
                start_loop()
                
            
            
            
            
pygame.quit()
