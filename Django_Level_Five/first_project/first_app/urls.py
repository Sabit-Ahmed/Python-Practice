from django.urls import path
from first_app import views

#TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns=[
path('base/',views.base,name='base'),
path('sign_up/',views.register,name='register'),
path('login/',views.user_login,name='user_login'),
]
