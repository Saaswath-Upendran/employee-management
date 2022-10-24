from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,CreateView,ListView,UpdateView,DetailView,DeleteView)
from .forms import *
from django.http import *
# Create your views here.

class HomePage(TemplateView):
    template_name = "index.html"

def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            return redirect('employe:home')

        else:
            return HttpResponse(user_form.errors,profile_form.errors)


    else:
        user_form = UserForm()
        profile_form = UserProfileInfo()
    return render(request,'create.html',{
        'user_form':user_form,
        "profile_form":profile_form
    })

class EmployeList(ListView):
    context_object_name = 'employe_list'
    model = UserProfile
    template_name = 'list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employe_list'] = UserProfile.objects.all()
        return context

class EmployeDetail(DetailView):
    context_object_name = 'employe_detail'
    model = UserProfile
    template_name = 'detail.html'

    


class EmployeUpdate(UpdateView):
    context_object_name = "employe_update"
    model = UserProfile
    fields = '__all__'
    success_url  = reverse_lazy("employe:list")
    template_name = "update.html"


class EmployeDelete(DeleteView):
    model = UserProfile
    success_url = reverse_lazy("employe:list")
    template_name = "delete.html"
    