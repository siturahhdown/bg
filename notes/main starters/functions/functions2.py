def greet_user(name, surname): # def is a keyword that tells python we are defining a function   also inside brackets are parameters that are passed to the function
    print(f"Hi there! {name} {surname}")
    print("How is your day going?")

def calc_cost(total, shipping, discount): # def is a keyword that tells python we are defining a function   also inside brackets are parameters that are passed to the function
    print(f"Total: {total}")
    print(f"Shipping: {shipping}")
    print(f"Discount: {discount}")
    print(f"Total cost: {total + shipping - total * discount}")
    
print("Start")
greet_user(name="Titas", surname="smith") # calling the function   #allows us to show what position the parameters are in
calc_cost(total=50, shipping=5, discount=0.1) #improves readability (the total,shipping and so on)
print("Finish")
# allows us to reuse code