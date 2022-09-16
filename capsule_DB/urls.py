from django.urls import include, path

from . import views

urlpatterns = [
    #타임캡슐 저장하는 api(post)
    path('capsule/all', views.Capsule.as_view()),
    #path('capsule/<int:id>', views.Capsule_open.as_view()),
]