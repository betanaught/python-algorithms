'''
python code to generate a pine tree of height h
Ex: h = 4, the tree looks like this:

How tall is your tree? 4

   #   (3-1)
  ###  (2-3)
 ##### (1-5)
#######(0-7)
   #   (3-1)
'''

h=eval(input("How tall your the tree? "))
num_spaces = h - 1
num_hashes = 1
stump = (" " * (h - 1)) + "#"

while h !=0:
    for i in range(num_spaces):
        print(" ", end = "")
    for i in range(num_hashes):
        print("#", end = "")
    print()
    num_spaces -= 1
    num_hashes += 2
    h -= 1

print(stump, end = "")

