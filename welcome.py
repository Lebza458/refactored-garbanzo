# USE DEF FUNCTION TO CREATE OWN FUNCTION
def hello():
    print("Hello user")

def welcome(to):
    print("Welcome", to)
hello()
name = input("What is your name? ").strip().title()
welcome(name)