from django.db import models

# Create your models here.
class Tip(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    update_date=models.DateTimeField(auto_now=True)
    file=models.FileField(upload_to='tip/',null=True)
    hit=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50]
    
    @property
    def update_counter(self):
        self.hit=self.hit+1
        self.save()


