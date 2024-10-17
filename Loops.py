# Initialize the number of muffins and cupcakes
muffins = 10
cupcakes = 10

while True:
    # Take input from the user
    purchase = input("Enter your purchase (muffin/cupcake) or '0' to finish: ").strip().lower()
    
    if purchase == "0":
        break  # Exit the loop if user inputs "0"
    
    if purchase == "muffin":
        if muffins > 0:
            muffins -= 1
            print("Muffin purchased!")
        else:
            print("Out of stock")
    
    elif purchase == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
            print("Cupcake purchased!")
        else:
            print("Out of stock")
    
    else:
        print("Invalid input. Please enter 'muffin', 'cupcake', or '0'.")

# Print remaining muffins and cupcakes
print(f"muffins: {muffins} cupcakes: {cupcakes}")
