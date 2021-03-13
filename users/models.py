from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Permission


# class Permission(models.Model):
#     name = models.CharField(max_length=200)



class Role(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)




class User(AbstractUser):
    first_name = models.CharField(max_length = 200)
    second_name = models.CharField(max_length=200)
    third_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200, unique=True)
    password = models.CharField(max_length = 200)
    rank = models.CharField(max_length = 200)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    

    def get_full_name(self):
        full_name = '%s %s %s %s' % (self.first_name, self.secondy_name, self.third_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        short_name = '%s %s' % (self.first_name, self.last_name)
        return short_name.strip()