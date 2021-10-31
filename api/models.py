from django.db import models
from django.contrib.auth import get_user_model

# Models here:-

User = get_user_model()

class advisor(models.Model):
    advisor_name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    advisor_photo = models.ImageField(upload_to='advisor_pic/', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.advisor_name

class booking(models.Model):
    My_bookings_name = models.CharField(max_length=50, default='',)
    booked_on = models.DateTimeField(auto_now_add=True)
    Booked_advisor = models.ForeignKey(advisor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.My_bookings_name
