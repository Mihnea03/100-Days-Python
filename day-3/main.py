def main():
    print("Welcome to Treasure Island!\nYour mission is to find the treasure.\n\n")

    road = str(input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")).lower()

    if road == "right":
        print("The right road is full of snakes. Game over!")
        return

    print("You chose the left road and you arrive to a lake.")

    swim = str(input("Do you want to wait for a boat to arrive or swim across the lake? Type \"wait\" or \"swim\"\n")).lower()

    if swim == "swim":
        print("You failed! Game over!")
        return
    
    door = str(input("You arrive at the island unharmed. There are 3 doors and you need to choose one. Type \"red\" for the red door, \"yellow\" for the yellow door and \"blue\" for the blue door.\n")).lower()

    if door == "red" or door == "blue":
        print("The door leads you to a room on fire. Game Over!")
        return
    
    print("You found the treasure. Good Job!")
    

if __name__ == '__main__':
    main()