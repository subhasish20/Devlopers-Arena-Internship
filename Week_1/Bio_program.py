name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

favorite_foods = ["Pizza", "Sushi", "Tacos"]

print("\n--- Bio Data ---")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Favorite Foods:")
for food in favorite_foods:
    print("->", food)