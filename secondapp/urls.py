from django.urls import path
from.import views

urlpatterns = [
    
    path('',views.check1,name="check1"),
    path('det/',views.det,name="det"),
    path('rec/',views.rec,name="rec"),
    path('rec1/',views.rec1,name="rec1"),
    path('rec2/',views.rec2,name="rec2"),
    path('loggin/',views.loggin,name="loggin"),
    path('reggister/',views.reggister,name="reggister"),
    path('conttact/',views.conttact,name="conttact"),
    path('regdata/',views.regdata,name="regdata"),
    path('memberlogin/',views.memberlogin,name='memberlogin'),
    path('logoutt/',views.logoutt,name='logoutt'),
    path('jquery/',views.jquery,name='jquery')
       

]
