class emp:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
        self.email = fname + "." + lname + "@domain.com"

    def get_name(self):
        return self.first_name + " " + self.last_name

hari = emp("Hari", "Mantry")
print(hari.get_name())
print(hari.__dict__)