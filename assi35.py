def stock():
    x = 100 
    print("total bikes is", x)
def rate():
    y = 2000
    print("one bike charges is", y)
def bikerate(x):
    print("selection of bike is:",x)
    if x > 100 :
     print("bike are out of stock")
    elif x <= 0 :
      print("invalid selection, please enter a number greater than zero.")
    else:
      a = 2000*x
      print(a)
print("1 stock")
print("2 rate")
print("3 bike rate")
while True:
    choice = input("Enter choice(1/2/3): ")
    if choice == '1':
        stock()
    elif choice == '2':
         rate ()
    elif choice == '3':
        num_bikes=eval(input("How many bikes are there?"))
        bikerate(num_bikes)
    # e= input("Do you want to continue? (yes/no)")
    # if e == "no":
    #     break    


       