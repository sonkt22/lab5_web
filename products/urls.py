from django.urls import path
from . import views
from .views import ItemUpdateView, ItemDeleteView, ItemDetailView

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('new', views.add_product, name='add_product'),
    path('update/<int:pk>', ItemUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>', ItemDetailView.as_view(), name='detail_product'),
    path('delete/<int:pk>', ItemDeleteView.as_view(), name='delete_product'),
]