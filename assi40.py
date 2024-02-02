class Person :
    def __init__(myobject , name , age):
        myobject.name = name
        myobject.age = age
    def myfun(myobject):
        print("Hello my age is " ,  myobject.name , myobject.age)
p1 = Person ("jone" , 21)
p1.age = 20
p1.name = "heena"
p1.myfun()