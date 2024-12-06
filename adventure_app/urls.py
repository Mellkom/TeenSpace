from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('vacancy/', views.empVacancy, name="empVacancy"),
    path('task/', views.teenTask, name="teenTask"),
    path('teen/vacancy/', views.teenVacancy, name="teenVacancy"),
    path('teen/vacancy/description/', views.teendescription, name="teendescription"),
    path('search/', views.search_action, name="search_action"),
    path('create/', views.create_post, name="create_post"),
    path('posts/', views.post_list, name="post_list"),
    path('delete/<int:post_id>/', views.delete_post, name="delete_post"),
]