from django.db import models

# Create your models here.
class Category(models.Model):
    name =   models.CharField(max_length=255)
    def __str__(self):
        return self.name 
class Question (models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    category = models.CharField(max_length=100, null=True, default=None)
    image = models.ImageField(upload_to='quiz/',default='quiz/default.jpg')
    audio_file = models.FileField(upload_to='audio/')
    score = models.IntegerField(default = 0)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
