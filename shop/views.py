from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *


class LandingPageView(TemplateView):
    template_name = 'landing.html'


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


# Product

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = "__all__"
    success_url = reverse_lazy('product')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product')


# City

class CityListView(LoginRequiredMixin, ListView):
    model = City
    template_name = 'city.html'


class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    template_name = 'city_new.html'
    fields = "__all__"
    success_url = reverse_lazy('city')


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'city_delete.html'
    success_url = reverse_lazy('city')


# Inventory

class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventory.html'


class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = Inventory
    template_name = 'inventory_new.html'
    fields = "__all__"
    success_url = reverse_lazy('inventory')


class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Inventory
    template_name = 'inventory_delete.html'
    success_url = reverse_lazy('inventory')


# InventoryStock

class InventoryStockListView(LoginRequiredMixin, ListView):
    model = InventoryStock
    template_name = 'inv_stock.html'


class InventoryStockCreateView(LoginRequiredMixin, CreateView):
    model = InventoryStock
    template_name = 'inv_stock_new.html'
    fields = "__all__"
    success_url = reverse_lazy('inv_stock')


class InventoryStockDeleteView(LoginRequiredMixin, DeleteView):
    model = InventoryStock
    template_name = 'inv_stock_delete.html'
    success_url = reverse_lazy('inv_stock')


# Order

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order.html'


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'order_update.html'
    fields = "__all__"
    success_url = reverse_lazy('order')


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'order_delete.html'
    success_url = reverse_lazy('order_list')


# users purchasable products based on their city
class UserProductListView(LoginRequiredMixin, ListView):
    model = InventoryStock
    template_name = 'home.html'

    def get_queryset(self):
        return InventoryStock.objects.filter(inventory__city=self.request.user.city)


# user order submit view    
@login_required(login_url='login')
def user_order_submit_view(request, pk):
    if request.method == 'POST':
        product = InventoryStock.objects.get(id=pk)
        quantity = request.POST.get('quantity')
        if product.stock >= int(quantity):
            product.stock -= int(quantity)
            product.save()
            new_order = Order.objects.create(user=request.user, product=product, quantity=quantity)
            new_order.save()
            return render(request, 'user_order_success.html')
        else:
            return render(request, 'user_order_error.html')

    else:
        product = InventoryStock.objects.get(id=pk)
        context = {'product': product}
        return render(request, 'user_order.html', context)


# users previous orders view
class UserOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'user_order_list.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
