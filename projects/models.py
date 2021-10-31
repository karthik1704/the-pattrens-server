from django.db import models

from django_extensions.db.fields import AutoSlugField

from django.conf import settings

USER = settings.AUTH_USER_MODEL 

def my_slugify_function(self, content):
        return content.replace('_', '-').replace(' ', '-').lower()

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from=['catergory_name'] ,slugify_function=my_slugify_function)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    class Meta:
        """Meta definition for Element."""

        verbose_name = 'Category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.category_name

class Platform(models.Model):
    platform_name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from=['platform_name'] ,slugify_function=my_slugify_function)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.platform_name
 

class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    platform = models.ManyToManyField(Platform)

    project_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    copy_right = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ImageField(upload_to='projects/')    
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    def __str__(self)->str:
        return  self.project_name

# Project Image Model

class ProjectVersion(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    version = models.CharField(max_length=10)
    slug = AutoSlugField(populate_from='version', slugify_function=my_slugify_function)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project', 'platform', 'version'], name='unique_projectversion')
        ]
    def __str__(self) -> str:
        return self.project.project_name

class Pattern(models.Model):
    """Model definition for Pattern."""

    # TODO: Define fields here
    pattern_name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='pattern_name', slugify_function=my_slugify_function)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    class Meta:
        """Meta definition for Pattern."""

        verbose_name = 'Pattern'
        verbose_name_plural = 'Patterns'

    def __str__(self)->str:
        """Unicode representation of Pattern."""
        return self.pattern_name

class Element(models.Model):
    """Model definition for Element."""

    # TODO: Define fields here
    element_name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='element_name', slugify_function=my_slugify_function)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    class Meta:
        """Meta definition for Element."""

        verbose_name = 'Element'
        verbose_name_plural = 'Elements'

    def __str__(self)->str:
        """Unicode representation of Element."""
        return self.element_name

class ProjectImage(models.Model):
    """Model definition for ProjectImage."""

    # TODO: Define fields here

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="projects/")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    class Meta:
        """Meta definition for ProjectImage."""

        verbose_name = 'ProjectImage'
        verbose_name_plural = 'ProjectImages'

    def __str__(self)->str:
        """Unicode representation of ProjectImage."""
        return self.project.project_name


# Project Like Model
class Like(models.Model):
    user = models.ForeignKey(USER, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self)->str:
        return f'{self.project.name} -{self.count}'
        