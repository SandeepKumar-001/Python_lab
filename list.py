"""
Create a list of colors with comma seperated color names entered by the user.
Display he first and last colors.
Read another color list and print out all colors from list 1 that are not in the list 2.
create another list from color list 1 by assigning an integer value for each color.
"""
color=input("ENTER COLORS SEPERATED BY COMAS:")
color_list1=color.split(',')
print(color_list1)

print("FIRST COLOR:", color_list1[0])
print("LAST COLOR:", color_list1[-1])

color_list2 = ["Red", "Orange", "Black", "White"]
print("color-list1 not contained in color-list2 are : ")

diff=list(set(color_list1)- set(color_list2))
print(diff)
color_int_list=[]

for color in color_list1:
 color_int_list.append(len(color))
print(f"List of integers corresponding to each color: {color_int_list}")