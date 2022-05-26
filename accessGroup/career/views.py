from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,'login.html')

# This is a function-based view of profile page
def profile_page(request):
    return render(request, 'career/profile.html')

# And this is a class-based view of the profile page (Works the same way but better in every way)
@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class ProfilePage(View):
    template_name = 'career/profile.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if first_name and last_name:
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.save()

        return render(request, self.template_name)

def admin_page(request):
    return render(request,'table_users.html')



