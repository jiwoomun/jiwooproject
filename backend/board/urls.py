from django.conf.urls import url
from .views import Boards as boards
#.하나는 같은 경로에 있는.. 시블링 관계

urlpatterns =[
    url('/postwrite', boards.as_view()),
]