class Emp:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
        self.email = fname + "." + lname + "@domain.com"
        self.full_name = self.get_name()

    def get_name(self):
        return self.first_name + " " + self.last_name
class Developer(Emp):
    def __init__(self,fname,lname,language):
        self.lang=language
        super().__init__(fname,lname)

class Manager(Emp):
    def __init__(self,fname,lname,employees=None):
        super().__init__(fname,lname)
        if  not employees:
            self.employees = []
        else:
            self.employees = employees

    def add_employees(self,employee):
        self.employees.append(employee)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.full_name)


dev_1 = Developer('Corey', 'Schafer',  'Python')
dev_2 = Developer('Test', 'Employee',  'Java')

mgr_1 = Manager('Sue', 'Smith',  [dev_1])

print(mgr_1.email)

mgr_1.add_employees(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()