# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
##


# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name,mobile, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        client = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )

        client.set_password(password)
        client.save(using=self._db)
        return client

    def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

# Create your User Model here.
class Client(AbstractBaseUser,PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240,default ="")
    last_name = models.CharField(max_length=255,default ="")
    mobile = models.CharField(max_length=50,default ="")


    is_staff = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(default=False) # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','mobile']

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

#

class Langue(models.Model):
    name = models.CharField(max_length=200,unique = True,primary_key = True )

class specialisation(models.Model):
    name = models.CharField(max_length=200,unique = True,primary_key = True )


class Avocat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    numero_tlfn = models.CharField(max_length=20)
    specialisation = models.ManyToManyField(specialisation, blank=True)
    email = models.EmailField(unique=True)
    langue =models.ManyToManyField(Langue, blank=True)

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
