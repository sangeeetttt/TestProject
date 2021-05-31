'''
 N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the questions above.
'''
K = int(input("write the no of apples: "))
N = int(input("write the no of students: "))

eachgets = (K//N)
remaining = (K%N)
print(f"no of apples each student gets: {eachgets}")
print(f"no of apples remaining in the basket: {remaining}")