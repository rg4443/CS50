# dict that has all food data
food_data = {
    "apple": "Calories: 130",
    "avocado": "Calories: 50",
    "banana": "Calories: 110",
    "cantaloupe": "Calories: 50",
    "grapefruit": "Calories: 60",
    "grapes": "Calories: 90",
    "honeydew melon": "Calories: 50",
    "kiwifruit": "Calories: 90",
    "lemon": "Calories: 15",
    "lime": "Calories: 20",
    "nectrarine": "Calories: 60",
    "orange": "Calories: 80",
    "peach": "Calories: 60",
    "pear": "Calories: 100",
    "pineapple": "Calories: 50",
    "plums": "Calories: 70",
    "strawberries": "Calories: 50",
    "sweet cherries": "Calories: 100",
    "tangerine": "Calories: 50",
    "watermelon": "Calories: 80"
}


#converts user input to be lowercase then checks to see if it is in dict, if so to print the value of the corrosponding key that user types.
user_input = input("Item: ")
lowered = user_input.lower()
if lowered in food_data:
    print(food_data[lowered])
