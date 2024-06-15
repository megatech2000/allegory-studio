from django.db import models

# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=250, unique=True)
    desc = models.CharField(max_length=300, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    home_image = models.ImageField(upload_to="Image/", default="Image/None/Noimg.jpg")
    image_1 = models.ImageField(upload_to="Image/", default="Image/None/Noimg.jpg")
    image_2 = models.ImageField(upload_to="Image/", default="Image/None/Noimf.jpg")
    image_3 = models.ImageField(upload_to="Image/", default="Image/None/Noimf.jpg")
    image_4 = models.ImageField(upload_to="Image/", default="Image/None/Noimf.jpg")
    image_5 = models.ImageField(upload_to="Image/", default="Image/None/Noimf.jpg")
    image_6 = models.ImageField(upload_to="Image/", default="Image/None/Noimf.jpg")
    

    def __str__(self):
        return self.title
    
class Featured(models.Model):
    heading = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, unique=True)
    title = models.CharField(max_length=250, unique=True)
    image= models.ImageField(upload_to="Image/", default="Image/None/Noimg.jpg")
    num_1 = models.TextField()
    num_2 = models.TextField()
    num_3 = models.TextField()

    def __str__(self):
        return self.title

class GearCategory(models.Model):
    title = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return self.title

class GearItem(models.Model):
    category = models.ForeignKey(GearCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to="Image/", default="Image/None/Noimf.jpg")

    def __str__(self):
        return self.title
