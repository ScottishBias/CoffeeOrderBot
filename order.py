class Orders:

    def __init__(self, name, coffee, iced, milk, decaff, size, time):
        self.name = name
        self.iced = iced
        self.coffee= coffee
        self.milk = milk
        self.decaff = decaff
        self.size = size
        self.time = time

    def __repr__(self):
        return f"('{self.name}', '{self.coffee}', '{self.iced}', '{self.milk}', '{self.decaff}', '{self.size}', '{self.time}')"        
        
