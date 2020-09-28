import random

lotus = ['Red', 'Blue', 'Pink']
lotus_flavors = ['Cherry', 'Raspberry', 'Blueberry', 'Banana', 'Blackberry',
            'Blackcherry', 'Pineapple', 'Green Apple', 'Dragonfruit',
            'Strawberry', 'Watermelon', 'Lemon', 'lime', 'Kiwi',
            'Mango', 'Blueraspberry', 'Pomegranate', 'Peach', 'Orange']
coffee = ['White Coffee', 'Dark Roast', 'Light Roast', 'Expresso']
coffee_drinks = ['Carmal', 'Chocolate', 'vinilla',]
quit = False

print("Don't know what drink to get? Try this drink randomnizer!")


while quit == False:
    drink = input("What drink do you want? ")

    if drink.upper() == 'LOTUS':
        print(random.choice(list(lotus)), random.choice(list(lotus_flavors)))
    elif drink.upper() == 'COFFEE':
        print(random.choice(list(coffee)), random.choice(list(coffee_drinks)))
    elif drink == 'quit':
        print("Enjoy whatever drink you choose next!g")
        quit = True
        break
    else:
        print("""That drink doesn't appear on the menu, try lotus or
coffee.""")
