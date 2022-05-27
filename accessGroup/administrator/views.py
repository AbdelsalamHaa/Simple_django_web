from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

@method_decorator(login_required, name='get')
class Accounts(View):
    template_name = 'administrator/accounts_list.html'

    def get(self, request):
        if not request.user.is_superuser:
            return HttpResponse('You do not have access to this page', status=401)

        users = User.objects.all()

        context = {
            'users': users
        }
        return render(request, self.template_name, context=context)


class AddAccount(View):
    template_name = 'administrator/add_account.html'

    def get(self, request):
        if not request.user.is_superuser:
            return HttpResponse('You do not have access to this page', status=401)

        return render(request, self.template_name)

    def post(self, request):
        if not request.user.is_superuser:
            return HttpResponse('You do not have access to this page', status=401)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        if first_name and last_name and username and email and password:
            user = User.objects.create()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.profile.location = address
            user.profile.phone = phone
            # user = User(first_name=first_name, last_name=last_name, username=username, email=email)
            user.save()
            user.set_password(password)
            user.save()
            return redirect('accounts_list')
        else:
            return render(request, self.template_name)


class EditAccount(View):
    template_name = 'administrator/edit_account.html'

    def get(self, request):
        if not request.user.is_superuser:
            return HttpResponse('You do not have access to this page', status=401)

        user_id = request.GET.get('id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return HttpResponse('User not found', status=404)
        else:
            return render(request, self.template_name, context={'user': user})

    def post(self, request):
        if not request.user.is_superuser:
            return HttpResponse('You do not have access to this page', status=401)

        user_id = request.GET.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get("address")
        phone = request.POST.get('phone')
        user = User.objects.get(id=user_id)


        if request.POST.get("save_user"):
            if first_name and last_name and username and email:
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.profile.location = address
                user.profile.phone = phone
                if password:
                    user.set_password(password)
                    user.save()
                    if user.is_superuser :
                        return redirect('login')
                user.save()
            else:
                return render(request, self.template_name)

        elif request.POST.get("remove_user"):
            if not user.is_superuser:
                # This is how to delete a user (or any object)
                user.delete()
            else:
                return HttpResponse('You Can not remove the admin user', status=401)

        return redirect('accounts_list')
