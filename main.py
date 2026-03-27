import pygame, sys, random, time 
from pygame.locals import * 

print("Running")

pygame.init()
score = 0
high_score = 0

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Framework")
clock=pygame.time.Clock()
running = True

player = pygame.Rect(375, 275, 50, 50)
target = pygame.Rect(400, 300, 60, 60)
player_color = (0,128,255)
target_color = (255, 0, 0)

font = pygame.font.Font(None, 36)
text=font.render("Framework", True, (255,255,255)) #Invisible 

sound=pygame.mixer.Sound('sound.ogg')


while running:
    for event in pygame.event.get():


        if event.type == pygame.QUIT: 
            running=False
            
            print("Program Ended")
        
        if event.type == pygame.KEYDOWN: 
            if event.key==pygame.K_SPACE:
                sound.play()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[pygame.K_a]: 
            player.x -= 5
        if keys[K_RIGHT] or keys[pygame.K_d]: 
            player.x += 5
        if keys[K_UP] or keys[pygame.K_w]: 
            player.y -= 5
        if keys[K_DOWN] or keys[pygame.K_s]:
            player.y += 5

        if player.colliderect(target):
            score += 1 
            target.x = random.randint(0, 590)
            target.y = random.randint(0, 430)
        
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, player_color, player)
        pygame.draw.rect(screen, target_color, target)
        
        score_text = font.render("Score: " + str(score), True, (0,0,0))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
        
        
    
pygame.quit()
sys.exit()