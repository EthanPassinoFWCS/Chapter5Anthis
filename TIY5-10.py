current_users = ["Greg", "Jake", "John", "Paul", "Hallie"]

new_users = ["john", "Jake", "Amy", "Vince", "Ethan"]

for user in new_users:
  lowerlist = [cuser.lower() for cuser in current_users]
  if(user.lower() in lowerlist): print("You will need to enter a new username because the one you chose was taken.")
  else: print("Username available.")
