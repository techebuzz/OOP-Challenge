class Pet:
    def __init__(self, name):
        """Initialize a new pet with given name and default values for attributes."""
        self.name = name
        self.hunger = 5  # Starting at middle value
        self.energy = 10  # Starting at full energy
        self.happiness = 5  # Starting at middle value
        self.tricks = []  # List to store learned tricks (bonus feature)
    
    def eat(self):
        """Feed the pet to reduce hunger and increase happiness."""
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger but not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness but not above 10
        return f"{self.name} has eaten and is feeling better!"
    
    def sleep(self):
        """Let the pet sleep to increase energy."""
        self.energy = min(10, self.energy + 5)  # Increase energy but not above 10
        return f"{self.name} had a good sleep and is now energized!"
    
    def play(self):
        """Play with the pet to increase happiness but consume energy and increase hunger."""
        if self.energy < 2:
            return f"{self.name} is too tired to play!"
        
        self.energy = max(0, self.energy - 2)  # Decrease energy but not below 0
        self.happiness = min(10, self.happiness + 2)  # Increase happiness but not above 10
        self.hunger = min(10, self.hunger + 1)  # Increase hunger but not above 10
        return f"{self.name} had fun playing!"
    
    def get_status(self):
        """Return the current status of the pet."""
        return f"""
Status of {self.name}:
Hunger: {self.hunger}/10 {'🍽️' if self.hunger > 7 else ''}
Energy: {self.energy}/10 {'😴' if self.energy < 3 else ''}
Happiness: {self.happiness}/10 {'😊' if self.happiness > 7 else '😢' if self.happiness < 3 else ''}
"""
    
    def train(self, trick):
        """Teach the pet a new trick (bonus feature)."""
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)  # Increase happiness for learning
            self.energy = max(0, self.energy - 1)  # Decrease energy from training
            return f"{self.name} learned how to {trick}!"
        return f"{self.name} already knows how to {trick}!"
    
    def show_tricks(self):
        """Display all tricks the pet knows (bonus feature)."""
        if not self.tricks:
            return f"{self.name} doesn't know any tricks yet!"
        return f"{self.name}'s tricks: {', '.join(self.tricks)}" 