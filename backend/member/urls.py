from django.conf.urls import url
from .views import Members as members
#.하나는 같은 경로에 있는-> 시블링 관계

urlpatterns =[
    url('/signup', members.as_view()),
    url('/login', members.as_view()),

]