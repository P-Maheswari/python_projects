import greetings

def madlib():
    firstname = input("your first name:")
    lastname = input("your last name:")
    name=firstname+lastname
    placeofbirth = input("enter where you come from:")
    greetings.madlib()
    madlib = f" I'm {name}. I come from {placeofbirth}."
    print(madlib)

