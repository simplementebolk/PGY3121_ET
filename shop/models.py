from django.db import models

class RankedAccount(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='ranked_accounts/', null=True, blank=True)
    available = models.BooleanField(default=True)
    rank = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    account = models.ForeignKey('RankedAccount', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    session_key = models.CharField(max_length=40)  # Para almacenar la sesión del usuario anónimo

    def subtotal(self):
        return self.account.price * self.quantity
    
class ContactForm(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)
    profesion = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    ocupacion = models.CharField(max_length=100)
    puesto_empresa = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre