from django.urls import path

from commentapp.views import CommentCreateView

app_name = 'commnetapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),

]