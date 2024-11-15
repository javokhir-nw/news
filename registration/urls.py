from django.urls import path

from registration.views import user_logout, SignUp

urlpatterns = [
    path('',SignUp.as_view(),name='signup'),
    path('logout',user_logout,name='logout')
]