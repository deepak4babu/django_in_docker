from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import re
from django.shortcuts import redirect
from hello1.forms import LogMessageForm
from hello1.models import LogMessage
from django.views.generic import ListView

#def home(request):
#    return render(request, "hello1/home.html")
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
def about(request):
    return render(request, "hello1/about.html")

def contact(request):
    return render(request, "hello1/contact.html")
def hello_there(request, name):
    return render(
        request,
        'hello1/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello1/log_message.html", {"form": form})
"""
# home and hello_there function, without templates
def home(request):
    return HttpResponse("Hello, Django!")  
def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    # You can also provide html tags in the content like below. But not recommended.
    # Developers avoid such a practice because it opens the app to cross-site scripting (XSS) attacks.
    # content = "<h1>Hello there, " + clean_name + "! It's " + formatted_now + "!</h1>"

    # Better practice is to keep HTML out of your code entirely by using templates, 
    # so that your code is concerned only with data values and not with rendering
    return HttpResponse(content)
"""