from django.db import models

# Create your models here.

class Persona: #Defino una clase Persona SIN HEREDAR DE MODELS ya que sino esta al migrar los modelos generaria un tabla en la base de datos
    nombre = models.CharField(max_length=30) #Con campos que después van a ser heredados por las clases hijas
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()

class Profes_Tutores(models.Model, Persona): #Genero la clase hija y heredo de Models para que al importarlos se agreguen como tabla a la base de datos 
    pass                                     #y Persona, por lo que esta tiene los mismos campos que le definimos a Persona