class Duck :
    def __init__(self, image):
        self.image = pygame.image.load('./assets/duck.png')
        self.x = random.randrange(100, 600)
        self.y = random.randrange(100, 600)
        self.pos = (self.x, self.y)
        self.rect = self.get_rect( center = (self.x , self.y) )
    def draw (self, ecran):
        print(self.x)
        print(self.y)
        try:
            ecran.blit(duck, self)
        except:
            print(self.x)
            print(self.y)