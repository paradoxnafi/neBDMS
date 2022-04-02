from django.db import models

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

class Post(models.Model):
    author_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=250)
    blood_group = models.CharField(max_length=8, choices=BLOOD_GROUPS, default='O+')
    required_bags = models.PositiveIntegerField()
    deadline = models.DateTimeField()
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author_name + ", Blood group: " + self.blood_group
