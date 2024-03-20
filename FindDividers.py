

def Dividers(Number):
	
	DividersArray = []
	
	Pivot = 2
	
	for Loop in range(Number):
		ValueLeft = Number % Pivot
		
		if (ValueLeft == 0):
			DividersArray.append(Number // Pivot)
		#if
		Pivot += 1
	#for Loop
	
	return (DividersArray)
	
#def Dividors


def Main():
	
	print("Input a number: ", end="")
	Number = int(input())
	DividersFound = Dividers(Number)
	print("The dividers are: ", DividersFound)
     
#def Main

Main()
