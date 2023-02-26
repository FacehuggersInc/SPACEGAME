
from Engine import img_load, entity, randint

class Planet(entity):
    def __init__(self):
        #Sprite
        entity.__init__(self)
        self.imageMaster = img_load("A:\PY\Projects\SPACEGAME\Assets\PNG\Planets\planet18.png")
        self.image = self.imageMaster
        self.rect = self.image.get_rect()

        #Starting pos
        self.startX = 120
        self.startY = 120
        self.rect.centerx = self.startX  #START X Pos
        self.rect.centery =  self.startY  #START Y Pos