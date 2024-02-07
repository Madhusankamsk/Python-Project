from django.http import HttpResponse
from django.template import loader
from .models import StudentData, SchoolData, ClassData, AwardData, AssessmentAreaData, AnswerData, SubjectData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    schools = SchoolData.objects.all()
   # print(schools)
    className = StudentData.objects.values('class_name').distinct()
    assessmentAreas = AssessmentAreaData.objects.all()
    answers = AnswerData.objects.all()
    award = AwardData.objects.all()
    className = ClassData.objects.all()
    subjects = SubjectData.objects.all()
    students_list = StudentData.objects.values('student_id', 'first_name', 'last_name').distinct()
    paginator = Paginator(students_list, 10)  # Show 10 students per page

    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

   # summery = StudentData.objects.values('').distinct()
    template = loader.get_template('myfirst.html')
    context = {
        'schools': schools,
        'class': className,
        'assessmentAreas': assessmentAreas,
        'answers': answers,
        'award': award,
        'subjects': subjects,
        'students': students
    }
    return HttpResponse(template.render(context, request))
