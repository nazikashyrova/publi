from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse

from publi import settings

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True): # may look repetitive adding staff, admin and active status, but it simplifies the
                                                                                        # work when using create_staffuser() and create_superuser()
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError('User must have a password')
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.is_active = is_active
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True, is_admin=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    biography = models.CharField(max_length=300,null=True)
    profile_image = models.ImageField(upload_to='media/profile_images/',default='media/default.jpg')
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_absolute_url(self):
        return reverse('main:user-detail', kwargs={'pk': self.pk})

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    """@property
    def is_active(self):
        return self.is_active"""


class LoginAttempt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_attempts = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'user: {}, attempts: {}'.format(self.user.email, self.login_attempts)


class FriendshipRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_friendship_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_friendship_requests')
    status = models.CharField(choices=(('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')), default='pending', max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)


