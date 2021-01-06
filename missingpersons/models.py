import uuid 
from django.db import models

class Missingperson(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    SEXCHOICES = (
        ('----','----'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    STaTES = (
        ('----','----'),
        ('Abia','Abia'),
        ('Adamawa','Adamawa'),
        ('Akwa Ibom','Akwa Ibom'),
        ('Anambra','Anambra'),
        ('Bauchi', 'Bauchi'),
        ('bayelsa','Bayelsa'),
        ('Benue','Benue'),
        ('Borno','Borno'),
        ('Cross River','Cross River'),
        ('Delta','Delta'),
        ('Ebonyi','Ebonyi'),
        ('Edo','Edo'),
        ('Ekiti','Ekiti'),
        ('Enugu', 'Enugu'),
        ('Federal Capital Territory - Abuja','Federal Capital Territory - Abuja'),
        ('Gombe', 'Gombe'),
        ('Imo','Imo'),
        ('Jigawa','Jigawa'),
        ('Kaduna','Kaduna'),
        ('Kano', 'Kano'),
        ('Katsina', 'Katsina'),
        ('Kebbi','Kebbi'),
        ('Kogi','Kogi'),
        ('Kwara','Kwara'),
        ('Lagos','Lagos'),
        ('Nasarawa','Nasarawa'),
        ('Niger','Niger'),
        ('Ogun','Ogun'),
        ('Ondo','Ondo'),
        ('Osun','Osun'),
        ('Oyo','Oyo'),
        ('Plateau','Plateau'),
        ('Rivers','Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba','Taraba'),
        ('Yobe','Yobe'),
        ('Zamfara','Zamfara'),
    )
    Name = models.CharField(max_length=200)
    Sex = models.CharField(max_length=8,choices = SEXCHOICES)
    age = models.CharField(max_length=2)
    state = models.CharField(max_length=500,choices = STaTES)
    lastseenat = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    uploaddate = models.DateTimeField(auto_now_add=True,null = True)

    def __str__(self):
        return 'Missing ' + self.age + ' year old' + ' with name ' + self.Name + ', last seen at ' + self.lastseenat

