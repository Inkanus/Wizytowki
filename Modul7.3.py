from faker import Faker
fake = Faker("pl_PL")

class BusinessContact:
    def __init__(self, first_name, last_name, company, occupation, email_address,tel_work):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.occupation = occupation
        self.email_address = email_address
        self.tel_work = tel_work
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}, {self.occupation}, {self.company}"

    def __repr__(self):
        return f"Card(first_name={self.first_name} last_name={self.last_name}, adres email={self.email_address})"

    def contact(self):
        return f"Wybieram numer domowy: {self.tel_work} i dzwonię do {self.first_name} {self.last_name} "
    
    def privcontact(self):
        return f"Wybieram numer służbowy: {self.tel_priv} i dzownię do {self.first_name} {self.last_name}"
    #Zliczanie znaków
    @property
    def label_lenght(self):
        return sum([len(self.first_name), len(self.last_name),])
    

class BaseContact(BusinessContact):
    def __init__(self, tel_priv, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_priv = tel_priv


human_1 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(human_1)
print(human_1.contact())
print(human_1.privcontact())
print(human_1.label_lenght)
print()


human_2 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(human_2)
print(human_2.contact())
print(human_2.privcontact())
print(human_2.label_lenght)
print()


human_3 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(human_3)
print(human_3.contact())
print(human_3.privcontact())
print(human_3.label_lenght)
print()


human_4 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(human_4)
print(human_4.contact())
print(human_4.privcontact())
print(human_4.label_lenght)
print()


human_5 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(human_5)
print(human_5.contact())
print(human_5.privcontact())
print(human_5.label_lenght)
print()

