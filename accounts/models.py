
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class  UsuarioManager(BaseUserManager):
    def create_user(self, email, rut, nombre, apellido ,password = None):
        if not rut:
            raise ValueError("Debes ingresar un rut")
        if not email:   
            raise ValueError("Debes ingresar un correo")
        usuario = self.model(
            email=self.normalize_email(email),
            rut=rut,
            nombre = nombre,
            apellido = apellido,
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self ,rut, email,nombre, apellido, password):
        usuario = self.create_user(
            email,
            rut=rut,
            nombre = nombre,
            apellido = apellido,
            password = password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    id_usuario = models.BigAutoField(primary_key=True)
    email = models.EmailField(verbose_name="Correo", max_length=100,  unique=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(null=True,max_length=9)
    usuario_administrador = models.BooleanField(default=False)
    usuario_activo = models.BooleanField(default=True)
    usuario_empleado = models.BooleanField(default=False)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut','nombre','apellido']


    def __str__(self):
        return f'{self.nombre},{self.apellido}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador


        