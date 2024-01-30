from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import jwt
from .managers import CustomUserManager
from LMS.settings import JWT_SECRET

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # extra fields
    @property
    def membership_date(self):
        return self.date_joined    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    @property
    def token(self):
        # expiration time 
        expiration_time = timezone.now() + timedelta(hours=10)
        
        payload = {
            'user_id': self.pk,
            'email': self.email,
            'exp': expiration_time,
            
        }

        # using the RS256 algorithm
        token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')

        return token