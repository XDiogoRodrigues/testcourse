from django.urls import path

from .views import create_course, create_section_class, home, detail, create_category,create_sub_category, list_courses_subcategory

urlpatterns = [
    path('udemy.com.br', home, name='home'),
    path('udemy-create-category', create_category, name='create_category'),
    path('udemy-create-subcategory', create_sub_category, name='create_sub_category'),
    path('udemy-create-course', create_course, name='create_course'),
    path('udemy-create-section', create_section_class, name='create_section'),
    path('udemy-course-detail/<slug:slug>', detail, name='detail'),
    path('udemy-search-course-subcategory/<slug:slug>', list_courses_subcategory, name='search_subcategory'),
    
]
