from django.db import models

# Create your models here.
class Login(models.Model):
    u_id=models.CharField(max_length=50,null=False)
    u_pw=models.CharField(max_length=200,help_text="Enter PassWord",null=False)

    
    def __str__(self):
        return self.u_id


    
    