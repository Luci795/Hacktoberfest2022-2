# Python program to check leap year or not
def checkYear(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

# Driver Code
year = 2000
if(checkYear(year)):
	print("Leap Year")
else:
	print("Not a Leap Year")
	
# This code is contributed by Chinmoy Lenka
