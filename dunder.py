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
        return 'Employee({},{})'.format(self.first_name,self.last_name)

    def __add__(self, other):
        return self.first_name + other.first_name

hari = Emp("Hari","mantry")
bibek = Emp("Bibek","mantry")
print(hari + bibek)
print(Emp.__add__(hari,bibek))