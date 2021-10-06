
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from validate_email import validate_email

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email, password, and addition fields.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        
        if not validate_email(email):
            raise ValueError(_('Invalid email set'))
        
        if not password:
            raise ValueError('Users must have a password')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user

    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email, password, and addition fields.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        return self.create_user(email, password, **extra_fields)
