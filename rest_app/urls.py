from django.urls.conf import path
from rest_app.views import ListView,DetailView

urlpatterns = [
    path('',ListView.as_view(),name='list_view'),
    path('<int:pk>/',DetailView.as_view(),name='detail_view'),

]