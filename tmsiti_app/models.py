from django.db import models

from accounts.models import User


# Create your models here.
class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class News(AbstractBaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Announcements(AbstractBaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class CEOs(AbstractBaseModel):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()


class OrganizationalStructure(AbstractBaseModel):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Contact(AbstractBaseModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    appeal_type = models.CharField(max_length=255)
    file_upload = models.FileField(upload_to='uploads/')


class Fund(AbstractBaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    year = models.IntegerField()
    description = models.TextField()


class BuildingRegulations(AbstractBaseModel):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    document = models.FileField(upload_to='building_regulations/')


class Word(models.Model):
    UZBEK = 'uz'
    RUSSIAN = 'ru'
    ENGLISH = 'en'
    TURKISH = 'tr'

    LANGUAGE_CHOICES = [
        (UZBEK, 'Uzbek'),
        (RUSSIAN, 'Russian'),
        (ENGLISH, 'English'),
        (TURKISH, 'Turkish'),
    ]

    word = models.CharField(max_length=100)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)


class Subsystem(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.name


class Rating(models.Model):
    product = models.ForeignKey(News, on_delete=models.CASCADE, related_name = 'rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(choices=((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s {self.rating}-star rating for {self.product}"
