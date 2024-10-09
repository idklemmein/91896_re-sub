def topping_id_checker(id):
    if id < 1 or id > 10:
        return ("Invalid Topping ID", 0)
    topping_dict = {
        1: ("Hummus", 2.00), 2: ("Tabbouleh", 1.50), 3: ("Baba Ganoush", 1.50),
        4: ("Garlic Sauce", 2.50), 5: ("Chili Sauce", 2.30), 6: ("Fried Onions", 3.00),
        7: ("Pickles", 2.00), 8: ("Feta Cheese", 1.00), 9: ("Grilled Veggies", 3.00),
        10: ("Pomegranate Molasses", 4.00)
    }
    return topping_dict.get(id, ("Unknown Topping", 0))


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

topping_order_id = num_check("Please enter the number of the topping you want to order (1-10): ", min_value=1,
                             max_value=10)
topping_order_name, topping_cost = topping_id_checker(topping_order_id)

print(f"You have selected {topping_order_name}")

