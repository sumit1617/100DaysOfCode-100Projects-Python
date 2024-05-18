# Function that allows more than 1 input

def greet_with(Name, location):
    print(f"Hello {Name}, I know you stay in {location}")

Name = input("Type you name: ")
location = input("Type you location: ")
greet_with(location=location, Name=Name)


# IMP points
""""Positional Argument ---> it is nothing but we have to arrange the data in order wise while calling the function 
like we have doen while defining the funtion """
# Keyword Argument ---> in this we can arrange the data in any order while calling but we have to use keyword (=)