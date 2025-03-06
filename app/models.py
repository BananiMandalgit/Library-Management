from django.db import models

# Create your models here.
# class Book (models.Model):
#     id=models.IntegerField(unique=True, primary_key=True)
#     title=models.CharField(max_length=128)
#     author=models.CharField(max_length=128)
    #  page=models.IntegerField(max_length=128)
#     
# isbn=models.IntegerField(max_length=128)

#     is_active= models.BooleanField(default=True)
#     is_staff= models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = ''
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.id, self.title
    

class student (models.Model):
    student_id=models.IntegerField(unique=True)
    name=models.CharField(max_length=128)
    email= models.EmailField(unique=True)
    password= models.CharField(max_length=128)
    department= models.CharField(max_length=128)
    gender= models.CharField(max_length=128)
    year= models.CharField(max_length=128)

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['student_id']

    def __str__(self):
        return self.student_id
    
class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    isbn = models.CharField(max_length=128,unique=True)
    in_stock = models.IntegerField(default=0)
    publishDate = models.CharField(max_length=250,null=True, blank=True)
    language = models.CharField(max_length=128, blank=True, null=True)
    category = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    pages= models.IntegerField(null=True, blank=True)
    File_format = models.CharField(max_length=128 ,blank=True, null=True)
    
    def __str__(self):
        return self.title, self.isbn
    
    def borrow_book(self):
        if self.in_stock > 0:
            self.in_stock -=1
            self.save()
            return True
        return False
    
    def return_book(self):
        self.in_stock += 1
        self.save()
        

