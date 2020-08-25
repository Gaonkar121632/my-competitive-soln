# Python code to demonstrate 
# conversion of hex string 
# to binary string 

import math 

# Initialising hex string 
ini_string = input()

# Printing initial string 
# print ("Initial string", ini_string) 

# Code to convert hex to binary 
n = int(ini_string, 16) 
bStr = '' 
while n > 0: 
	bStr = str(n % 2) + bStr 
	n = n >> 1	
res = bStr 

# Print the resultant string 
rest=str(res)
print (rest[len(res)-1]) 
