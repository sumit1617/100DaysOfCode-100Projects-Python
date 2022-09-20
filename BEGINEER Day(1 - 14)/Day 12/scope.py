# Local scope
def drink_potion():
    potion = 2
    print(potion)

drink_potion()

# Global scope
men_health = 10
def health():
    women_health = 8
    print(men_health)
health()

# There is no block scope in python
import random
game_level = 3
def create_enemy():
    """Note :- If we have declared any variable,list,dictionary or any kind of stuff we can use that inside the function only
           not outside the function. if the any kind of stuff is declared inside the (if,for,while) we can use it anywhere."""
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = random.choice(enemies)
        print(new_enemy)

create_enemy()

# Modifying global scope ---> Above one is that we can use the outside declared variable or any kind of stuff inside the function.

enemies = 1
def  increase_enemy():
    """It is recommened that plz don't modify the global scope, bcz in future it can create bugs when you will n no of projects"""
    global enemies
    enemies += 1
increase_enemy() 
print(enemies) 

# Global Constants
PI = 3.14125
URL = "https://www.google.com"
TWITTER_HANDLE = "@sumit.singh____"

def global_constants():
    """You can use the global constants because it will not change as you go deep in the code.
       but it should all in the capital letters, after that in the function u can use without using global keyword"""
    print(f"{PI}\n{URL}\n{TWITTER_HANDLE}")
global_constants()

