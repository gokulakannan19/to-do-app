
file = open("file.txt", 'w')
temperatures = [str(i) + "\n" for i in [10, 12, 14]]
file.writelines(temperatures)