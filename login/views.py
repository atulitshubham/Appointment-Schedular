from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from .forms import LoginForm
from .models import Account
# from django.http import HttpResponse

# Create your views here.

def login(request):
	logout(request)
	return render(request, 'login/login.html')

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")


def loginSubmit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            try:
            	query = str(Account.objects.get(username=u_name)).split()
            	if query[0]==u_name and u_pass==query[1]:
            		request.session['username'] = u_name
            		return HttpResponseRedirect('/dashBoard')
            	else:
            		return HttpResponse("<h2>Wrong password</h2>")
            except:
            	return HttpResponse("<h2>No Such User</h2>")
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    # return render(request, 'name.html', {'form': form})
    return HttpResponse("<h2>POST ony accepted</h2>")
