italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]


def find_meal(name, menu):
  if name in menu:
    return name
  else:
    return None

def select_meal(name, food_type):
  if food_type == "Italian":
    return find_meal(name, italian_food)
  elif food_type == "Indian":
    return find_meal(name, indian_food)
  else:
    return None

def display_available_meals(food_type):
  if food_type == "Italian":
    print("Available Italian Meals:")
    for meal in italian_food:
      print(meal)
  elif food_type == "Indian":
    print("Available Indian Meals:")
    for meal in indian_food:
      print(meal)
  else:
    print("Invalid food type!")

def create_summary(name, amount, food_type):
  order = select_meal(name, food_type)
  if order:
    return f"{amount} {order} on the way!"
  else:
    return f"Meal not found"


print("Welcome to the Food Ordering System!")
type_input = input("What type of food would you like? ")
display_available_meals(type_input)
name_input = input("What meal would you like? ")
amount_input = input("How many would you like? ")
result = create_summary(name_input, amount_input, type_input)
print(result)

