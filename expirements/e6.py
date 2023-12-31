file = open("../files/members.txt", "r")
members = file.readlines()
file.close()

user_input = input("Add a nuw member: ") + "\n"

file = open("../files/members.txt", "w")
members.append(user_input)
file.writelines(members)
file.close()
