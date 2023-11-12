class PATIENT(object):
    '''

    Medical centre patient

    '''

    status = 'patient'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []

    def get_details(self):
        print(f'Patient Record {self.name}, {
              self.age} years.  Current information {self.conditions}.')

    def add_info(self, information):
        self.conditions.append(information)


class INFANT(PATIENT):
    def __init__(self, name, age):
        self.vaccinations = []
        super().__init__(name, age)

    def add_vac(self, vaccine):
        self.vaccinations.append(vaccine)

    def get_details(self):
        print(f'Patient Record {self.name}, {self.age} years.')
        print(f'Patient had {self.vaccinations} vaccines.')
        print(f'\n{self.name} is an infant and has had all checks.')
