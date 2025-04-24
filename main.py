from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet("Buddy")
    print(f"Welcome to Virtual Pet Game! You have a new pet named {my_pet.name}!")
    
    # Show initial status
    print("\nInitial status:")
    print(my_pet.get_status())
    
    # Demonstrate various activities
    print("\nLet's play with our pet!")
    print(my_pet.play())
    print(my_pet.get_status())
    
    print("\nTime to eat!")
    print(my_pet.eat())
    print(my_pet.get_status())
    
    print("\nLet's teach some tricks!")
    print(my_pet.train("sit"))
    print(my_pet.train("roll over"))
    print(my_pet.train("fetch"))
    print(my_pet.show_tricks())
    print(my_pet.get_status())
    
    print("\nTime for a nap!")
    print(my_pet.sleep())
    print(my_pet.get_status())

if __name__ == "__main__":
    main() 