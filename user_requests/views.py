from django.db.models import fields
from django.shortcuts  import render
from django.forms import ModelForm
from django.views.generic.edit import  CreateView

from user_requests.models import UserRequest

def request_form(request):

    return render(request, 'user_requests/request.html', {})


class MyRequestForm(ModelForm):
    class Meta:
        model = UserRequest
        fields = ('app_name', 'platform', 'app_url', 'description', 'name', 'country', 'email', 'promotion')

class UserRequestCreateView(CreateView):
    model = UserRequest
    template_name = 'user_requests/request.html'
    form_class = MyRequestForm
    success_url = '/'
