from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.CanalDeTodos.as_view(),name='canaldetodos'),
    
]