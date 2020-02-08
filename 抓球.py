import sys
import pygame
import random
from  pygame.sprite import Sprite, Group


class Ball(Sprite):
    def __init__(self, screen):
        """初始化球"""
        super().__init__()
        self.screen = screen
        self.factor = 1
        self.ball_left = 0
        self.y = 0

        # 创建球类对象
        self.rect = pygame.draw.circle(screen, (230, 230, 230), (0, 0), 40)
        self.screen_rect = screen.get_rect()

        # 将球放到顶端任意位置
        self.rect.x = random.randint(self.rect.width, self.screen_rect.right - self.rect.width)
        self.rect.top = self.screen_rect.top

    def update(self):
        self.y += 1
        if self.rect.top > self.screen_rect.bottom:
            self.y = self.screen_rect.top
            self.ball_left += 1

        self.rect.top = self.y

    def blitme(self):
        """绘制角色图像"""
        pygame.draw.circle(self.screen, (0, 0, 0), (self.rect.x, self.rect.bottom), 40)

class Role:
    def __init__(self, screen):
        """初始化角色位置"""
        self.screen = screen
        self.factor = 1

        # 创建角色对象
        self.rect = pygame.Rect(0, 0, 300, 8)
        self.screen_rect = screen.get_rect()

        # 将角色放在底端中心位置
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

        # 角色位置储存小数值
        self.center = float(self.rect.centerx)


        # 移动标志
        self.moving_left = False
        self.moving_right = False


    def update(self):
        """根据移动标志调整球位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.factor

        self.rect.centerx = self.center

    def blitme(self):
        """绘制角色图像"""
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)





def rungame():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("抓球")


    balls = Group()
    # 创建一个角色和球
    ball = Ball(screen)
    balls.add(ball)
    role = Role(screen)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    role.moving_right = True
                elif event.key == pygame.K_LEFT:
                    role.moving_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    role.moving_right = False
                elif event.key == pygame.K_LEFT:
                    role.moving_left = False


        screen.fill((230, 230, 230))
        if ball.ball_left < 3:
            ball.update()
            if pygame.sprite.spritecollideany(role, balls):
                balls.remove(ball)
            if len(balls) == 0:
                ball = Ball(screen)
                balls.add(ball)
            role.update()
            ball.blitme()
            role.blitme()

        pygame.display.flip()

rungame()


