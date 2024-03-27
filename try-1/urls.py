from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('try-1/', admin.site.urls),
	# Enter the app name in following
	# syntax for this to work
	path('', include("projectApp.urls")),
]
