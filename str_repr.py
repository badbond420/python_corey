class Emp:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
        self.email = fname + "." + lname + "@domain.com"

    def get_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_name()

    def __repr__(self):
        return 'Emp("{}","{}")'.format(self.first_name,self.last_name)
        # return "lol" # doesnt work


hari = Emp("Hari","mantry")
print(hari.__str__())
print(hari.__repr__())
repr_obj = hari.__repr__()
print(eval(repr_obj).first_name)
