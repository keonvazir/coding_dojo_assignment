-e TODO in soccer_team/soccer_team/: 
	
 _____________ in soccer_team/settings.py,  INSTALLED_APPS list 
	
 __________________________'apps.roster_app', 
	
 _____________ in urls.py:  
	
 __________________________ comment out, or just delete 'from django.contrib import admin'
	
 __________________________url(r'^', include('apps.roster_app.urls')),	# add to url patterns, don't forget the comma 
	TODO in soccer_team/appsroster_app/: 
	
 _____________ in urls.py:
	
 __________________________ from django.conf.urls import url
	
 __________________________ from . import views
	
 __________________________in urlpatterns add
	
 ________________________________________ url(r'^$', views.index), # index is the name of a method in views.py
	
 _____________ in views.py:
	
 __________________________from django.shortcuts import render, redirect
	
 __________________________def index(request):
	
 __________________________    return render(request, 'roster_app/index.html')
