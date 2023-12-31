waiting_list = ["john", "ben", "maan"]
waiting_list.sort()

for index, member in enumerate(waiting_list):
    print(f"{index+1} - {member.capitalize()}")