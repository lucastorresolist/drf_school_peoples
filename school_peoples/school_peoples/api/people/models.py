from django.db import models


class Materials(models.Model):
    name = models.CharField(max_length=25, null=False)


class Address(models.Model):
    address = models.CharField(max_length=100, null=False)
    cep = models.CharField(max_length=5, null=False)
    number = models.IntegerField(null=False)
    complement = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'Address: {self.address}, Cep: {self.cep}, Number: {self.number}, Complement: {self.complement}'


class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)    


class ClassRoom(models.Model):
    number_room = models.IntegerField(null=False)
    floor = models.IntegerField(null=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return f'Number Room: {self.number_room}, Floor: {self.floor},\
                 Description: {self.description}'

class People(models.Model):
    full_name = models.CharField(max_length=50, null=False)
    cpf = models.CharField(max_length=20, null=False)
    fk_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return f'Name: {self.full_name}, Course: {self.cpf},\
                 Addess: {self.fk_address}'


class Alumn(People):
    course = models.CharField(max_length=50, null=False)
    period = models.IntegerField(null=False)
    class_room = models.ManyToManyField(ClassRoom)
    
    def __str__(self):
        return f'Name: {self.full_name}, Course: {self.course},\
                 Classroom: {self.class_room}'

class Teacher(People):
    salary = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    specialty = models.ManyToManyField(Materials)
