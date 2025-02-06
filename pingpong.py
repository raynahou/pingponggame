from pygame import *


# parent class for sprites
class GameSprite(sprite.Sprite):
    # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)

        # every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# work on the rackets/players
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    # make another one for left racket (update_l), keys: w (up) & s (down)
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


# create game window
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PingPong")
back = (200, 255, 255)
window.fill(back)

# creating ball and paddles
racket1 = Player('racket.jpg', 30, 200, 4, 50, 150)
racket2 = Player('racket.jpg', 520, 200, 4, 50, 150)
ball = GameSprite('tennis_ball.jpg', 200, 200, 4, 50, 50)

# create game loop
run = True
finish = False
clock = time.Clock()
FPS = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()

    display.update()
    clock.tick(FPS)
