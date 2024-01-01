# models.py

from django.db import models

class Avocat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    numero_tlfn = models.CharField(max_length=20)
    specialisation =models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    langue = models.TextField(max_length=20, default='english')
    password = models.TextField(max_length=20,default='null')

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    body = models.TextField()

class ProfilAvocat(models.Model):
    avocat = models.OneToOneField(Avocat, on_delete=models.CASCADE)
    experience = models.TextField()
    rating = models.FloatField()
    site_web = models.URLField(blank=True, null=True)
    blogs = models.ManyToManyField(Blog, related_name='profils_avocats', blank=True)

    def __str__(self):
        return f"Profil de {self.avocat.prenom} {self.avocat.nom}"

class Client(models.Model): 
    username = models.CharField(max_length=100,default = "null")
    password = models.CharField(max_length=100,default = "null")
    email = models.EmailField(unique=True)
    numero_tlfn = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Avis(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    avocat = models.ForeignKey(Avocat, on_delete=models.CASCADE)
    texte = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"Avis de {self.client.nom} sur {self.avocat.nom}"

class RendezVous(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    avocat = models.ForeignKey(Avocat, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"Rendez-vous chez {self.avocat.nom} avec {self.client.nom} le {self.date}"
