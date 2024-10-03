# pandas is imported to create and manipulate a DataFrame, which is used to store and calculate the order details such as items, quantities, prices, and total costs.
import pandas

# functions go here

# Checks that user has a valid response (e.g. yes/no, cash/credit) based on the list of options
def string_checker(question, valid_ans):
    while True:
        error = f"Enter a valid response from {valid_ans}"
        user_response = input(question).lower()
        if user_response in valid_ans or user_response in [item[0] for item in valid_ans]:
            return valid_ans[[item[0] for item in valid_ans].index(user_response)] if user_response in [item[0] for item in valid_ans] else user_response
        print(error)

# Prints welcome message
def welcome_message():
    print("                   <--- Welcome to Divine Kebab --->")
    print("In our kebab place, you will order and eat quality kebabs, made with premium ingredients")
    print("Keep in mind, on our special anniversary event every 3rd kebab is on a 50% discount!! "
          "(toppings are not included in the discount)")

# Shows history of the Divine Kebab
def history():
    print('''
 The Divine Kebab Restaurant traces its roots back to 1000 BC, when nomadic tribes in the Middle East
 began skewering and roasting meat over open fires, creating the earliest form of kebabs. This ancient cooking tradition
 was passed down through generations, evolving with regional spices and techniques.
 By the Ottoman Empire, kebabs became a celebrated dish across the Middle East, 
 eventually making their way to Europe and beyond. The modern-day Divine Kebab Restaurant, 
 founded in 1982, honors this rich history by using traditional recipes and authentic cooking methods. 
 Today, it stands as a testament to thousands of years of culinary heritage.
    ''')

# Display kebab Menu
def show_kebab_menu():
    print('''\n
    ***** Kebab Menu *****
   1. Chicken Kebab Wrap         Regular: $12.50       Large: $15.00
   2. Lamb Kebab Wrap            Regular: $13.00       Large: $16.00
   3. Beef Kebab Wrap            Regular: $12.00       Large: $14.50
   4. Mixed Meat Kebab Wrap      Regular: $14.00       Large: $17.00
   5. Falafel Kebab Wrap         Regular: $10.50       Large: $13.00
   6. Halloumi Kebab Wrap        Regular: $11.50       Large: $14.00
   7. Spicy Chicken Kebab Wrap   Regular: $13.00       Large: $16.00
   8. Vegetarian Kebab Wrap      Regular: $10.00       Large: $12.50
   9. Lamb Kofta Kebab Wrap      Regular: $13.50       Large: $16.50
  10. Grilled Fish Kebab Wrap    Regular: $14.50       Large: $17.50


    ******************************
    ''')

# Display Toppings Menu
def show_toppings_menu():
    print('''\n
    ***** Toppings Menu *****
   1. Hummus
   2. Extra Cheese
   3. Avocado
   4. Grilled Mushrooms
   5. Pickles
   6. Garlic Sauce
   7. Chilli Sauce
   8. Feta Cheese
   9. Olives
   10. Tabbouleh
    ******************************
''')

# Gather Customer Information
def get_customer_info():
    name = validate_name("Please enter your name: ")
    phone = validate_phone("Please enter your phone number (max 14 digits): ")
    return name, phone


# Validates that the name contains only letters
def validate_name(question):
    while True:
        response = input(question).strip()
        if all(letters.isalpha() or letters.isspace() for letters in response):
            return response
        else:
            print("Invalid input. Please enter letters only.")



# Validates that the phone number contains only
# digits and is no more than 14 digits long
def validate_phone(question):
    while True:
        response = input(question).strip()
        if response.isdigit() and len(response) <= 14:
            return response
        else:
            print("Invalid input. Please enter digits only, with a maximum of 14 digits.")

# Set maximum number of kebabs/toppings below
MAX_kebabS = 5

# List to hold kebab details
kebab_dict = {
    1: "Chicken Kebab Wrap",
    2: "Lamb Kebab Wrap",
    3: "Beef Kebab Wrap",
    4: "Mixed Meat Kebab Wrap",
    5: "Falafel Kebab Wrap",
    6: "Halloumi Kebab Wrap",
    7: "Spicy Chicken Kebab Wrap",
    8: "Vegetarian Kebab Wrap",
    9: "Lamb Kofta Kebab Wrap",
    10: "Grilled Fish Kebab Wrap"
}


topping_dict = {
    1: "Hummus",
    2: "Extra Cheese",
    3: "Avocado",
    4: "Grilled Mushrooms",
    5: "Pickles",
    6: "Garlic Sauce",
    7: "Chilli Sauce",
    8: "Feta Cheese",
    9: "Olives",
    10: "Tabbouleh"
}
# Prices for kebabs
kebab_prices = {
    1: [12.50, 15.00],  # Chicken Kebab Wrap
    2: [13.00, 16.00],  # Lamb Kebab Wrap
    3: [12.00, 14.50],  # Beef Kebab Wrap
    4: [14.00, 17.00],  # Mixed Meat Kebab Wrap
    5: [10.50, 13.00],  # Falafel Kebab Wrap
    6: [11.50, 14.00],  # Halloumi Kebab Wrap
    7: [13.00, 16.00],  # Spicy Chicken Kebab Wrap
    8: [10.00, 12.50],  # Vegetarian Kebab Wrap
    9: [13.50, 16.50],  # Lamb Kofta Kebab Wrap
    10: [14.50, 17.50]  # Grilled Fish Kebab Wrap
}
# Checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry, this can't be blank. Please try again.")
        else:
            return response

