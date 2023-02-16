# Fisal Ikhmayes


# Sample function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print("The Grinch Stole Christmas Game")
    print("Collect 6 items to win the game, or be eaten by the grinch.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


def main():
    show_instructions()
    rooms = {
        'Main living room': {'South': 'Bedroom', 'North': 'Kitchen', 'East': 'Family room', 'West': 'Garden', 'Item' : None},
        'Bedroom': {'North': 'Main living room', 'East': 'Bathroom', 'Item': 'Helmet'},
        'Bathroom': {'West': 'Bedroom', 'Item': 'Armor'},
        'Garden': {'East': 'Main living room', 'Item': 'Garlic powder'},
        'Kitchen': {'South': 'Main living room', 'East': 'Garage', 'Item': 'Lamb chops'},
        'Garage': {'West': 'Kitchen', 'Item': 'Long crescent wrench'},
        'Family room': {'West': 'Main living room', 'North': 'Basement', 'Item': 'Rope'},
        'Basement': {'South': 'Family room', 'Item': 'The Grinch'},  # villian
    }

    # Starting room
    current_room = 'Main living room'
    # List to store collected items
    inventory = []

    # Loop to simulate moves between rooms based on the user input
    while True:
        # If current_room is Dining Room then breaking the loop
        if current_room == 'Basement':
            print("\nYou are in the", current_room)
            print("You see a Grinch and have not collected all the items!", )
            if len(inventory) == 6:
                print("\nCongrats! You have all items and defeated The Grinch!")
            else:
                print("\nNOM NOM...GAME OVER!")
            break

        # Printing current_room
        print("\nYou are in the", current_room)

        # Taking user opinion to pick the item or not
        if rooms[current_room]['Item'] != None:
            print("You see a", rooms[current_room]['Item'])
            opinion = input("get " + rooms[current_room]['Item'] + "?(Y/N): ").upper()
            # Validating user input
            while opinion not in ['Y', 'N']:
                print("Invalid input. Try again")
                opinion = input("Get " + rooms[current_room]['Item'] + "?(Y/N): ").upper()
            if opinion == 'Y':
                inventory.append(rooms[current_room]['Item'])
                rooms[current_room]['Item'] = None
        else:
            print("Already item collected or nothing in this room")

        # Printing inventory
        print("Inventory:", inventory)

        # Taking user input for direction to move
        direction = input("Direction to move?(East,West,North,South): ").title()
        directions = list(rooms[current_room].keys())

        # Validating direction
        while direction not in directions:
            print("Invalid direction from " + current_room + ". Try again")
            direction = input("Direction to move?(East,West,North,South): ").title()

        # Setting next_room
        next_room = rooms[current_room][direction]
        print("You have just moved to", next_room)
        print("------------------------------------------------")

        # Updating current_room
        current_room = next_room

    # Printing end message
    print("\nThanks for playing the game. Hope you enjoyed it.")


# Calling main function
main()
