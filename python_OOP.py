import selfmoudel
print selfmoudel.add(5,8)
print selfmoudel.substract(10,5)
print selfmoudel.multiply(12,6)
'''
Why set those modules as starndard Modules instead of build-in funcitons.abs
why don't we import the whole package instead of a modules from package?
no, it violate the Zen of Python. Explicit is better than implicit.
'''
from my_modules import test_module
test_module.zero(1,2,3)
# inheritance
class Vehicle(object):
    def __init__(self,wheels,capacity,make,model):
        self.wheels=wheels
        self.capacity=capacity
        self.make=make
        self.model=model
        self.mileage=0
    def drive(self, miles):
        self.mileage+=miles
        return self
    def reverse(self,miles):
        self.mileage-=miles
        return self
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels=4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage+=miles
        return self
    def drive(self,miles):
        raise NotImplementedError#this is one way to kill drive method for aiplane. I find it at internet. Not neccessary to do that .
'''
for me, inheritance is like adding new functions and ignore some old funcitons, but are thsoe old function still there?
will it cause problem? Does class Airplane has a drive function?
'''
bird= Airplane(22,853,"Airbus","A380")
print bird.drive(100).mileage 
'''
still there
there is way to delete it. Search it after I finish assignment.
'''

b=Bike(2,1,'schwinn','paramount')
print b.vehicle_type()
'''
I think it causes a __init__ question for me. I know __init__is setting the value of object. Does it change the value to function return a specific data for a object?
vechile_type is function, but it is also a value for Bike. And can we modify __init__ by using inheritance to add a paramiter?
it is not.
'''
c=Car(8,5,'Toyota','Matrix')
c.set_wheels()
'''
if we build a car class, we need run set_wheel()function everythime?
yes. That's the reason we have super. It is easy to change the __init__
'''
# multiple Arguments
def varargs(arg1, *args):
    print 'Got '+arg1+' and '+','.join(args)
varargs('one','two','three')
def varargs1(arg1, *args):
    print 'args is of'+str(type(args))
varargs1('one','two','three')
'''
Cant this be used on array?
'''
def arrplus(arg1, *args):
    arr=[]
    arr.append(arg1)
    arr.append(args)
    print arr
arrplus(1,2,3,4)
'''
it adds 2,3,4 as a turple into array. This way can be only used on turple.
it can be used on the others. It just the args is turple. If we really want to use it on array, we need 
loop the turple.
'''
def arrplus1(arg1, *args):
    arr=[]
    arr.append(arg1)
    for value in args:
        arr.append(value)
    print arr
arrplus1(1,2,3,4)
# supper try to add a parameter to child class

class Motorcycle(Vehicle):
    def __init__(self,capacity,make,model,color):#parameters of parent class + parementer you gona creat
        super(Motorcycle, self).__init__(2,capacity,make,model)#parameters of parent class
        self.color=color
motorola=Motorcycle(853,'Toyota','Matrix','blue')
print motorola.wheels
'''
super() argument 1 must be type, not classobj if I haven't write parent class '(object)'
if there is some parameter of parent class are not usefull--you need a certain value for them so don't need 
to pass argument---you just change the parament after super and __init__function to a certain number
if you want to remove a parameter which passed from parent class to child class, best way is just write none in 
arugement.

'''