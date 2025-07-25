from django.forms import ModelForm

from .models import Course, Section, ClassRoom, Category, SubCategory

class CourseModelForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description_short', 'news', 'price', 'level', 'image', 'name_teacher']


class SectionModelForm(ModelForm):
    class Meta:
        model = Section
        fields = ['name',]


class CategoryModelForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name',]


class SubCategoryModelForm(ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name',]