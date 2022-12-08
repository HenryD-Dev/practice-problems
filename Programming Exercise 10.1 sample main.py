import classPet

def main():
    name = input('What is your pet\'s name? ')
    animal_type = input('What is your pet\'s animal type? ')
    age = input('What is your pet\'s age? ')
    
    my_pet = classPet.Pet(name, animal_type, age)

    print('Your pet\'s name is', my_pet.get_name())
    print(my_pet.get_name(), 'is a', my_pet.get_animal_type())
    print(my_pet.get_name(), 'is', my_pet.get_age(), 'years old.')
     
    
main()
