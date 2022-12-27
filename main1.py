import pygame
import os
import sys
import random


all_sprites = pygame.sprite.Group()
count = 0
pacman_stages = []
for i in range(1, 5):
    pacman_stages.append(pygame.image.load(f'files/{i}1.png'))


class Pacman(pygame.sprite.Sprite):
    # image = pygame.image.load("files/11.png")
    image = pacman_stages[count // 5]

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Pacman.image
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image_default = self.image
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30
        self.way_to = "RIGHT"
        self.current_way_to = "RIGHT"
        self.able_move = [1, 1, 1, 1]

        #               up, down, left, right
        # pygame.draw.rect(screen, (255, 255, 255),
        #                  (20, 20, 100, 75))

        screen.blit(self.image, [self.rect.x, self.rect.y])

    def set_direction(self, event):
        if event.key == pygame.K_w:
            self.way_to = "UP"
            # self.image = pygame.transform.rotate(self.image, 270)
        elif event.key == pygame.K_a:
            self.way_to = "LEFT"

        elif event.key == pygame.K_s:
            self.way_to = "DOWN"

        elif event.key == pygame.K_d:
            self.way_to = "RIGHT"

    def change_direction(self):

        if self.way_to == "UP" and self.able_move[0] == 1:
            self.current_way_to = "UP"
            self.image = pygame.transform.rotate(self.image_default, 90)
        elif self.way_to == "DOWN" and self.able_move[1] == 1:
            self.current_way_to = "DOWN"
            self.image = pygame.transform.rotate(self.image_default, 270)
        elif self.way_to == "LEFT" and self.able_move[2] == 1:
            self.current_way_to = "LEFT"
            self.image = pygame.transform.rotate(self.image_default, 180)
        elif self.way_to == "RIGHT" and self.able_move[3] == 1:
            self.current_way_to = "RIGHT"
            self.image = pygame.transform.rotate(self.image_default, 0)

    def move(self):
        if self.current_way_to == "UP":
            self.rect.y -= 1
        elif self.current_way_to == "DOWN":
            self.rect.y += 1
        elif self.current_way_to == "LEFT":
            self.rect.x -= 1
        elif self.current_way_to == "RIGHT":
            self.rect.x += 1
        print(2)

    def draw(self):
        self.change_direction()
        screen.blit(pacman.image, pacman.rect)
        # if self.way_to == "UP":
        #     self.image = pygame.transform.rotate(self.image, 90)
        # elif self.way_to == "DOWN":
        #     self.image = pygame.transform.rotate(self.image, 270)
        # elif self.way_to == "LEFT":
        #     self.image = pygame.transform.rotate(self.image, 180)
        # elif self.way_to == "RIGHT":
        #     self.image = pygame.transform.rotate(self.image, 0)






if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 900
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    way_to = 0
    image1 = pygame.image.load("files/11.png")
    pacman_x = 450
    pacman_y = 450
    # pygame.draw.rect(screen, (255, 255, 255),(20, 20, 100, 75))
    angle = 0
    pacman = Pacman()

    running = True
    while running:
        if count < 19:
            count += 1
        else:
            count = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pacman.set_direction(event)
                # if event.key == pygame.K_RIGHT:
                #     way_to = 'R'
                # if event.key == pygame.K_LEFT:
                #     way_to = "L"
                # if event.key == pygame.K_UP:
                #     way_to = 'U'
                # if event.key == pygame.K_DOWN:
                #     way_to = "D"
        screen.fill((0,0,0))
        pacman.move()
        pacman.draw()
        # all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(200)

    pygame.quit()