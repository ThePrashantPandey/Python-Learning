class Person :
    def __init__(myobject , name , age):
        myobject.name = name
        myobject.age = age
    def myfun(myobject):
        print("Hello my name is " ,  myobject.name , myobject.age)
class go(Person):
    pass
p =go("ho" , "vo")
p.myfun()