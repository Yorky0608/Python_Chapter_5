car = 'bmw'
car == 'bmw'
car = 'audi'
car == 'bmw'
car = 'Audi'
car == 'audi'
car = 'Audi'
car.lower() == 'audi'
car = 'Audi'
car.lower() == 'audi'
car
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
age = 18
age == 18
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
age = 19
age < 21
age <= 21
age > 21
age >= 21
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
age_1 = 22
age_0 >= 21 and age_1 >= 21
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
age_0 = 18
age_0 >= 21 or age_1 >= 21
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
game_active = True
can_edit = False