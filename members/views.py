from django.http import HttpResponse
from django.template import loader
from .models import Member

rdm_img = "https://picsum.photos/200/300"

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    
    context = {
        'mymembers': mymembers,
        'random_url_img': rdm_img,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    
    context = {
        'mymember': mymember,
        'random_url_img': rdm_img,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')

    context = {
        'img': rdm_img,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    mydata = Member.objects.filter(firstname='Nick').values() | Member.objects.filter(firstname='lars').values()

    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))


def about(request):
    template = loader.get_template('about.html')
    
    context = {
        'img': rdm_img,
    }
    return HttpResponse(template.render(context, request))

  