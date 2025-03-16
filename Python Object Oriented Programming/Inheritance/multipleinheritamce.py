# multiple inheritance = inherit from more than one parent class
#                        C(A,B)
# multilevel inheritance = inheriting from more than one parent class
#                        C(B) <- B(A) <- A
class Animal:
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = fish("Neon")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
rabbit.eat()
hawk.eat()
fish.eat()
rabbit.sleep()
hawk.sleep()
fish.sleep()