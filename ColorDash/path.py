import pygame
from pygame.locals import *

class Path(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def scrollPath(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left <= -self.rect.width:
            self.rect.left = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    path = Path("assets/path.png", [0,0], [-1, 0])

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        path.scrollPath()
        screen.fill((255, 255, 255))
        screen.blit(path.image, path.rect)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()