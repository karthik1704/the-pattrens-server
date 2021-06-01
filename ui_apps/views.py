from django.shortcuts import  get_object_or_404, render
from ui_apps.models import (
    Category,
    Element,
    Pattern,
    Platform,
    Tag,
    UiApps,
)

# Create your views here.
def index(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    platforms = Platform.objects.all()
    patterns = Pattern.objects.all()
    elements = Element.objects.all()

    context = {
        'categories': categories,
        'tags': tags,
        'platforms': platforms,
        'patterns': patterns,
        'elements': elements
    }
    return render(request, 'ui_apps/apps.html', context)

def project_detail(request, slug):
    project = get_object_or_404(UiApps, slug=slug)
    platforms = Platform.objects.filter(uiapps=project.id)
    patterns = Pattern.objects.all()
    elements = Element.objects.all()

    context = {
        'project':project, 
        'platforms':platforms,
        'patterns': patterns,
        'elements': elements
        
    }
    return render(request, 'ui_apps/project_detail.html', context)


def project_slider(request):
    return render(request, 'ui_apps/project_slider.html', {})  