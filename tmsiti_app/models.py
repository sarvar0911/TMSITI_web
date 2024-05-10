from django.db import models


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
