import random
import Recipe_db
print('Welcome to the Meal Plan Generator \n\n')

recipes_needed = int(input("For how many nights this week do you need a dinner recipe?\n"))

for i in range(0,recipes_needed):
    print(Recipe_db.Recipes[random.randint(0, 6)].get('name'))