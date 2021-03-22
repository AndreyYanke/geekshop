from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminProfileForm


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')


# READ
class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# CREATE
class UserCreatView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admin_staff:admin_users')

# UPDATE
class UserUpdateView(UpdateView):
    model = User
    template_name ='adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admin_staff:admin_users')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'BookOfTea - Редактироввание пользователя'
        return context

# DELETE
class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())




# Логика класса UserListView
    # @user_passes_test(lambda u: u.is_superuser)
    # def admin_users(request):
    #     context = {'users': User.objects.all()}
    #     return render(request, 'adminapp/admin-users-read.html', context)

# Логика класса UserCreatView
    # @user_passes_test(lambda u: u.is_superuser)
    # def admin_users_create(request):
    #     if request.method == 'POST':
    #         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
    #         if form.is_valid():
    #             form.save()
    #             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    #     else:
    #         form = UserAdminRegistrationForm()
    #     context = {'form': form}
    #     return render(request, 'adminapp/admin-users-create.html', context)

# Логика класса UserUpdateView
    # @user_passes_test(lambda u: u.is_superuser)
    # def admin_users_update(request, user_id):
    #     user = User.objects.get(id=user_id)
    #     if request.method == 'POST':
    #         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
    #         if form.is_valid():
    #             form.save()
    #             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    #     else:
    #         form = UserAdminProfileForm(instance=user)
    #     context = {'form': form, 'user': user}
    #     return render(request, 'adminapp/admin-users-update-delete.html', context)


# # Логика класса UserUpdateView
    # @user_passes_test(lambda u: u.is_superuser)
    # def admin_users_delete(request, user_id):
    #     user = User.objects.get(id=user_id)
    #     user.is_active = False
    #     user.save()
    #     return HttpResponseRedirect(reverse('admin_staff:admin_users'))
