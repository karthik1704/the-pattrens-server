from django.db import models


# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

class Pattern(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

class Element(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

class Version(models.Model):
    name = models.FloatField()
    slug = models.SlugField(unique=True)

class Tag(models.Model):
    name = models.CharField(max_length=25)

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name


class UiApps(models.Model):
    name = models.CharField(max_length=100)
    copyright = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ImageField(upload_to='apps/')
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 


    class Meta:
        verbose_name = 'User Interface Apps'
        verbose_name_plural = 'User Interface Apps'


    def __str__(self) -> str:
        return self.name

    def uiimage(self):
        if not hasattr(self, '_uiimages'):
            self._uiimages = self.uiimages_set.all()
        return self._uiimages


class UiImages(models.Model):
    uiapp = models.ForeignKey(UiApps, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING)
    version = models.ForeignKey(Version, on_delete=models.DO_NOTHING)
    pattern = models.ForeignKey(Pattern, on_delete=models.DO_NOTHING,  blank=True, null=True)
    element = models.ForeignKey(Element, on_delete=models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='apps/')

