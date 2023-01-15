import re

height = input("enter property hight in feet and inches (example : 1'2(1 feet 2 inches):")
h = re.split(r'[\'\"]',height)
width = input("enter property width in feet and inches (example : 1'2(1 feet 2 inches):")
w=re.split(r'[\'\"]',width)

h_inches=int(h[0])*12+int(h[1])
w_inches=int(w[0])*12+int(w[1])

if int(w[1]) < 12 and int(h[1]) < 12:
    sq_in=h_inches*w_inches    
    sq_feet=sq_in/144
    sq_feet_inches = sq_feet%1*12


    

print("the total area is {} square feet and {} inches:".format((int(sq_feet)),int(sq_feet_inches)))