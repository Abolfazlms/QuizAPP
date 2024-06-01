from django.db import models

# Create your models here.
class Category(models.Model):
    name =   models.CharField(max_length=255)
    def __str__(self):
        return self.name 
class Question (models.Model):
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='quiz/')
    audio_file = models.FileField(upload_to='audio/')
    choice = models.IntegerField(default = 0)    
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.content
