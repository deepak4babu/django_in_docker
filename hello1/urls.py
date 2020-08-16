from django.urls import path
from hello1 import views
from hello1.models import LogMessage
home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello1/home.html",
)
urlpatterns = [
    path("", home_list_view, name="home"),
    # hello_there mentioned here is the function in views.py. 
    # This function requires a parameter 'name' which is mentioned in path as "hello/<name>"
    # This 'name' takes the value from the url
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]