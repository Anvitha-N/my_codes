# Python program to print positive Numbers in a List 

# list of numbers 
list1 = [10, 21, -7, -75, 38, -66, -56, 93] 
num = 0

# using while loop	 
while(num < len(list1)): 
	
	# checking condition 
	if list1[num] >= 0: 
		print(list1[num], end = " ") 
	
	# increment num 
	num += 1
	
