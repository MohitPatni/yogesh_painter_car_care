
from django.urls import path
from end_user import views

urlpatterns = [
    path('master-service/', views.MasterServiceListCreateAPIView.as_view()),
    path('master-service/<int:pk>', views.MasterServiceRetrieveUpdateAPIView.as_view()),
    path('feedback/', views.FeedbackListCreateAPIView.as_view()),
    path('feedback/<int:pk>', views.FeedbackRetrieveUpdateAPIView.as_view()),
    path('services/', views.CreateServiceRetriveBYMasterIDServiceAPIView.as_view()),
    path('all-services/', views.ServiceListAPIView.as_view()),
    path('services/<int:pk>', views.ServiceRetrieveUpdateByIDAPIView.as_view()),
    path('photo-gallary/', views.CreatePhotoGallaryRetriveBYMasterIDServiceAPIView.as_view()),
 
   
   
]
