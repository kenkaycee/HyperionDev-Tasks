# get user inputs 
city_flight = input("Select destination city [London, Paris, Rome, Texas]: ").lower()
while city_flight.capitalize() not in ["London", "Paris", "Rome", "Texas"]: # ensures city entered is among the available cities
    print("Please choose from these cities [London, Paris, Rome, Texas] only!")
    city_flight = input("Select destination city [London, Paris, Rome, Texas]: ").lower()


num_nights = int(input("Enter number of nights you will stay in a hotel: "))
rental_days = int(input("Enter number of days you will hire a car: "))

# functions 
# function that calcuates total cost of hotel stay given a fixed price
def hotel_cost(num_of_night):
    # price per night at the hotel
    pricePerNight = 200
    return pricePerNight * num_of_night

# function that calculates the cost of flight based on the city a passenger is flying to
def plane_cost(city):
    if(city == "london"):
        flight_cost = 100 
    elif(city == "paris"):
        flight_cost = 50
    elif(city == "rome"):
        flight_cost = 55
    elif(city == "texas"):
        flight_cost = 400
    return flight_cost 

# function that accepts rental days and calculates total cost of car rental 
def car_rental(num_days):
    car_cost = 100 # daily cost of renting a car
    return num_days * car_cost

# function that calculates the total cost for a holiday - takes three arguments: 
    # number of nights, destination city and number of days renting a car

def holiday_cost(num_of_night, city, num_days):
    cost_a = hotel_cost(num_of_night) # calls hotel_cost function
    cost_b = plane_cost(city) # calls plane_cost function
    cost_c = car_rental(num_days) # calls car_rental function
    return cost_a + cost_b + cost_c # total cost of holiday

# 5. Print out all the details about the holiday in a way that is easy to read.
print() # empty line 
print("*****HOLIDAY PACKAGE*****")
print(f"You are flying to: {city_flight.capitalize()}")
print(f"The cost of your flight is: £{plane_cost(city_flight)}\n")
print(f"The number of days you plan to stay in a hotel: {num_nights}")
print(f"The total cost of your hotel stay is: £{hotel_cost(num_nights)}\n")
print(f"The number of days you want to a hire a car: {rental_days}")
print(f"The total cost of hiring a car is: £{car_rental(rental_days)}\n")
total_holiday_cost = holiday_cost(num_nights, city_flight, rental_days)
print(f"The total cost of your holiday is: £{total_holiday_cost}")