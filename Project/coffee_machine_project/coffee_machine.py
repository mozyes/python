# coffee machine
from flavors import flavor
from resources import resource
from differentcoins import coins


def user_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_user_coins = quarters * coins["quarter"] + dimes * coins["dime"] + nickels * coins["nickel"] + pennies * \
                       coins["penny"]
    remain_water = resource["water"] - flavor[user_choice]["water"]
    remain_milk = resource["milk"] - flavor[user_choice]["milk"]
    remain_coffee = resource["coffee"] - flavor[user_choice]["coffee"]
    if total_user_coins >= flavor[user_choice]["price"]:
        if remain_water >= 0 and remain_milk >= 0 and remain_coffee >= 0:
            change = total_user_coins - flavor[user_choice]["price"]
            print(f"Here is ${change:.2f} in change.")
            print(f"Here is your {user_choice}. Enjoy!")

            # Update the resources after a successful purchase
            resource["water"] = remain_water
            resource["milk"] = remain_milk
            resource["coffee"] = remain_coffee
        else:
            # Return coins and print an error message if resources are not enough
            print(f"Sorry, we are out of some resources for {user_choice}.")
            print(f"Here is your ${total_user_coins:.2f} back.")
            return None, None, None
    else:
        # Return coins and print an error message if there are insufficient funds
        print("Insufficient funds.")
        print(f"Here is your ${total_user_coins:.2f} back.")
        return None, None, None

    return resource["water"], resource["milk"], resource["coffee"]


remaining_resource = True
while remaining_resource:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    remaining_water, remaining_milk, remaining_coffee = user_coins()
    if remaining_water is None or remaining_milk is None or remaining_coffee is None:
        remaining_resource = False
    elif remaining_water < 0 or remaining_milk < 0 or remaining_coffee < 0:
        print("Sorry, we are out of some resources. The machine will stop.")
        remaining_resource = False
