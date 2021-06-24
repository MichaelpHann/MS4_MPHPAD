from django.db import models

class ProjectCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Project Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(
        'ProjectCategory', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    descriptive_name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    date = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
