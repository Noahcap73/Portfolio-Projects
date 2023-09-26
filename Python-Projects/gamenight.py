gamers = []

#Function to add gamers name and availability to "gamers" list
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else: print("Gamer missing critical information!")

kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}

# adding gamers to "gamers" list
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson',"availability": ["Monday", "Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers',"availability": ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes',"availability": ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams',"availability": ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', "availability": ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan',"availability": ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer',"availability": ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.',"availability": ["Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo',"availability": ["Monday", "Tuesday", "Wednesday"]}, gamers)

#building a daily frequency table
def build_daily_frequency_table():
    return {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
count_availability = build_daily_frequency_table()

#adding values for the frequency table
def calculate_availbility(gamers_list, available_frequency):
    for gamer in gamers_list:
        for days in gamer["availability"]:
            available_frequency[days] += 1

calculate_availbility(gamers, count_availability)
print(count_availability)   #Outputs = {'Monday': 7, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 6, 'Friday': 3, 'Saturday': 4, 'Sunday': 3}

#Finding the night with the most available gamers
def find_best_night(availability_table):
    return max(availability_table, key = availability_table.get)

game_night = find_best_night(count_availability)
print(game_night) #Outputs: Monday

#Returning the gamers who are available on the day from the find_best_night func
def available_on_night(gamers_list, day):
    return [gamer["name"] for gamer in gamers_list if day in gamer["availability"]]
            

attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)     #Outputs: ['Kimberly Warner', 'Thomas Nelson', 'Joyce Sellers', 'Joanne Lynn', 'Latasha Bryan', 'James Barnes Jr.', 'Michel Trujillo']

#formatting an email
form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
The Sorcery Society
"""

#Creating a function to send the formatted email, above, to each gamer who is available
def send_email(gamers_attend, day, game):
    for gamer in gamers_attend:
        print(form_email.format(name = gamer, day_of_week = day, game = game))
send_email(attending_game_night, game_night, "Abruptly Goblins!")

#finding the gamers who is NOT available
def not_available_on_night(gamers_list, day):
    return [gamer["name"] for gamer in gamers_list if day not in gamer["availability"]]

not_attending_game_night = not_available_on_night(gamers, game_night) 
print(not_attending_game_night)#Outputs: ['Michelle Reyes', 'Stephen Adams', 'Crystal Brewer']


#Finding second best night
def find_second_best_night(availability_table):
    availability_table.pop(max(availability_table, key = availability_table.get)) #removes first best night
    return max(availability_table, key = availability_table.get) #gets second best night

second_game_night = find_second_best_night(count_availability)
print(second_game_night) #Outputs : "Thursday"


#Sending an email to players unavailable for the first game night, and telling them the second best night
def send_email(gamers_attend, day, game):
    for gamer in gamers_attend:
        print(form_email.format(name = gamer, day_of_week = day, game = game))
send_email(not_attending_game_night, second_game_night, "Abruptly Goblins!")
