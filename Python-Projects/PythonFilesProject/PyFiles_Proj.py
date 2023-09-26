"""
Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create 
data in your quest for justice. Work with CSV files and other text files in this exploration of the 
strength of Python file programming.
"""

import csv

#creating an empty list of users who have been hacked
compromised_users = []

#getting a list of the usernames from "Password.csv" & appending it to the "compromised_users" list
with open("Password.csv") as password_file:
    password_csv = csv.DictReader(password_file)
    for row in password_csv:
        password_row = row
        compromised_users.append(row["Username"])

#adding the users of compromised users to a file
with open("compromised_users.txt", "w") as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user)

import json

#Using json to send a message
with open("boss_message.json", "w") as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)

#replacing a csv with the hackers signature
with open("new_passwords.csv", "w") as new_passwords_obj:
    slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
    new_passwords_obj.write(slash_null_sig)

with open("new_passwords.csv") as new_pass:
    print(new_pass.read())

