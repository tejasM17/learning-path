#  Inheritance

# Definition: Inheritance allows a class to inherit attributes and methods from another class, facilitating reuse.


class user:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in")

class admin(user):
    def delete_user(self):
        print(f"{self.username} deleted user")

a = admin("tejas")
print(a.username)
a.login()
a.delete_user()






# Real-World Example: Consider human families. Characteristics like surname, traditions, or physical features can be passed down from parents to children.

class family:
    def __init__(self, surname):
        self.surname = surname

class child(family): # single inheritance
# class child(family,family): # multiple inheritance
# class grandchild(child,family): # multilevel inheritance  
# class grandchild(family): # hierarchical inheritance  
    def __init__(self, surname,name):
        super().__init__(surname)
        self.name = name

c = child("oom","tejas")

print(c.name)
print(c.surname)



#     POLYMORPHISUM [many forms]

#  definition: onde class inda inherit madiddru diffrent class ge diffrent behaviour kododunna polymorphisum antare.

class animal:
    def sound(self):
        print("animal make sounds")

class dog(animal):
    def sound(self):
        print("bow, bow..")
class cat(animal):
    def sound(self):
        print("meow, meow..")

animal = [dog(),cat()]
for anim in animal:
    anim.sound()

# d = dog()   
# c = cat()

# d.sound()
# c.sound()

# relating computer science

class notification:
    def send(self):
        print("notification sent")

class email(notification):
    def send(self):
        print("email sent")

class sms(notification):
    def send(self):
        print("sms sent")