from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('vacancy/', views.empVacancy, name="empVacancy"),
    path('task/', views.teenTask, name="teenTask"),
    path('teen/vacancy/', views.teenVacancy, name="teenVacancy"),
    path('teen/vacancy/description/', views.teendescription, name="teendescription"),
    path('teenager/workspace/', views.teenProf, name="teenProf"),
    path('employer/workspace/', views.employProf, name="employProf"),
    path('parent/workspace/', views.parentProf, name="parentProf"),
    path('employer/create-new-vacancy', views.emplEdit, name="emplEdit"),
    path('search/', views.search_action, name="search_action"),
    path('create/', views.create_post, name="create_post"),
    path('posts/', views.post_list, name="post_list"),
    path('posts/', views.empVacancy, name="empTeen"),
    path('posts/', views.empTeen, name="empTeen"),
    path('posts/', views.empMyTeen, name="empMyTeen"),
    path('delete/<int:post_id>/', views.delete_post, name="delete_post"),
    path('register/child/', views.register_child, name='register_child'),
    path('register/parent/', views.register_parent, name='register_parent'),
    path('register/employer/', views.register_employer, name='register_employer')
]