from Engine import group

class Camera(group):
    def __init__(self, bg_color, engine, DISPLAY):
        super().__init__()
        self.display_surface = DISPLAY
        
        #Targeting
        self.target = None

        #Camera Offset
        self.offset = engine.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        #BG Color
        self.bg_color = bg_color

        #Reference Background Surface
        self.background = engine.Surface((1,1))
        self.background.fill(self.bg_color)
        self.bg_rect = self.background.get_rect()

    def center_on_target(self):
        if self.target:
            self.offset.x = self.target.rect.centerx - self.half_w
            self.offset.y = self.target.rect.centery - self.half_h

    def draw(self):
        #Consitant BG
        self.display_surface.fill(self.bg_color)

        #Refernce BG
        bg_offset = self.bg_rect.topleft - self.offset
        self.display_surface.blit(self.background, bg_offset)

        #All Sprites
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
