from django.db import models


NATIONALITY_CHOICES = (
    ('FRANCE', 'France'),
    ('BRAZIL', 'Brazil'),
    ('CHINA', 'China'),
    ('USA', 'United States'),
    ('SPAIN', 'Spain'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200) # blank and null are setted up as False by default.
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
