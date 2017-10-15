nums=input("Enter how many numbers avg you want: ")
count = 0
sum=0
while count < nums:
		read = input ("Enter number: ")
		sum = sum+read
	 	count = count + 1
avg = sum/nums
print ("Average of given numbers is ", avg)

