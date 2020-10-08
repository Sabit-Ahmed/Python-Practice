from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    #relationship with built in User class
    user = models.OneToOneField(User,'on_delete')
    #Additional custom attributes
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='pro_pics',blank=True)#upload_to='pro_pics'

    def __str__(self):
        return self.user.username #username is built-in attribute of User
