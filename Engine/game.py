from Engine.InputManager import Input_Manager

class Game():
    def __init__(self, engine):
        self.FPS = 165
        self.WIDTH = 800#px
        self.HEIGHT = 500#px

        self.running = False

        self.engine = engine
        self.engine.init()
        self.engine.mixer.init()

        self.CLOCK = self.engine.time.Clock()

        self.DISPLAY = self.engine.display
        self.DISPLAY.set_mode((self.WIDTH,self.HEIGHT))
        self.DISPLAY.set_caption(f"SPACE GAME")

        self.IM = Input_Manager()

        print("[GAME] Instantiated")
    
    def run(self):
        self.running = True
        print("[GAME] Running")

        #Main Loop
        while self.running:
            self.CLOCK.tick(self.FPS)#Tick Clock
            self.IM.manage(self.engine) #InputManage

            self.engine.display.flip()#Refresh Display
