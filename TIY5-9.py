users = []

if(users):

  for user in users:
    if(user == "admin"): print("Hello admin, would you like to see a status report?")
    else:
      print(f"Greetings, {user}!")

else: print("There are no users.")