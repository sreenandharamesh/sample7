import random
x="D"
while x == "D":
	no = random.randint(1,6)
	if no == 1:
		print("|-----|")
		print("|     |")
		print("|  *  |")
		print("|     |")
		print("|-----|")
		print("\n")
	if no == 2:
		print("|-----|")
		print("|  *  |")
		print("|     |")
		print("|  *  |")
		print("|-----|")
		print("\n")
	if no == 3:
		print("|-----|")
		print("|     |")
		print("|* * *|")
		print("|     |")
		print("|-----|")
		print("\n")
	if no == 4:
		print("|-----|")
		print("|*   *|")
		print("|     |")
		print("|*   *|")
		print("|-----|")
		print("\n")
	if no == 5:
		print("|-----|")
		print("|*   *|")
		print("|  *  |")
		print("|*   *|")
		print("|-----|")
		print("\n")
	if no == 6:
		print("|-----|")
		print("|* * *|")
		print("|     |")
		print("|* * *|")
		print("|-----|")
		print("\n")
		
	x=input("Press 'D' to roll again and 'X' to exit:  ")
	print("\n")
