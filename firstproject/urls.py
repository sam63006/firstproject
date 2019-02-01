"""

firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""


from django.contrib import admin
from django.urls import path, re_path


from myapp.views import sayhello, hello2, hello3, hello4, hello5, hello6, hello7, hello8


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sayhello),
    path('sayhello/', sayhello),
    re_path(r'^hello2/(\w+)/$', hello2),
    re_path(r'^hello3/(\w+)/$', hello3),
    re_path(r'^hello4/(\w+)/$', hello4),
    re_path(r'^hello5/$', hello5),    
    re_path(r'^hello6/$', hello6),        
    re_path(r'^hello7/$', hello7),         
    re_path(r'^hello8/(\w+)/$', hello8),        
]
