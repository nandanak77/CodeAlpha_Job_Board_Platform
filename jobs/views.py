from django.http import HttpResponse
from .models import Job
from django.shortcuts import render
from .models import Candidate, Application
from django.http import HttpResponseRedirect

def home(request):
    # temporary override to test
    html = '''
    <h2>Welcome to Jobboard Platform</h2>
    <a href="/jobs/1/" class="btn">REGISTER JOB</a>
    <a href="/candidate/dashboard/" class="btn">CANDIDATE DASHBOARD</a>
    <a href="/employer/dashboard/" class="btn">EMPLOYERS DASHBOARD</a>
    '''
    from django.http import HttpResponse
    return HttpResponse(html)

def job_detail(request, job_id):
    from .models import Job
    job = Job.objects.get(id=job_id)
    return render(request, 'jobs/detail.html', {'job': job})

def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        resume = request.FILES['resume']
        candidate = Candidate.objects.create(name=name, email=email, resume=resume)
        Application.objects.create(candidate=candidate, job=job)
        return HttpResponseRedirect("/")
    return render(request, 'jobs/apply.html', {'job': job})

def employer_dashboard(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/employer_dashboard.html', {'jobs': jobs})

def candidate_dashboard(request):
    apps = Application.objects.all()
    return render(request, 'jobs/candidate_dashboard.html', {'apps': apps})


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})