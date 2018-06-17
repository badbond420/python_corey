class Emp:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname

    @property
    def first_name(self):
        return self.__fname

    @first_name.setter
    def first_name(self,value):
        self.__fname = value


    @property
    def fulname(self):
        self.__full_name =  self.first_name + " " + self.last_name
        return self.__full_name

    @fulname.setter
    def fulname(self,full_name):
        self.first_name, self.last_name = full_name.split()

hari = Emp("Hari","mantry")
bibek = Emp("Bibek","mantry")
print(bibek.first_name)
print(bibek.fulname)
bibek.fulname = "Kalu Mantry"
print(bibek.first_name)
print(bibek.fulname)
bibek.first_name = "dhedu"
print(bibek.first_name)
print(bibek.fulname)



