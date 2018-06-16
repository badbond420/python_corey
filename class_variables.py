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

hari = Emp("Hari","Mantry",1500)
print(hari.sal)
hari.do_hike()
print(hari.sal)
print(Emp.counter)

bibek = Emp("Bibek","Mantry",1500)
print(hari.sal)
print(Emp.counter)