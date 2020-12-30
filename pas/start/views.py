from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.http import HttpResponse, Http404, HttpResponseForbidden
from .models import School_User, Project, Project_assign



def login(request):
    if request.method == "POST":
        data = request.POST
        number = data.get('username')
        password = data.get('password')
        try:
            School_User.get_user_by_number(number, password)
        except:
            return render(request, 'start/login.html', {'user_notfound': 'True'})
        user = School_User.get_user_by_number(number, password)
        request.session['User'] = user.name
        request.session['number'] = user.number
        request.session['profession'] = user.profession
        request.session['student_id'] = user.id
        return redirect('dashboard')
    else:
        return render(request, 'start/login.html', {'user_notfound': 'False'})


def dashboard(request):
    if request.method == "GET":
        us_id = request.session.get('student_id')
        us_name = request.session.get('User')
        profession = request.session.get('profession')
        projs = Project_assign.return_project_assign(us_id)
        if profession == None:
            return render(request, 'start/error/error.html')
        else:
            return render(request, 'start/dashboard.html', {'name': us_name, 'profession': profession,
            'projects': projs})

            

"""if request.session.get('profession') == 'Teacher':
    return HttpResponse("You are a Teacher.")
elif request.session.get('profession') == 'Student':
    return HttpResponse("You are a Student.")"""
        

def signup(request):
    if request.method == "POST":
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        number = postData.get('number')
        password = postData.get('password')
        profession = postData.get('profession')

        user = School_User(name = name,
                            email = email,
                            number = number,
                            password = password,
                            profession = profession,
                            )
        user.register()
        return render(request, 'start/dashboard.html', {'name': user.name, 'profession': user.profession})
    else:   
        return render(request, 'start/signup.html')

def base(request):
    return render(request, 'start/base.html')

def aboutus(request):
    return render(request, 'start/aboutus.html')


def submit(request):
    if request.method == "POST":
        us_id = request.session.get('student_id')
        if us_id == None:
            return render(request, 'start/error/error.html')
        else:
            link = request.POST.get('link')
            project_spid = request.POST.get('pr_id')
            pa = Project_assign.objects.get(pk = project_spid)
            pa.project_status = "SUBMITTED"
            pa.submission_link = link
            pa.save()
            return redirect('dashboard')
    else:
        return render(request, 'start/error/error.html')

def logout(request):
    request.session.flush()
    return render(request, 'start/login.html')

    """#id = request.session.get('student_id')
    #print(id)
    #
    latest_question_list = Project_assign.objects.all()
    print(latest_question_list)
    #output = ', '.join([q for q in latest_question_list])
    #return HttpResponse(output)

    #return render(request, 'start/dashboard.html', {'profession': professsion})"""