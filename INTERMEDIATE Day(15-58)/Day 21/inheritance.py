class Animal:
    def __init__(self):
        self.num_of_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()   #This is inheritance. we can use other class function inside the new class.

# if we want to modify the other class function inside the new class. let's se above.

    def breathe(self):
        super().breathe()
        print("but inside the water")

    

    def swim(self):
        print("moving in water")

rocky = Fish()
rocky.swim()
rocky.breathe()


# Can we used the f string for combining the two class's functions