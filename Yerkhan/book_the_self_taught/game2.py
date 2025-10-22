import pygame
import random
import sys
from typing import List

# Simple "Dodge the falling blocks" game using pygame.
# Save this file as game2.py and run with: python game2.py

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 16
PLAYER_COLOR = (50, 200, 50)
PLAYER_SPEED = 420  # pixels per second

ENEMY_MIN_SIZE = 20
ENEMY_MAX_SIZE = 60
ENEMY_COLOR = (200, 50, 50)
ENEMY_BASE_SPEED = 180  # starting falling speed
ENEMY_SPEED_INCREASE = 3  # speed increase per second of play

SPAWN_INTERVAL = 0.6  # seconds between enemies at start
SPAWN_MIN_INTERVAL = 0.12
SPAWN_ACCELERATION = 0.006  # how much spawn interval reduces per second

BG_COLOR = (30, 30, 40)
TEXT_COLOR = (240, 240, 240)

pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont(None, 28)
BIG_FONT = pygame.font.SysFont(None, 56)
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodge - simple pygame game")


class Player:
    def __init__(self):
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.x = (SCREEN_WIDTH - self.width) / 2
        self.y = SCREEN_HEIGHT - self.height - 18
        self.color = PLAYER_COLOR
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt, keys):
        dx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
        self.x += dx * PLAYER_SPEED * dt
        # clamp
        if self.x < 0:
            self.x = 0
        if self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
        self.rect.topleft = (self.x, self.y)

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=6)


class Enemy:
    def __init__(self, speed):
        self.size = random.randint(ENEMY_MIN_SIZE, ENEMY_MAX_SIZE)
        self.x = random.uniform(0, SCREEN_WIDTH - self.size)
        self.y = -self.size
        self.speed = speed
        # random slight color variation
        r = min(255, ENEMY_COLOR[0] + random.randint(-30, 30))
        g = max(0, min(255, ENEMY_COLOR[1] + random.randint(-30, 30)))
        b = max(0, min(255, ENEMY_COLOR[2] + random.randint(-30, 30)))
        self.color = (r, g, b)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self, dt):
        self.y += self.speed * dt
        self.rect.topleft = (self.x, self.y)

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=6)


def draw_text_center(surf, text, y, font, color=TEXT_COLOR):
    img = font.render(text, True, color)
    rect = img.get_rect(center=(SCREEN_WIDTH / 2, y))
    surf.blit(img, rect)


def main():
    player = Player()
    enemies: List[Enemy] = []
    running = True
    game_over = False

    score = 0.0
    total_time = 0.0
    spawn_timer = 0.0
    spawn_interval = SPAWN_INTERVAL

    while running:
        dt = CLOCK.tick(FPS) / 1000.0
        total_time += dt
        if not game_over:
            score += dt * 10  # score increases with time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if game_over and event.key == pygame.K_r:
                    # restart
                    player = Player()
                    enemies = []
                    game_over = False
                    score = 0.0
                    total_time = 0.0
                    spawn_timer = 0.0
                    spawn_interval = SPAWN_INTERVAL

        keys = pygame.key.get_pressed()

        if not game_over:
            player.update(dt, keys)

            # spawn logic
            spawn_timer += dt
            # progressively make spawn interval shorter (higher difficulty)
            spawn_interval = max(SPAWN_MIN_INTERVAL, SPAWN_INTERVAL - SPAWN_ACCELERATION * total_time)
            if spawn_timer >= spawn_interval:
                # enemy speed increases with time
                speed = ENEMY_BASE_SPEED + ENEMY_SPEED_INCREASE * total_time
                enemies.append(Enemy(speed))
                spawn_timer = 0.0

            # update enemies
            for e in enemies:
                e.update(dt)

            # remove off-screen enemies
            enemies = [e for e in enemies if e.y <= SCREEN_HEIGHT + 200]

            # collision detection
            for e in enemies:
                if player.rect.colliderect(e.rect):
                    game_over = True
                    break

        # drawing
        SCREEN.fill(BG_COLOR)

        # draw player and enemies
        player.draw(SCREEN)
        for e in enemies:
            e.draw(SCREEN)

        # HUD
        draw_text_center(SCREEN, f"Score: {int(score)}", 24, FONT)
        draw_text_center(SCREEN, f"Time: {int(total_time)}s", 52, FONT)
        draw_text_center(SCREEN, "Move: ← → or A D    Quit: ESC", SCREEN_HEIGHT - 28, FONT)

        if game_over:
            # overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((10, 10, 10, 180))
            SCREEN.blit(overlay, (0, 0))
            draw_text_center(SCREEN, "GAME OVER", SCREEN_HEIGHT / 2 - 40, BIG_FONT)
            draw_text_center(SCREEN, f"Final Score: {int(score)}", SCREEN_HEIGHT / 2 + 10, FONT)
            draw_text_center(SCREEN, "Press R to restart or ESC to quit", SCREEN_HEIGHT / 2 + 50, FONT)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()