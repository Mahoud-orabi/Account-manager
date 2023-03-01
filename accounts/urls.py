from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('add_client/',views.AddClientView.as_view(),name='add_client'),
    path('<slug:slug>/',login_required(views.ClientDetails.as_view()),name='client'),
    path('<slug:slug>/delete/',views.delete_client,name='delete_client'),
    path('<slug:slug>/category/<int:id>/',views.CategoryDetailView.as_view(),name='category_details'),
    path('<slug:slug>/category/<int:id>/delete/',views.delete_category,name='delete_category'),
    path('<slug:slug>/category/add_new_category/',views.AddNewCategoryView.as_view(),name='add_new_category'),
    path('<slug:slug>/category/<int:id>/add_list/',views.AddListView.as_view(),name='add_list'),
    path('<slug:slug>/category/<int:id>/lists/<int:list_id>',views.ListUpdateView.as_view(),name='update_list'),
]
