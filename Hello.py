import os

name = input("Please enter your first name ")

if name!="Frank":
	print("Hello ", name, " this program was not made for you")
else:
	print("Hello ", name," are you impressed with my Python Skills?")
	answer = input("Answer Yes or No ")
	if answer== "Yes":
		print("You don't need much to be impressed")
	elif answer=="No":
		print("You are such a party pooper!")
	else:
		print("I asked you to say Yes or No. You're clearly too dumb to be Frank, you must have lied!")

os.system("pause")