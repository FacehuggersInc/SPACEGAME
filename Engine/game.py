from Engine import WIDTH, HEIGHT, FPS, refresh

from Engine.camera import Camera
from Engine.InputManager import Input_Manager
from Engine.EntityManager import Entity_Manager
from Engine.Entities.player import Player
from Engine.Entities.planet import Planet

class Game():
    def __init__(self, engine):
        #Setup Engine
        self.engine = engine
        self.engine.init()
        self.engine.mixer.init()
        self.CLOCK = self.engine.time.Clock()
        self.DISPLAY = engine.display.set_mode((WIDTH,HEIGHT))
        self.engine.display.set_caption(f"SPACE GAME")

        #Camera
        self.CAMERA = Camera((0,0,0), self.engine, self.DISPLAY)

        #Input
        self.IM = Input_Manager()

        #Entity Control/Manage
        self.EM = Entity_Manager(self.CAMERA)

        #Game Variables
        self.running = False
    
    def run(self):
        #PREGAME
        planet = Planet()
        self.EM.add(planet)
        player = Player()
        self.EM.add(player)

        #Set Camera Target
        self.CAMERA.target = player

        #Main Loop
        self.running = True
        while self.running:#The Game
            #START
            self.CLOCK.tick(FPS)#Tick Clock
            self.IM.manage() #InputManage

            #UPDATE | BEFORE ENTITIES
            self.CAMERA.center_on_target()

            self.EM.update_logic()
            #UPDATE | AFTER ENTITIES

            #DRAW/RENDER
            self.CAMERA.draw()

            #END
            refresh()#Refresh Display
