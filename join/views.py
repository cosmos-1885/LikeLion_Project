from pyexpat import model
from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.views.generic import CreateView, TemplateView, ListView
from django.db import transaction
from users.models import Users
from products.models import Product
from .models import Join
from .forms import JoinForm
from .decorators import login_required

# Create your views here.
@method_decorator(login_required, name = 'dispatch')
class JoinCreate(FormView):
    form_class = JoinForm
    success_url = '/product'

    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Join(
                product = prod,
                user = Users.objects.get(email = self.request.session.get('user'))
            )
            order.save()
            prod.people += 1
            prod.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/'+str(form.data.get('product')))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request':self.request
        })
        return kw

@method_decorator(login_required, name = 'dispatch')
class JoinList(ListView):
    template_name = "join.html"
    context_object_name = 'join_list'

    def get_queryset(self, **kwargs):
        queryset = Join.objects.filter(user__email = self.request.session.get('user'))
        return queryset