class fruit:
    def __init__(self,c,s,si,t,li):
        self.colour = c
        self.shape = s
        self.size = si
        self.taste = t
        self.likeness = li
    def plusone(self):
        self.likeness = self.likeness+1
    def minusone(self):
        self.likeness = self.likeness-1
    def showdetails(self):
        print("Fruit colour is "+self.colour)
        print("Fruit shape is "+self.shape)
        print("Fruit size is "+self.size)
        print("Fruit taste is "+self.taste)
        print("Fruit likeness factor is "+str(self.likeness)+"/10")
        choice = input("Do you want to increase or decrease the likeness factor by one? ")
        if choice == "increase":
            self.plusone()
        if choice == "decrease":
            self.minusone()
    def changedetails(self):
        ss = input("What's the size")
        self.size = ss
watermelon = fruit("red","semi-circle","extra-large","sweet and juicy",8)
x = fruit("light yellow", "oval","extra-large","very sweet if ripe",5)
x.showdetails()
x.changedetails()
x.showdetails()
watermelon.showdetails()
