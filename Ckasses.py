class fruit:
    def __init__(self,c,s,si,t):
        self.colour = c
        self.shape = s
        self.size = si
        self.taste = t
    def showdetails(self):
        print("Fruit colour is "+self.colour)
        print("Fruit shape is "+self.shape)
        print("Fruit size is "+self.size)
        print("Fruit taste is "+self.taste)
    def changedetails(self):
        ss = input("What's the size")
        self.size = ss
watermelon = fruit("red","semi-circle","extra-large","sweet and juicy")
x = fruit("light yellow", "oval","extra-large","very sweet if ripe")
x.showdetails()
x.changedetails()
x.showdetails()
watermelon.showdetails()
