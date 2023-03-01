from django.urls import path
from . import views

urlpatterns = [
    path('persons/',views.person,name='person'),
    path('persons/add_person/',views.add_person,name='add_person'),
    path('persons/<slug:slug>/delete_person/',views.delete_person,name='delete_person'),
    path('persons/<slug:slug>/',views.person_details,name='person_details'),
    path('persons/<slug:slug>/add_details/',views.add_details,name='add_details'),
    path('persons/<slug:slug>/<int:id>/delete_details/',views.delete_details,name='delete_details'),
    # path('persons/<slug:slug>/<int:id>/update_details/',views.DetailsUpdateView.as_view(),name='update_details'),
    path('persons/<slug:slug>/<int:id>/update_details/',views.detail_update,name='update_details'),
]
