import math

family = 4
pizzaslices = 8

p1 = int(input("how many slices of pizza does Dad want? "))
p2 = int(input("how many slices of pizza does Mom want? "))
p3 = int(input("how many slices of pizza does Son want? "))
p4 = int(input("how many slices of pizza does Daughter want? "))


totalslices = int(p1 + p2 + p3 + p4)
print("Total slices ate:", totalslices)

wholepizza = math.ceil(totalslices/pizzaslices)

print("Total pizzas to buy:", wholepizza)

leftover = (wholepizza*pizzaslices) - totalslices

print("Leftover slices:", leftover)
