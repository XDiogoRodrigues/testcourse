from django.shortcuts import render

from .forms import CourseModelForm, SectionModelForm, CategoryModelForm, SubCategoryModelForm

from .models import Course, Section, ClassRoom, Category, SubCategory

from django.contrib import messages

from utils import list_courses
   

def create_course(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST, request.FILES)
        if form.is_valid():
            value_check = True
            if request.POST.getlist('news'):
                value_check = True
            else:
                value_check = False

            sub_category = SubCategory.objects.get(name=request.POST['subcategory'])
            course_search = Course.objects.filter(name=request.POST['name'])
            if course_search:
                messages.error(request, f'O {request.POST['name']} já está cadastrado!')
            else:
                course = Course(name=request.POST['name'], video=request.FILES.getlist('video')[0], description_short=request.POST['description_short'], detailed_description=request.POST['detailed_description'], news=value_check, price=request.POST['price'], level=request.POST['level'], image=request.FILES['image'], name_teacher=request.POST['name_teacher'], sub_category=sub_category)
                course.save()
                messages.success(request, f'O {request.POST['name']} foi cadastrado com sucesso!')       
          
    return render(request, 'ap_courses/create_course.html', context={
        'name_page': 'Adicionar Curso',
        'subcategories': SubCategory.objects.order_by('name').all()
    })


def create_section_class(request):
    if request.method == 'POST':
        form = SectionModelForm(request.POST, request.FILES)
        if form.is_valid():
            course = Course.objects.get(name=request.POST['course'])
            course_all = course.section_set.all()
            verdadeiro = False

            for c in course_all:
                if c.name == request.POST['name_section']:
                    verdadeiro = True
                    break
    
            if verdadeiro:
                messages.error(request, f'A {request.POST['name_section']} já está cadastrado neste curso!')
            else:
                course_add = Course.objects.get(name=request.POST['course'])
                section = Section(name=request.POST['name_section'], course=course_add)
                section.save()
                section = Section.objects.get(name=request.POST['name_section'])
                classes = request.POST['classes'].split('.')
                classes = [ClassRoom.objects.create(name=c.strip()) for c in classes]
  
                for class_room in classes:
                    section.classes_room.add(class_room)

                messages.success(request, f'{request.POST['name_section']}, salva no curso {request.POST['course']}!')
          
           
    courses = Course.objects.order_by('name_course').all()
    return render(request, 'ap_courses/create_Section_class.html', context={
        'courses': courses,
        'name_page': 'Adicionar Seção'
    })


def create_category(request):
    if request.method == 'POST':
        form = CategoryModelForm(request.POST or None)
        if form.is_valid():
            category_exists = Category.objects.filter(name=request.POST['name'])
            if category_exists:
                messages.error(request, f'Categoria {request.POST['name']}, já esta cadastrada!')
            else:
                Category.objects.create(name=request.POST['name'])
                messages.success(request, f'Categoria {request.POST['name']},registrada com sucesso!')
    return render(request, 'ap_courses/create_category.html')


def create_sub_category(request):
    categories = Category.objects.order_by('name').all()
    if request.method == 'POST':
        form = SubCategoryModelForm(request.POST or None)
        if form.is_valid():
            sub_category_exists = SubCategory.objects.filter(name=request.POST['name'])
            search_categories = Category.objects.get(name=request.POST['category'])

            if not sub_category_exists and sub_category_exists not in search_categories.subcategory_set.all():
                subcategory = SubCategory(name=request.POST['name'], category=search_categories)
                subcategory.save()
                messages.success(request, f'A sub-categoria {request.POST['name']}, foi cadastrada com sucesso na categoria {search_categories.name}!')
            else:
                messages.error(request, f'A sub-categoria {request.POST['name']}, já está cadastrada na categoria {search_categories.name}')

    return render(request, 'ap_courses/create_sub_category.html', context={
        'categories': categories
    })


def home(request):
    courses = Course.objects.order_by('name').all()
    courses_news = Course.objects.filter(news=True).order_by('?')

    if request.method == 'POST':
        list_search = [course for course in courses if request.POST['search'].lower() in course.name.lower()]

        if len(list_search) == 0:
            message = f'Nenhum curso listado com a palavra chave "{request.POST['search']}"'
        elif len(list_search) == 1:
            message = f'{len(list_search)} Curso listado com a palavra chave "{request.POST['search']}"'
        else:
            message = f'{len(list_search)} Cursos listados com a palavra chave "{request.POST['search']}"'

        return render(request, 'ap_courses/list_search.html', context= {
        'courses': list_search,
        'search': message,
        'name_page': 'Udemy',
        'categories': Category.objects.order_by('name').all(),
        'quantity_cart': len(list_courses)

        })

    return render(request, 'ap_courses/list_course.html', context={
        'courses': courses,
        'search': f'{len(courses)} Cursos listados',
        'name_page': 'Udemy',
        'categories': Category.objects.order_by('name').all(),
        'courses_news': courses_news,
        'quantity_cart': len(list_courses)
    })


def detail(request, slug):
    course = Course.objects.get(slug=slug)
    return render(request, 'ap_courses/detail_course.html', context={
        'course': course,
        'name_page': course.name,
        'quantity_cart': len(list_courses)

    })


def list_courses_subcategory(request, slug):    

    if request.method == "POST":
        courses_search = Course.objects.order_by('name').all()
        list_search = [course for course in courses_search if request.POST['search'].lower() in course.name.lower()]

        if len(list_search) == 0:
            message = f'Nenhum curso listado com a palavra chave "{request.POST['search']}"'
        elif len(list_search) == 1:
            message = f'{len(list_search)} Curso listado com a palavra chave "{request.POST['search']}"'
        else:
            message = f'{len(list_search)} Cursos listados com a palavra chave "{request.POST['search']}"'

        return render(request, 'ap_courses/list_search.html', context= {
        'courses': list_search,
        'search': message,
        'name_page': 'Udemy',
        'categories': Category.objects.order_by('name').all(),
        'quantity_cart': len(list_courses)
        })
  
    subcategory = SubCategory.objects.get(slug=slug)
    courses = subcategory.course_set.order_by('name').all()

    if len(courses) == 0:
        message = f'Nenhum curso listado'  
    elif len(courses) == 1:
        message = f'{len(courses)} Curso de {subcategory.name} listado'
    else:
        message = f'{len(courses)} Cursos de {subcategory.name} listados'
            
    return render(request, 'ap_courses/list_search.html', context={
        'courses': courses,
        'search': message,
        'name_page': f'Cursos {subcategory.name}',
        'categories': Category.objects.order_by('name').all(),
        'quantity_cart': len(list_courses)
    })
    