# Checks users enter an integer to a given question
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer.")

# Main routine for ordering kebab
def order_kebab():
    order = []
    item_list = []
    quantity_list = []
    price_list = []

    kebab_count = 0  # Counter to track the number of kebabs ordered


    while len(order) < MAX_kebabS:
        kebab_num = num_check("Enter the number of the kebab you would like to order (1-10) or '0' to finish: ")
        if kebab_num == 0:
            break
        elif kebab_num in kebab_dict:
            quantity = num_check(f"How many of {kebab_dict[kebab_num]} would you like to order? ")
            size = string_checker("Would you like a regular or large kebab? (r/l): ", ["r", "l"])
            for _ in range(quantity):
                kebab_count += 1
                price = kebab_prices[kebab_num][0] if size == "r" else kebab_prices[kebab_num][1]

                # Apply 50% discount to every third kebab
                if kebab_count % 3 == 0:
                    price *= 0.5

                order.append((kebab_dict[kebab_num], size))
                item_list.append(kebab_dict[kebab_num])
                quantity_list.append(1)
                price_list.append(price)
        else:
            print("Invalid kebab number, please choose a valid number between 1 and 10.")
    return order, item_list, quantity_list, price_list

# Function to order toppings
def order_toppings(item_list, quantity_list, price_list, num_kebabs):
    toppings = []
    topping_price = 1.50  # Example price per topping
    for i in range(num_kebabs):
        print(f"\nToppings for kebab {i + 1}:")
        while True:
            topping_num = num_check(
                "Enter the number of a topping you would like to add (1-10) or '0' to finish toppings: ")
            if topping_num == 0:
                break
            elif topping_num in topping_dict:
                toppings.append(topping_dict[topping_num])
                item_list.append(f"Topping for kebab {i + 1}: {topping_dict[topping_num]}")
                quantity_list.append(1)
                price_list.append(topping_price)
            else:
                print("Invalid topping number, please choose a valid number between 1 and 10.")
    return toppings

# Function to calculate total price
def calculate_price(prices, delivery_surcharge):
    total_price = sum(prices)
    total_price += delivery_surcharge
    return total_price

# Function to process payment
def process_payment(total_price):
    print(f"Your total is ${total_price:.2f}.")
    payment_method = string_checker("Would you like to pay by cash or credit? ", ["cash", "credit"])
    if payment_method == "cash":
        print("Please have your cash ready upon delivery or pickup.")
    else:
        print("Please swipe your card when the delivery arrives or at the counter upon pickup.")

# Function to print the order summary
def print_order_summary(expense_frame, delivery_surcharge, sub_total, kebab_count):
    print("\n********* Order Summary *********")
    print(expense_frame)
    print(f"\nSubtotal: ${sub_total:.2f}")
    if delivery_surcharge > 0:
        print(f"Delivery Surcharge: ${delivery_surcharge:.2f}")
    print(f"Total: ${sub_total + delivery_surcharge:.2f}")
    if kebab_count >= 3:
        print("\nNote: Your total includes a 50% discount on every 3rd kebab ordered!")
    print("*********************************")

# Main routine
def main():
    welcome_message()

    yes_no = ["yes", "no"]
    pick_del = ["delivery", "pick up"]

    want_history = string_checker("\nWould you like to learn about the history of Divine Kebab? ", yes_no)
    if want_history == "yes":
        history()

    name, phone = get_customer_info()

    want_order = string_checker(f"Hello, {name}, would you like to order delivery or pick up? ", pick_del)
    delivery_surcharge = 0
    if want_order == "delivery":
        print("A $5 surcharge will be applied to your order!")
        delivery_surcharge = 5
    elif want_order == "pick up":
        print("Our address is:")
        print("565 Maunganui Road, Mount Maunganui 3116.")
        print("See you soon!\n")

    # Automatically display the kebab menu after choosing delivery or pick up
    show_kebab_menu()

    order, item_list, quantity_list, price_list = order_kebab()

    if order:
        print("\nYour kebab order is:")
        for item in order:
            print(f"- {item[0]} ({'Regular' if item[1] == 'r' else 'Large'})")

        add_toppings = string_checker("\nWould you like to add toppings to your kebab(s)? ", yes_no)
        if add_toppings == "yes":
            show_toppings_menu()
            toppings = order_toppings(item_list, quantity_list, price_list, len(order))
        else:
            print("No toppings added.")

        # Create DataFrame
        variable_dict = {
            'Item': item_list,
            'Quantity': quantity_list,
            'Price': price_list
        }
        expense_frame = pandas.DataFrame(variable_dict)
        expense_frame = expense_frame.set_index('Item')

        # Calculate cost of each component
        expense_frame['Cost'] = expense_frame['Price']

        # Find sub-total
        sub_total = expense_frame['Cost'].sum()

        # Print the final order summary, including kebab count
        kebab_count = len(order)
        print_order_summary(expense_frame, delivery_surcharge, sub_total, kebab_count)

        total_price = calculate_price(price_list, delivery_surcharge)
        process_payment(total_price)
        print("Thank you for ordering from Divine Kebab! Your order will be ready soon.")
    else:
        print("Thank you! Have a nice day.")

if __name__ == "__main__":
    main()