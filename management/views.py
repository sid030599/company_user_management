from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, DetailView, UpdateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Company, CustomUser
from .forms import CustomUserForm
from management.serializers import CompanySerializer, CustomUserSerializer

class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_detail')  # Redirect to user detail page
        return render(request, self.template_name, {'error': 'Invalid credentials'})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'user_detail.html'
    model = CustomUser

    def get_object(self):
        return self.request.user


class CompanyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'company_detail.html'
    model = Company

    def get_object(self):
        company_id = self.kwargs.get('company_id')
        return get_object_or_404(Company, id=company_id)


class UserDetailEditView(LoginRequiredMixin, FormView):
    template_name = 'user_detail_edit.html'
    form_class = CustomUserForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect('user_detail')


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
