from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, name, email, password=None):
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            name = name
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, name, email, password=None):
        user = self.create_user(
            username = username,
            name = name,
            email = email,
            password= password
        )
        user.isAdmin = True
        user.save()
        return user

class User(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique = True, max_length = 100)
    name = models.CharField('Nombre completo', unique = False, max_length = 200)
    email = models.EmailField('Correo electronico', max_length = 254, unique = True)
    profile_photo = models.ImageField('Imagen de perfil', upload_to = 'profileImages/',  max_length = 200, blank = True, null = True)
    isActive = models.BooleanField(default=True)
    isAdmin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return f'{self.name}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.isAdmin

class Writer(models.Model):
    name = models.TextField()
    email = models.EmailField()

class Article(models.Model):
    name = models.TextField()
    writer = models.OneToOneField(Writer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    last_edited = models.DateField(auto_now=True)
    title = models.TextField()
    subtitle = models.TextField()
    image = models.FileField(null=True, blank=True)
    body = models.TextField()

class Favorites_users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Bookmark_users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


