from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    username = models.OneToOneField(User, related_name='users', on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=30)
    address = models.TextField()
    district = models.CharField(max_length=25)
    thana = models.CharField(max_length=25)
    union = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=25)
    bank_count_no = models.IntegerField(default=0)
    contact_number = models.IntegerField(default=0)
    select_gender = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    sex = models.CharField(max_length=6, choices=select_gender)
    profile_photo = models.ImageField(upload_to="users", blank=True, null=True)
    select_user = (
        ('agent', 'Agent'),
        ('member', 'Member'),
    )
    select_hand = (
        ('left', 'Left'),
        ('right', 'Right'),
    )
    user_type = models.CharField(max_length=8, choices=select_user)
    hand_type = models.CharField(max_length=6, choices=select_hand)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='product', blank=True, null=True)
    discount_price = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
