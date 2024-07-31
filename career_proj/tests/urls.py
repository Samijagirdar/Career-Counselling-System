from django.urls import path
from .import views
from .views import aptitude_test,results

urlpatterns=[
    path('',views.rooms,name='tests'),
    path('aptitude-test/', aptitude_test, name='aptitude_test'),
    path('results/', results, name='results'),
]
