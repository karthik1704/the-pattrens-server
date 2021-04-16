from django.shortcuts import  render

# Create your views here.
def index(request):
    return render(request, 'ui_apps/apps.html', {'range': range(10)})

def project_detail(request):
    return render(request, 'ui_apps/project_detail.html', {})


def project_slider(request):
    return render(request, 'ui_apps/project_slider.html', {})  