
from django.urls import path
from end_user import views

urlpatterns = [
    path('feedbacks/', views.FeedbackAPIView.as_view()),
    path('service/', views.ServiceAPIView.as_view()),
    path('contact/', views.ContactAPIView.as_view()),
    path('master-service/', views.MasterServiceAPIView.as_view()), 
    #  path('service/<int:pk>', views.ServiceAPIView.as_view()), 
   
]
