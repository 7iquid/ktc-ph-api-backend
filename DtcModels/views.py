from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render_to_response
# from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        content = '<h1>dummy content</h1>'
    return render(request, 'formstemplateko.html', {'form': form})
    # return HttpResponse(form)

def http_response_view(request):
    content = '<p>dummy content</p>'
    return HttpResponse(form)