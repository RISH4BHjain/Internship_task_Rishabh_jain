recipes = [
    {"name": "Pancakes", "ingredients": ["flour", "milk", "egg", "sugar"], "type": "Breakfast"},
    {"name": "rajma rice", "ingredients": ["rajma", "rice","lemon","onion"], "type": "Lunch"},
    {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber", "olive oil"], "type": "Lunch"},
    {"name": "Omelette", "ingredients": ["egg", "cheese", "pepper"], "type": "Breakfast"},
    {"name": "Tea", "ingredients": ["sugar","tea leaves","ginger"], "type": "Breakfast"}
]

def search_recipes():
    ingredients = input("Enter ingredients (comma-separated): ").lower().split(",")
    ingredients = [i.strip() for i in ingredients]
    
    print("\nMatching Recipes:")
    found = False
    for recipe in recipes:
        if all(i in recipe["ingredients"] for i in ingredients):
            print(f"- {recipe['name']} ({recipe['type']})")
            found = True
    
    if not found:
        print("No matching recipes found.")

def filter_recipes_by_type():
    meal_type = input("Enter meal type (Breakfast/Lunch): ").capitalize()
    
    print(f"\n{meal_type} Recipes:")
    found = False
    for recipe in recipes:
        if recipe["type"] == meal_type:
            print(f"- {recipe['name']}")
            found = True
    
    if not found:
        print(f"No {meal_type} recipes found.")

def main():
    while True:
        print("\n1. Search Recipes")
        print("2. Filter by Type")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            search_recipes()
        elif choice == "2":
            filter_recipes_by_type()
        elif choice == "3":
            print("Exiting application...Thank You!!")
            break
        else:
            print("Invalid choice. Try again.")


main()
