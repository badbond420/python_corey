import datetime
class Robot:
    __counter = 1

    def __init__(self):
        type(self).__counter += 1

    # def RobotInstances(): # possible to use with class but not with inst
    #     return Robot.__counter
    #
    # def RobotInstances(self): # possible to use with inst but not with class
    #     return Robot.__counte


class Pets:
    name = "pet animals"

    @staticmethod
    def about1():
        print("This class is about {}!".format(Pets.name))

    @classmethod
    def about2(cls):
        print("This class is about {}!".format(cls.name))


class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"


class Cats(Pets):
    name = "cats"

# p = Pets()
# print(p.about2())
# d = Dogs()
# print(d.about2())
# c = Cats()
# print(c.about2())

class Emp:
    hike = 1.5
    counter = 0
    def __init__(self,fname,lname, sal):
        self.first_name = fname
        self.last_name = lname
        self.sal =sal
        self.email = fname + "." + lname + "@domain.com"
        type(self).counter += 1

    def get_name(self):
        return self.first_name + " " + self.last_name

    def do_hike(self):
        self.sal *= type(self).hike

    @classmethod
    def raise_hike_percentage(cls,num):
        cls.hike = num
    @classmethod
    def get_obj_from_string(cls,string):
        fname, lname, sal = string.split("-")
        return cls(fname, lname, int(sal))

    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True


hari = Emp("Hari","Mantry",1500)
print(hari.sal)
bibek = Emp.get_obj_from_string("Hari-Mantry-2500")
print(bibek.sal)

my_date = datetime.date(2018,7,18)
print(bibek.is_working_day(my_date))

junk_func = Emp.is_working_day
print(junk_func(my_date))

def addition(a , b):
    return a + b

Emp.addition = addition
print(Emp.addition(9,8))
