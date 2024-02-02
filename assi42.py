class Person :
    def __init__(myobject , name , age):
        myobject.name = name
        myobject.age = age
    def myfun(myobject):
        print("Hello my name is " ,  myobject.name , myobject.age)
class go(Person):
    def welcome(myobject):
        print("welcome" , myobject.name, "to my class")
p =go("ho" , "vo")
p.welcome()