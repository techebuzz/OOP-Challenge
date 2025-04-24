# 🐶 Python OOP Challenge: Build Your Own Digital Pet

Welcome to this week's Python challenge! 🎉

In this challenge, you’ll be creating a virtual pet using Object-Oriented Programming concepts in Python. This fun project will help you practice how to use classes, attributes, methods, and constructors.

---

## 🧠 Objective

Create a class called `Pet` with the following:

### Attributes:
- `name`: the name of your pet
- `hunger`: an integer representing hunger level (0 = full, 10 = very hungry)
- `energy`: an integer representing energy level (0 = tired, 10 = fully rested)
- `happiness`: an integer (0–10)

### Methods:
- `eat()`: reduces hunger by 3 points (but not below 0), and increases happiness by 1.
- `sleep()`: increases energy by 5 points (but not above 10).
- `play()`: decreases energy by 2, increases happiness by 2, and increases hunger by 1.
- `get_status()`: prints the current state of the pet.

### Bonus 🎯
- Add a method `train(trick)` that teaches your pet a new trick and stores it in a list.
- Add a method `show_tricks()` that prints all learned tricks.

---

## 📝 How to Complete
1. `Pet` class in `pet.py`.
2. `main.py`, create a pet object and call its methods to test functionality.
   

---

## ✅ Output

```bash
Welcome to Virtual Pet Game! You have a new pet named Buddy!

Initial status:

Status of Buddy:        
Hunger: 5/10 
Energy: 10/10 
Happiness: 5/10         


Let's play with our pet!
Buddy had fun playing!  

Status of Buddy:        
Hunger: 6/10 
Energy: 8/10 
Happiness: 7/10         


Time to eat!
Buddy has eaten and is feeling better!

Status of Buddy:
Hunger: 3/10
Energy: 8/10
Happiness: 8/10 😊


Let's teach some tricks!
Buddy learned how to sit!
Buddy learned how to roll over!
Buddy learned how to fetch!
Buddy's tricks: sit, roll over, fetch

Status of Buddy:
Hunger: 3/10
Energy: 5/10
Happiness: 10/10 😊


Time for a nap!
Buddy had a good sleep and is now energized!

Status of Buddy:
Hunger: 3/10
Energy: 10/10
Happiness: 10/10 😊



### 💡 Tips
Use max() and min() to keep values between 0 and 10.

Think about edge cases like trying to play when energy is 0.

🏁 Submission

Submission format: clone/fork this repo

Bonus points for creativity (custom actions, emojis, pet types, etc.)
