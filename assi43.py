class car :
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
    def move (self):
        print("go!")
class Bike :
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
    def move (self):
        print("ho!")
class ship :
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
    def move (self):
        print("vo!")

a = car ("BMW" , 2024 , "Black")
b = Bike ("Yamaha" , 2020 , "Red")
c = ship ("INS Vikarant" ,2019 , "White")

for x in (a , b , c ):
    print(x.name)
    print(x.model)
    print(x.color)
    x.move()