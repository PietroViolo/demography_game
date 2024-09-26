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
max_counter = 3

# Flame emoji
flame = pygame.image.load(flags_dir + "flame.png")
new_size = (100, 100)
flame = pygame.transform.scale(flame, new_size)


# Crown emoji
crown = pygame.image.load(flags_dir + "crown.png")
new_size = (110, 130)
crown = pygame.transform.scale(crown, new_size)

# Banner
banner = pygame.image.load(flags_dir + "bg_demo.png")


with open(data_file, encoding = 'utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        countries.append({
            "name": row[0],
            "population": float(row[1]),
            "iso2": row[2]
        })

def get_random_flags():
    flags = []
    while len(flags) < 3:
        country = random.choice(countries)
        if country not in flags:
            flags.append(country)
    return flags

def get_highest_population(flags):
    max_population = 0
    for flag in flags:
        if flag["population"] > max_population:
            max_population = flag["population"]
    return max_population

def get_highest_iso(flags):
    max_population = 0
    for flag in flags:
        if flag["population"] > max_population:
            max_population = flag["population"]
            iso = flag["iso2"]
    return iso
  

def draw_flags(flags):
    x = 100
    for flag in flags:
        flag_image = pygame.image.load(flags_dir + flag["iso2"] + ".png")
        screen.blit(flag_image, (x, 700))
        x += 650
        

def draw_text(text, x, y):
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (x, y))
    
def game_loop():
    flags = get_random_flags()
    highest_population = get_highest_population(flags)
    highest_iso = get_highest_iso(flags)
    counter = 0
    
    screen.fill((82, 138, 235)) # blue
    draw_text("Quel pays est le plus peuplé?", 450, 400) 
    draw_text(flags[0]['name'], 100, 600) # Pays 1
    draw_text(flags[1]['name'], 750, 600) # Pays 2
    draw_text(flags[2]['name'], 1400, 600) # Pays 3
    
    
    
    #draw_text("Streak: " + str(counter), 1100, 1000) # Counter
    #draw_text("Score le plus élevé d'aujourd'hui: " + str(counter), 700, 1200) # Highest counter
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if flags[0]["population"] == highest_population:
                        screen.fill((0, 255, 0)) # green
                        draw_text("Vrai! Sa population est de " + str(flags[0]["population"]), 350, 500)
                        pygame.display.update()
                        pygame.time.wait(5000)                
                        screen.fill((82, 138, 235)) # blue
                        counter += 1
                        game_loop()
                    else:
                        screen.fill((255, 0, 0)) # red
                        draw_text("Faux! La bonne réponse est:", 350, 400)
                        flag_x = pygame.image.load(flags_dir +highest_iso+ ".png")
                        screen.blit(flag_x, (1450, 400))
                        pygame.display.update()
                        pygame.time.wait(5000)                
                        screen.fill((82, 138, 235)) # blue
                        counter = 0
                        game_loop()

                elif event.key == pygame.K_DOWN:
                    if flags[1]["population"] == highest_population:
                        screen.fill((0, 255, 0)) # green
                        draw_text("Vrai! Sa population est de " + str(flags[1]["population"]), 350, 500)
                        pygame.display.update()
                        pygame.time.wait(5000)                
                        screen.fill((82, 138, 235)) # blue
                        counter += 1
                        game_loop()
                    else:
                        screen.fill((255, 0, 0)) # red
                        draw_text("Faux! La bonne réponse est:", 350, 400)
                        flag_x = pygame.image.load(flags_dir +highest_iso+ ".png")
                        screen.blit(flag_x, (1450, 400))
                        pygame.display.update()
                        pygame.time.wait(5000)                
                        screen.fill((82, 138, 235)) # blue
                        counter = 0
                        game_loop()
                elif event.key == pygame.K_RIGHT:
                    if flags[2]["population"] == highest_population:
                        screen.fill((0, 255, 0)) # green
                        draw_text("Vrai! Sa population est de " + str(flags[2]["population"]), 350, 500)
                        pygame.display.update()
                        pygame.time.wait(5000)                
                        screen.fill((82, 138, 235)) # blue
                        counter += 1
                        game_loop()
                    else:
                        screen.fill((255, 0, 0)) # red
                        draw_text("Faux! La bonne réponse est:", 350, 400)
                        flag_x = pygame.image.load(flags_dir +highest_iso+ ".png")
                        screen.blit(flag_x, (1450, 400))
                        pygame.display.update()
                        pygame.time.wait(5000)                
                        screen.fill((82, 138, 235)) # blue
                        counter = 0
                        game_loop()
                        
                        
        
        
        # update display
        pygame.display.update()
        draw_flags(flags)
        pygame.display.update()
        screen.blit(banner, (0, 20))
        #screen.blit(flame, (970, 970))
        #screen.blit(crown, (550, 1150))

game_loop()
pygame.quit()
