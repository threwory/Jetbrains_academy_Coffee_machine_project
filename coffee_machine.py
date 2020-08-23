
class CoffeeMachine:
    """A class which represent a real-word coffee machine."""

    espresso = {'water': 250, 'coffee': 16, 'cups': 1}
    latte = {'water': 350, 'milk': 75, 'coffee': 20, 'cups': 1}
    cappuccino = {'water': 200, 'milk': 100, 'coffee': 12, 'cups': 1}

    def __init__(self, money, water, milk, coffee, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups

    def current_state(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of cups")
        print(f"{self.money} of money")

    def check_supply(self, chosen_coffee):
        missed_item = []
        for k, v in chosen_coffee.items():
            if self.__getattribute__(k) > chosen_coffee[k]:
                continue
            else:
                missed_item.append(k)
                break
        return missed_item

    def buy(self):
        coffee_type = input('What do you want to buy? '
                            '1 - espresso, '
                            '2 - latte, '
                            '3 - cappuccino, '
                            'back - to main menu: ')
        if coffee_type == 'back':
            return input_action()
        elif int(coffee_type) == 1:
            item = self.check_supply(self.espresso)
            if item:
                print(f'Sorry, not enough {item[0]}!')
            else:
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
                print('I have enough resources, making you a coffee!')
        elif int(coffee_type) == 2:
            item = self.check_supply(self.latte)
            if item:
                print(f'Sorry, not enough {item[0]}!')
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!')
        else:
            item = self.check_supply(self.cappuccino)
            if item:
                print(f'Sorry, not enough {item[0]}!')
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
                print('I have enough resources, making you a coffee!')

    def fill(self):
        added_water = int(input('Write how many ml of water do you want to add:'))
        added_milk = int(input('Write how many ml of milk do you want to add:'))
        added_coffee = int(input('Write how many grams of coffee beans do you want to add:'))
        added_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
        self.water += added_water
        self.milk += added_milk
        self.coffee += added_coffee
        self.cups += added_cups

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def organize(self, input_from_console):
        if input_from_console == 'buy':
            return self.buy()
        elif input_from_console == 'fill':
            return self.fill()
        elif input_from_console == 'take':
            return self.take()


def input_action():
    action = input('Write action (buy, fill, take, remaining, exit)')
    if action == 'remaining':
        return machine1.current_state()
    else:
        return action


machine1 = CoffeeMachine(550, 400, 540, 120, 9)

while True:
    user_choice = input_action()
    if user_choice == 'exit':
        break
    else:
        machine1.organize(user_choice)
