#HAPPY DIWALI


print("🪔HAPPY DIWALI🪔")
print("=====================")

print("Wishing you a joyous and prosperous Diwali filled with love, light, and happiness!")
print("======================================================================================")

print("May the festival of lights bring you and your family good health, wealth, and success in all your endeavors.")
print("===============================================================================================================")

name= input("Enter your name: ")
print(f"Happy Diwali, {name}! 🪔")

print("What would you like to do today?")
print("1. Light diyas! 🪔")
print("2. Burst crackers! 🎆")
print("3. Enjoy sweets! 🍬")
print("4. Decorate your home! 🏠")

activity=input("Enter your choice")

match activity:
    case "1":
        print("Light diyas! 🪔")
    case "2":
        print("Burst crackers! 🎆")
    case "3":
        print("Enjoy sweets! 🍬")
    case "4":
        print("Decorate your home! 🏠")
    case _:
        print("You don't have any other option, but you can still enjoy the festival! 🪔")