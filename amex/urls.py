"""amex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [

	path('', views.index),
    path('/static/Download_content/d_1.xlsx', views.download_file),
    path('/static/Download_content/d_2.xlsx', views.download_file_1),
    path('/static/Result/product1.csv', views.download_file_result1),
    path('/static/Result/product2.csv', views.download_file_result2),
    path('/static/Result/product3.csv', views.download_file_result3),
    path('/static/Result/product4.csv', views.download_file_result4),
    path('/static/Result/product5.csv', views.download_file_result5),
    path('/static/Result/merged.xlsx', views.download_file_result5),
	path('result', views.result),
    path('gotoHome', views.index),
   
    path('admin/', admin.site.urls),
]
