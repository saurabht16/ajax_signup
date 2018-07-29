from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    initial = {'username': 'abc'}


class exampleView(View):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        if form.is_valid():

            return HttpResponseRedirect('/valid/')
        return render(request, self.template_name, {'form': form})

