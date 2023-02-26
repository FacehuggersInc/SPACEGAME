img_folder = "Assets\PNG"
from Engine import os, engine, img_load, entity, WIDTH, HEIGHT, wrld_width, wrld_height

class Player(entity):
    def __init__(self):
        #Sprite
        entity.__init__(self)
        self.imageMaster = img_load(os.path.join(img_folder,"playerShip4_red.png"))
        self.image = self.imageMaster
        self.rect = self.image.get_rect()
        self.radius = 45

        #Starting pos
        self.startX = WIDTH / 2
        self.startY = HEIGHT / 2
        self.rect.centerx = self.startX  #START X Pos
        self.rect.centery =  self.startY  #START Y Pos

        self.speed = 10

    def control(self):
        #BOUNDS
        bRIGHT = self.rect.x > (wrld_width - self.image.get_width())
        bLEFT = self.rect.x < -abs(wrld_width)
        bTOP = self.rect.y < -abs(wrld_height)
        bBOTTOM = self.rect.y > (wrld_height - self.image.get_height())

        k = engine.key.get_pressed()
        if k[engine.K_w] and not bTOP:
            self.rect.y -= self.speed
        if k[engine.K_s] and not bBOTTOM:
            self.rect.y += self.speed
        if k[engine.K_a] and not bLEFT:
            self.rect.x -= self.speed
        if k[engine.K_d] and not bRIGHT:
            self.rect.x += self.speed

    def update(self):
        self.control()