from django.urls import include,path
from.import views

urlpatterns = [
    
    path('',views.hello,name="hello"),
    path('display/',views.display,name="display"), 
    path('sdata/',views.sdata,name="sdata"),
    path('check/',views.check,name="check"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('sam/',views.sam,name="sam"),
    path('dem/',views.dem,name="dem"),
    path('log/',views.log,name="log"),
    path('adlogin/',views.adlogin,name="adlogin"),
    path('logout/',views.logout,name="logout"),
    path('adlogout/',views.adlogout,name="adlogout"),
    path('cat1/',views.cat1,name='cat1'),
    path('cat2/',views.cat2,name='cat2'),
    path('cattable/',views.cattable,name='cattable'),
    path('edit1/<int:id>',views.edit1,name='edit1'),
    path('update1/<int:id>',views.update1,name='update1'),
    path('delete1/<int:id>',views.delete1,name='delete1'),
    path('hello/',views.hello,name='hello'),
    path('pdata/',views.pdata,name='pdata'),
    path('protable/',views.protable,name='protable'),
    path('edit2/<int:id>',views.edit2,name='edit2'),
    path('update2/<int:id>',views.update2,name='update2'),
    path('delete2/<int:id>',views.delete2,name='delete2'),
    
    
    
    

]

