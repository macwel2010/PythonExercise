row = float(input("enter the length of row in feet :"))
space_post = float(
    input("enter the amount of space used by end post assembly in feet :")
)
space_vine = float(input("enter the space between vines in feet :"))
no_gapevines = (row - 2 * space_post) / space_vine
print(f"the number of grapewines that will fit in the row is {no_gapevines}")
