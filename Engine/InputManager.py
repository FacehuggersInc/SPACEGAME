class Input_Manager():
    def __init__(self):
        print("[InputManager] Instantiated")
    
    def manage(self, engine):
        k = engine.key.get_pressed()

        #Events
        for event in engine.event.get():
            #Quit
            if event.type == engine.QUIT or k[engine.K_ESCAPE]: exit()

            #Key Report
            if event.type == engine.KEYDOWN:
                key = str(event)
                key = key[20:]
                key = key.split(",")
                key = key[0].split(":")
                key = key[1].replace(" ","")
                print(f"[InputManager]: [{key}] pressed.")
