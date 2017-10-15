def isPrime (numb):	
	check = true
	start = 2
	if numb < 1:
		print ("It's not a Prime number")
	else:
		if numb == 1 or numb ==2:
			print("It's a Prime Number")
		else:
			while start < num:
				if numb % start == 0 :
					check = false
			                break
				start = start + 1
			if check = true:
				print ("it's a Prime Number")
			else:
				Print ("it's not a Prime Number")
