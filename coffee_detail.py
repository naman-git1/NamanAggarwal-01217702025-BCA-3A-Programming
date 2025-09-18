menu = {
    'espresso': {
        'ingredients':{
            'water':50 , 'coffee': 18}
        ,'cost':1.50},
    'latte': {
        'ingredients':{
            'water':200 ,'milk':150 , 'coffee': 24}
        ,'cost':2.50},}
resources = {'water':1000,
             'milk':900,
             'coffee':200}
profit = 0


def is_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True


def coin_calc():
    print("please insert coins!")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    total += int(input("how many dime?: ")) * 0.1
    return total


def is_tran_success(money_received , drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost , 2)
        print(f"here is your change {change}$")
        global profit
        profit += drink_cost
        return True
    else:
        print("not enough money sorry here is a refund ")
        return False


def make_coffee(drink_name,ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"here is your {drink_name}🤫")


on = True
while on:
    order = input("what would u like to order espresso($1.50) or latte($2.50)?: ")
    if order == 'off':
        on = False
    elif order == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"money : {profit}$")
    else:
        drink = menu[order]
        if is_sufficient(drink["ingredients"]):
            payment = coin_calc()
            if is_tran_success(payment, drink["cost"]):
                make_coffee(order , drink["ingredients"])


