from django.shortcuts import render
from .models import Users
from django.views.generic import FormView
from users.forms import LoginForm, RegisterForm
from users.models import Users
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from rest_framework import generics, mixins, status
from .serializers import UsersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def home(request):
    return render(request, 'home.html', {'user' : request.session.get('user')})

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'
    
    def form_valid(self, form):
        user = Users(
            email = form.data.get('email'),
            password = make_password(form.data.get('password')),
            name = form.data.get('name'),
            phone = form.data.get('phone'),
            address = form.data.get('address')
        )
        user.save()
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

class UsersAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = UsersSerializer

    def get_queryset(self):
        return Users.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class UsersAPI(APIView):
#   def get(self, request):
#     users = Users.objects.filter(active = True)
#     serializer = UsersSerializer(users, many = True)
#     return Response(serializer.data)

#   def post(self, request):
#     serializer = UsersSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status = status.HTTP_201_CREATED)
#     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)