from my_global_var import *

class Fighter:
    def __init__(self):
        self.img = spaceship_image
        self.img = pygame.transform.scale(self.img, (120, 120))
        self.rect = self.img.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 3 * 2)
        self.is_moving = True

    def draw(self):
        if self.is_moving == True:
            screen.blit(self.img, self.rect)
    
    def update(self):
        if self.is_moving == True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= 10
            if keys[pygame.K_RIGHT]:
                self.rect.x += 10
            if keys[pygame.K_UP]:
                self.rect.y -= 10
            if keys[pygame.K_DOWN]:
                self.rect.y += 10

    def launch(self):
        if self.is_moving == True:
            if keys[pygame.K_SPACE]:
                Missil