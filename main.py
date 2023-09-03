print("Welcome to the GC fruit market!")
name = input("What is your name? ")

print("Welcome " + name + "!")

appleOrder = 0
grapeOrder = 0
orangeOrder = 0

while True:
    fruit_options = ["Apple", "Grape", "Orange"]
    fruit_price = [2, 1, 3]
    print(f"1). {fruit_options[0]} ${fruit_price[0]}")
    print(f"2). {fruit_options[1]} ${fruit_price[1]}")
    print(f"3). {fruit_options[2]} ${fruit_price[2]}")

    fruit_choice = input("Which fruit would you like to buy? ")


    if fruit_choice == "1":
        print(f"You bought an {fruit_options[0]} at ${fruit_price[0]}")
        appleOrder += 1
    elif fruit_choice == "2":
        print(f"You bought an {fruit_options[1]} at ${fruit_price[1]}")
        grapeOrder += 1
    elif fruit_choice == "3":
        print(f"You bought an {fruit_options[2]} at ${fruit_price[2]}")
        orangeOrder += 1


    buy_more = input("Would you like to buy another piece of fruit? y/n ")
    if buy_more =="y":
        continue
    elif buy_more =="n":
        print("Receipt for " + name + ":")
        print(f"{appleOrder} {fruit_options[0]}(s) at ${fruit_price[0]} a piece")
        print(f"{grapeOrder} {fruit_options[1]}(s) at ${fruit_price[1]} a piece")
        print(f"{orangeOrder} {fruit_options[2]}(s) at ${fruit_price[2]} a piece")
        break
    else:
        print("Enter either y/n")

appleTotal = appleOrder * fruit_price[0]
grapeTotal = grapeOrder * fruit_price[1]
orangeTotal = orangeOrder * fruit_price[2]

subtotal = appleTotal + grapeTotal + orangeTotal
tax = subtotal * 0.05
total = subtotal + tax

print(f"Subtotal: ${subtotal}")
print(f"Tax(5%): ${tax}")
print(f"Total: ${total}")
