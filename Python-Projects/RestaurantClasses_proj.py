import datetime as date
#Creating a Business Class
class Business:
    def __init__(self, name, franchises): #Creating a constructor for Business
        self.name = name
        self.franchises = franchises

#Creating a Franchise Class
class Franchise:
    def __init__(self, address, menus):  #Creating a constructor for Franchise
        self.address = address
        self.menus = menus
    def __repr__(self):
        return f"This restaurant is located at {self.address}" #Representing where the restaurant is located
  
    def available_menus(self, time = date.time()): #Creating a method specify which menus are available at a given time
        available_menus = []
        if time <= date.time(10, 59) or time >= date.time(23):
            return f"The restaraunt located at {self.address} is closed!"
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
              available_menus.append(menu)
        return available_menus
  
            

#Creating a Menu Class
class Menu:
    def __init__(self, name, items, start_time = date.time(), end_time = date.time()):  #Creating a constructor for Menu
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return f"Menu: {self.name} \nAvailability: {self.start_time} - {self.end_time}" #Representing the Menu name and availability
    
    def calculate_bill(self, purchased_items):    #Creating a method to calculate the bill of purchased items
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return "Your total is: $"+ str(bill)
    

#Items in Brunch Menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 
  'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

#Creating Brunch Menu
brunch = Menu("Brunch", brunch_items, date.time(11), date.time(16))

#Items in Early Bird Menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
#Creating Early Bird Menu
early_bird = Menu("Early Bird", early_bird_items, date.time(15), date.time(18))

#Items in Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
#Creating Dinner Menu
dinner = Menu("Dinner", dinner_items, date.time(17), date.time(23))

#Items in Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
#Creating Kids Menu
kids = Menu("Kids", kids_items, date.time(11), date.time(21))

#Items in Arepas Menu
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas = Menu("Arepas", arepas_items, date.time(10), date.time(20))
 
all_menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas)

print(new_installment.available_menus(date.time(17))) #Outputs: [Menu: Early Bird Availability: 15:00:00 - 18:00:00, 
                                                                #Menu: Dinner Availability: 17:00:00 - 23:00:00, 
                                                                #Menu: Kids Availability: 11:00:00 - 21:00:00]

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
second_business = Business("Take a' Arepa", arepas_place)

print(second_business.franchises) #Outputs: "This restaurant is located at 189 Fitzgerald Avenue"
