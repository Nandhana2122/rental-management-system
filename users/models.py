from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# ---------------- PROFILE MODEL ----------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()



# ---------------- EMAIL OTP ----------------
class EmailOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} OTP"


# ---------------- MOBILE OTP ----------------
class MobileOTP(models.Model):
    mobile = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mobile} OTP"



class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="profiles/", blank=True, null=True)

    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)

    occupation = models.CharField(max_length=100, blank=True, null=True)
    family_size = models.IntegerField(default=1)

    purpose = models.CharField(
        max_length=10,
        choices=[("Rent", "Rent"), ("Buy", "Buy")],
        blank=True,
        null=True
    )

    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    preferred_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"



# class ChatMessage(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.message

# from django.db import models
# from django.contrib.auth.models import User


# class Property(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     title = models.CharField(max_length=200)
#     description = models.TextField()

#     location = models.CharField(max_length=200)
#     rent = models.IntegerField()

#     bedrooms = models.IntegerField()
#     bathrooms = models.IntegerField()

#     wifi = models.BooleanField(default=False)
#     parking = models.BooleanField(default=False)
#     balcony = models.BooleanField(default=False)
#     washing_machine = models.BooleanField(default=False)

#     image = models.ImageField(upload_to='properties/')


# class PropertyImage(models.Model):
#     property = models.ForeignKey(
#         Property,
#         on_delete=models.CASCADE,
#         related_name="images"
#     )
#     image = models.ImageField(upload_to="property_images/")



from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)

    rent = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()

    wifi = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    washing_machine = models.BooleanField(default=False)

    image = models.ImageField(upload_to='properties/')

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="property_images/")

    def __str__(self):
        return self.property.title

class ChatMessage(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message