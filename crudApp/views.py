from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from .models import User
from .forms import StudentRegistration
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

class home(TemplateView):
    template_name='crud/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context ={'form': fm, 'stu': stud}
        return context

    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pas)
            reg.save()
        return HttpResponseRedirect('/')

class data_delete(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
    

class update_data(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'crud/change.html', {'form': fm})

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')

    



