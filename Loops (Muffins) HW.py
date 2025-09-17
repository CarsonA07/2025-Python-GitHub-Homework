muffins = 2
cupcakes = 2

buying = input("Do you want a muffin or a cupcake? Enter 0 to exit. ")

while buying != "0":
    if buying == "muffin" and muffins > 0:
        muffins = muffins - 1
    if muffins == 0:
        print("Muffins are out of stock.")
    if buying == "cupcake" and cupcakes > 0:
        cupcakes = cupcakes - 1
    if cupcakes == 0:
        print("Cupcakes are out of stock.")
    buying = input("Do you want a muffin or a cupcake? Enter 0 to exit. ")


print("Amount of muffins left:", muffins)
print("Amount of cupcakes left:", cupcakes)
