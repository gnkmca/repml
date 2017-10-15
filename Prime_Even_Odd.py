numb = input ("enter a number: ")
def isPrime(numb):
     check = True
     start = 2
     if numb < 1:
             print ("It's not a Prime number")
     else:
             if numb == 1 or numb ==2:
                     print("It's a Prime Number")
             else:
                     while start < numb:
                             if numb % start == 0 :
                                     check = False
                                     break
                             start = start + 1
                     if check == True:
                             print ("it's a Prime Number")
                     else:
                             print ("it's not a Prime Number")

def evenORodd (numb):
     if numb % 2 == 0 :
             print ("it's an Even Number")
     else :
             print ("it's an Odd Number")

isPrime(numb)
evenORodd(numb) 
