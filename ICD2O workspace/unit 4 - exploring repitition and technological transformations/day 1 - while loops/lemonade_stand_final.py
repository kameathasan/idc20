import random
import os
import time
 
assets = 200
day = 1
lemonade_cost = 2
total_profit = 0
daily_profit = 0
people_outside = 0
 
def print_lemonade_stand_intro():
    population = get_town_population()
    print(f"Welcome to Lemonade Stand! You are in a town with a population of {population} people.")
    print(f"The goal of the game is to make money by selling lemonade. ")
    print(f"Your current assets are ${assets/100} and the cost of lemonade is ${lemonade_cost/100}.")
    continue_game = input("Would you like to continue? ")
    if continue_game.lower() == "no":
        end_game()
 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
 
def get_weather():
    weather_conditions = ["sunny", "cloudy", "rainy"]
    probabilities = {"sunny": 0.6, "cloudy": 0.3, "rainy": 0.1}
    return random.choices(weather_conditions, weights=probabilities.values())[0]
 
def execute_game():
    print_lemonade_stand_intro()
   
    while True:
        keep_playing = execute_one_round_of_game()
        if not keep_playing:
            break
 
    end_game()
 
def execute_one_round_of_game():
    global day, assets, total_profit, daily_profit, lemonade_cost, glasses_made, num_of_signs, people_outside, weather, charge_per_glass, customers_at_stand
    cls()
    weather = get_weather()
    if day%4 == 0:
        lemonade_cost = lemonade_cost + 2
    print()
    print(f"Day {day}: Today, it is {weather}!")
    print(f"The cost of lemonade is ${lemonade_cost/100} and you have ${assets/100}.")
    print()
 
    glasses_made, num_of_signs, charge_per_glass =  get_player_input()
 
    customers_at_stand = get_customers_at_stand()
 
    glasses_sold = get_glasses_sold()
    income = round(glasses_sold * charge_per_glass, 2)
    expenses = round(15 * num_of_signs + lemonade_cost * glasses_made, 2)
    daily_profit = round(income - expenses, 2)
    assets = round(assets + daily_profit, 2)
    total_profit += daily_profit
 
    print()
    print(f"Day {day}")
    print(f"{glasses_sold} glasses sold")
    print(f"${charge_per_glass / 100} per glass")
    print(f"{glasses_made} glasses made")
    print(f"{num_of_signs} signs made")
    print()
    print(f"Income: ${income / 100}")
    print(f"Expenses: ${expenses / 100}")
    print()
    print("Calculating profit...")
    time.sleep(1)
    print(f"Today's Profit: ${daily_profit / 100}")
    print(f"Total Profit: ${total_profit / 100}")
    print(f"Assets: ${assets / 100}")
 
    day += 1
    keep_playing = input("Would you like to keep playing? ")
    return keep_playing.lower() != "no"
 
def get_town_population():
    return random.randint(100, 800)
 
# Get the people outside on that day based on the weather
def get_people_outside():
        population = get_town_population()
        weather = get_weather()
        if weather == "sunny":
            people_outside = round(random.uniform(population*0.4, population*0.7))
        elif weather == "rainy":
            people_outside = round(random.uniform(population*0.06, population*0.2))
 
        elif weather == "cloudy":
            people_outside = round(random.uniform(population*0.2, population*0.4))
        return people_outside
 
def end_game():
    print("See you next time!")
    exit()

def get_glasses_made(glasses_made):
    glasses_made = int(input("How many glasses of lemonade would you like to make? "))
    while glasses_made * lemonade_cost > assets:
        print("You don't have enough money for this. ")
        glasses_made = int(input("How many glasses of lemonade would you like to make? "))
   
    return glasses_made
 
def get_num_of_signs():
    num_of_signs = int(input("How many advertising signs are you using (15 cents each)? "))
    while num_of_signs * 15 > assets - (glasses_made * lemonade_cost):
        print("You don't have enough money for this. ")
        num_of_signs = int(input("How many advertising signs are you using (15 cents each)? "))
   
    return num_of_signs

 
def get_charge_per_glass():
    return int(input("How much would you like to charge for each glass of lemonade (cents)? "))
 
def get_player_input():
    glasses_made = get_glasses_made()
    num_of_signs = get_num_of_signs()
    charge_per_glass = get_charge_per_glass()
    return glasses_made, num_of_signs, charge_per_glass
 
# Calculate the customers at your stand based on the advertising signs
def calculate_customers_based_on_advertising(num_of_signs):
        people_outside = get_people_outside()
        customers_based_on_advertising = num_of_signs * (people_outside * 0.2)
        if customers_based_on_advertising > people_outside:
            customers_based_on_advertising = people_outside
        return customers_based_on_advertising
 
# Calculates the number of customers who see the stand without advertising
def get_customers_who_see_stand():
    return random.randint(5, 25)
 
# Calculates the number of customers at the stand
def get_customers_at_stand(customers_based_on_advertising):
        customers_based_on_advertising = calculate_customers_based_on_advertising()
        customers_who_see_stand = get_customers_who_see_stand()
        if customers_based_on_advertising + customers_who_see_stand > people_outside:
            return people_outside
        else:
            return customers_based_on_advertising + customers_who_see_stand
       
def get_glasses_sold():
    customers_who_buy_lemonade = 0
    if weather == "sunny":
        if charge_per_glass <= 10:
            customers_who_buy_lemonade = customers_at_stand
        elif 10 < charge_per_glass < 20:
            customers_who_buy_lemonade = round(customers_at_stand * 0.9)
        elif 20 <= charge_per_glass <= 30:
            customers_who_buy_lemonade = round(customers_at_stand * 0.6)
        elif 30 < charge_per_glass < 40:
            customers_who_buy_lemonade = round(customers_at_stand * 0.1)
    elif weather == "rainy":
        if charge_per_glass <= 10:
            customers_who_buy_lemonade = round(customers_at_stand * 0.5)
        elif 10 < charge_per_glass < 20:
            customers_who_buy_lemonade = round(customers_at_stand * 0.1)
    else:  # cloudy
        if charge_per_glass <= 10:
            customers_who_buy_lemonade = round(customers_at_stand * 0.7)
        elif 10 < charge_per_glass < 20:
            customers_who_buy_lemonade = round(customers_at_stand * 0.4)
        elif 20 <= charge_per_glass <= 30:
            customers_who_buy_lemonade = round(customers_at_stand * 0.2)
 
    return min(customers_who_buy_lemonade, glasses_made)
 
execute_game()