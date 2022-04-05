from django.db import models
from author.decorators import with_author

BLOOD_GROUPS = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

@with_author
class Post(models.Model):
#    author_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=250)
    blood_group = models.CharField(max_length=8, choices=BLOOD_GROUPS)
    required_bags = models.PositiveIntegerField()
    deadlineDate = models.DateField()
    deadlineTime = models.TimeField()
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.author) + ", " + str(self.blood_group) + ", " + str(self.address)
