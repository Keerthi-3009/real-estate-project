from django.db import models
from django.conf import settings


class PropertyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"


class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=255, blank=True, help_text="Full address for map display")
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')

    property_type = models.ForeignKey(
        PropertyType,
        on_delete=models.CASCADE

    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Properties"




class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.title}"


class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='inquiries', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inquiries"


class Favorite(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )
    user = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - {self.property.title}"

class SellerSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    property_title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property_title} by {self.name}"


class SellerSubmissionImage(models.Model):
    submission = models.ForeignKey(
        SellerSubmission,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='seller_submissions/')

    def __str__(self):
        return f"Image for {self.submission.property_title}"