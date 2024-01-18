from django.db import models

# Create your models here.
class House(models.Model):
    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField(
        verbose_name="Price",
        help_text="Positive Numbers Only"
        )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed?",
        default=True,
        help_text="Does this house allow pets?")

    def __str__(self):
        return self.name


