from Engine import engine

class Input_Manager():
    def manage(self):
        k = engine.key.get_pressed()
        #Events
        for event in engine.event.get():
            #Quit
            if event.type == engine.QUIT or k[engine.K_ESCAPE]: exit()
