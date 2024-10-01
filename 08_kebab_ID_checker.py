# function to check if the correct pizza ID is entered (1-10)
def kebab_id_checker(id):
    pizza_dict = {
        1: "Chicken Kebab Wrap", 2: "Lamb Kebab Wrap", 3: "Beef Kebab Wrap",
        4: "Mixed Meat Kebab Wrap", 5: "Falafel Kebab Wrap", 6: "Halloumi Kebab Wrap",
        7: "Spicy Chicken Kebab Wrap", 8: "Vegetarian Kebab Wrap",
        9: "Lamb Kofta Kebab Wrap", 10: "Grilled Fish Kebab Wrap"
    }
    return pizza_dict.get(id, "Unknown Pizza")

# linked to num checker
def num_check(question, min_value=None, max_value=None):
    while True:
        try:
            response = int(input(question))
            if (min_value is not None and response < min_value) or (max_value is not None and response > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return response
        except ValueError:
            print("Please enter an integer.")

# Main Routine

user_order_id = (num_check
                 ("Please enter the number of the kebab you want to order (1-10): ", min_value=1, max_value=10))
user_order_name = kebab_id_checker(user_order_id)

print(f"You have selected {user_order_name}")