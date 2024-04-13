from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_list, name = 'people'),
    path('doctors/', views.doctor_list, name = 'doctors'),
    path('teachers/', views.teacher_list, name = 'teachers'),
    path('<int:pid>/', views.people_detail, name = 'person_detail'),
    # path('new/', views.post_new, name='new_new'),
    # path('<int:pid>/edit/', views.post_edit, name='new_edit'),
]