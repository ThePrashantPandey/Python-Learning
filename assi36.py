def totalCtC(z):
    print("total employe income :" ,z)
    b = (z/100)*10
    print("PF deduction :" , b)
    c = (z/100)*5
    print("ESI deduction" , c)
    d = (z/100)*5
    print("CTC deduction" , d)
    e = z - (b+c+d)
    print("total income after deduction" , e)
while True:
    a = eval(input("enter the empolye income :"))
    totalCtC(a)


    

    



