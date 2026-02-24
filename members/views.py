from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
    
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
  
def testing(request):
  # This is how to get all the data from the database, and pass it to the template
  mymembers = Member.objects.all().values()

  # Following are filter examples, to show how to filter the data
  # mymembers = Member.objects.filter(firstname='Emil').values()
  # mymembers = Member.objects.filter(lastname='Refsnes', id=2).values()
  # mymembers = Member.objects.filter(firstname__startswith='L').values()

  # Following is how to order by firstname
  # mymembers = Member.objects.all().order_by('firstname').values()
  # mymembers = Member.objects.all().order_by('firstname','-lastname').values()
  
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))