from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import RegisterForm
from join.forms import JoinForm
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from rest_framework import generics, mixins, status
from .serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.
class ProductRegister(FormView):
    template_name = 'product_register.html'
    form_class = RegisterForm
    success_url = "/product"

    def form_valid(self, form):
        product = Product(
            name = form.data.get('name'),
            target = form.data.get('target'),
            price = form.data.get('price'),
            place = form.data.get('place'),
            buy_link = form.data.get('buy_link'),
            description = form.data.get('description'),
            product_image = self.request.FILES['product_image']
        )
        product.save()
        return super().form_valid(form)

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = JoinForm(self.request)
        return context

class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')
        
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ProductRegisterAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    # def get_queryset(self):
    #     return Product.objects.all().order_by('id')
        
    # # def get(self, request, *args, **kwargs):
    # #     return self.retrieve(request, *args, **kwargs)

    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)