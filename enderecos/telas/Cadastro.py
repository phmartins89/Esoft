from django.http import HttpResponse
from django.views.generic import View

class Cadastro(View):
    initial = {'key': 'value'}
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('This is GET request')

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is POST request')