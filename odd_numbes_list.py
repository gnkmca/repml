a = [1, 5, 3, 2, 54, 221, 34, 82, 11, 92, 100]
b=[]
element = 0
for element in a:
	if element%2 != 0 :
            print("element: ", element)	
	    b.append(element)
print ("Given List:", a)
print ("Odd Numbers in the List",b)
