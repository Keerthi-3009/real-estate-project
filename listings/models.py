from django.db import models


class PropertyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=200)
    property_type = models.ForeignKey(
        PropertyType,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="properties/")

    def __str__(self):
        return f"Image for {self.property.title}"


class Inquiry(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Inquiry from {self.name}"


class Favorite(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )
    user = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - {self.property.title}"

# Create your models here.
