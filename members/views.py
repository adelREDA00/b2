from django.shortcuts import render

# Create your views here.
import profile
from pyexpat import model
from django.http import request , HttpResponse
from django.shortcuts import render , redirect ,get_object_or_404
from django.template import context
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm , ProfilePage
from  django.views.generic import DetailView , CreateView
from blogapp.models import Profile

# Create your views here.
def creatuser(request):
    form = SignUpForm()

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    context = {'form':form}
    return render(request, 'registration/register.html',context)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self,*args,**kwargs):
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        context["page_user"]=page_user
        return context


class CreatProfilePage(CreateView):
    model = Profile
    template_name = 'registration/creat_profile_page.html'
    form_class = ProfilePage

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)