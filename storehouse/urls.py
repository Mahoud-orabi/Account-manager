from django.urls import path
from . import views

urlpatterns = [
    path('stores/',views.stores,name='stores'),
    path('stores/add_store/',views.add_new_store,name='add_store'),
    path('stores/<slug:slug>/delete/',views.delete_store,name='delete_store'),
    path('stores/<slug:slug>/',views.store_details,name='store_details'),
    path('stores/<slug:slug>/add_details/',views.add_details,name='add_details'),
    path('stores/<slug:slug>/<int:id>/delete/',views.delete_details,name='delete_details'),
    path('stores/<slug:slug>/<int:id>/Update/',views.DetailsUpdateView.as_view(),name='update_details'),
]
