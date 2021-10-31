from django.urls import path
from api.views import (advisorAPIView, advisorsAPIView,
                       bookingAPIView, bookedAPIView)

urlpatterns = [

    path('advisor/', advisorAPIView.as_view()),
    path('advisors/<int:pk>/', advisorsAPIView.as_view()),
    path('booking/', bookingAPIView.as_view()),
    path('booking/<int:pk>/', bookedAPIView.as_view()),

]
