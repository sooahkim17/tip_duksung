from django.db import models

# Create your models here.
class Login(models.Model):
    u_id=models.CharField(max_length=50,null=False)
    u_pw=models.CharField(max_length=200,help_text="Enter PassWord",null=False)
    th=models.IntegerField(null=False,help_text="Enter th")
    name=models.CharField(max_length=20,null=False)
    major=models.CharField(null=False,help_text="Enter major",max_length=300)
    stu_id=models.IntegerField(null=False,help_text="Enter student_id")
    email=models.EmailField(null=False)
    staff=models.BooleanField(null=False)

    
    def __str__(self):
        return self.u_id


    
    