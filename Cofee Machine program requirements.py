class CoffeeMachine:
    MENU = {
        "espresso": {
            "ingredients": {"water": 50, "coffee": 18},
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {"water": 200, "milk": 150, "coffee": 24},
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {"water": 250, "milk": 100, "coffee": 24},
            "cost": 3.0,
        }
    }

    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}
        self.is_on = True

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources.get('milk', 0)}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['money']}")

    def is_resource_sufficient(self, drink):
        ingredients = self.MENU[drink]["ingredients"]
        for item in ingredients:
            if self.resources.get(item, 0) < ingredients[item]:
                print(f"Sorry, there is not enough {item}.") 
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        return quarters + dimes + nickels + pennies

    def transaction_successful(self, inserted_money, drink_cost):
        if inserted_money < drink_cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        change = round(inserted_money - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        self.resources["money"] += drink_cost
        return True

    def make_coffee(self, drink):
        ingredients = self.MENU[drink]["ingredients"]
        for item in ingredients:
            self.resources[item] -= ingredients[item]
        print(f"Here is your {drink}. Enjoy!")

    def run(self):
        while self.is_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                print("Turning off the coffee machine. Goodbye!")
                self.is_on = False
            elif choice == "report":
                self.report()
            elif choice in self.MENU:
                if self.is_resource_sufficient(choice):
                    payment = self.process_coins()
                    if self.transaction_successful(payment, self.MENU[choice]["cost"]):
                        self.make_coffee(choice)
            else:
                print("Invalid input. Please choose a valid option.")


# Run the Coffee Machine
machine = CoffeeMachine()
machine.run()
