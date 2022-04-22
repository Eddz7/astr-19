#Write a python program that:
#writes out a table of sin(x) vs. x
#x is tabulated between 0 and 2pi with a thousand entries

#import numpy for pi and sin
import numpy as np

def main():
	#define array table of 1000 entries between 0 and 2pi
	table = np.linspace(0, 2*np.pi, 1000)
	#header for the table
	print(f"  {'x':10s} sin(x)")
	#print out each entry and its corresponding sin value
	for i in table:
		print(f"{i:10f} {np.sin(i):10f}")
if __name__ == '__main__':
	main()