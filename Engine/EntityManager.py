from Engine import engine, group, game

class Entity_Manager():
    def __init__(self, View):
        self.entities = group()
        self.View = View

    def update_logic(self):
        self.entities.update()
    def add(self, entity = object):
        self.View.add(entity)
        self.entities.add(entity)
