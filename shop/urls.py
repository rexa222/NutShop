from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),

    path('manage', HomePageView.as_view(), name='admin'),

    path('manage/product', ProductListView.as_view(), name="product"),
    path('manage/product/new', ProductCreateView.as_view(), name="product_new"),
    path('manage/product/<int:pk>/delete/', ProductDeleteView.as_view(), name="product_delete"),

    path('manage/city', CityListView.as_view(), name="city"),
    path('manage/city/new', CityCreateView.as_view(), name="city_new"),
    path('manage/city/<int:pk>/delete/', CityDeleteView.as_view(), name="city_delete"),

    path('manage/inventory', InventoryListView.as_view(), name="inventory"),
    path('manage/inventory/new', InventoryCreateView.as_view(), name="inventory_new"),
    path('manage/inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name="inventory_delete"),

    path('manage/invStock', InventoryStockListView.as_view(), name="inv_stock"),  # inventoryProduct
    path('manage/invStock/new', InventoryStockCreateView.as_view(), name="inv_stock_new"),  # inventoryProduct_new
    path('manage/invStock/<int:pk>/delete/', InventoryStockDeleteView.as_view(), name="inv_stock_del"),  # inventoryProduct_delete

    path('manage/order', OrderListView.as_view(), name="order"),
    path('manage/order/<int:pk>/update/', OrderUpdateView.as_view(), name="order_update"),
    path('manage/order/<int:pk>/delete/', OrderDeleteView.as_view(), name="order_delete"),

    path('home', UserProductListView.as_view(), name='home'),
    path('userOrder/<int:pk>', user_order_submit_view, name="user_order"),  # userOrder
    path('orderList', UserOrderListView.as_view(), name='order_list'),  # orderList
]
