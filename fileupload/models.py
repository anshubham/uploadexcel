#python imports
from datetime import datetime

#django imports
from django.db import models
from django.forms import ModelForm
from django.utils.safestring import mark_safe


#local imports

#inter app imports

#third party imports

class CatsData(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    vendor_name = models.CharField(max_length=200)
    batch_no = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)

class CatsNi(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

class CheckFile(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

# class UploadCatsData(models.Model):
#     docfile = models.FileField(upload_to='/home/shubham/Project/CATS/catdata_files/') 
#     def doc_name(self): 
#         return self.docfile.name.split('/')[-1]
#     def button(self):
#         return mark_safe('<a href="{% url "printsome" %}" >Import to DB</a>')
#     button.allow_tags = True

# class UploadCatsNi(models.Model):
#     docfile = models.FileField(upload_to='/home/shubham/Project/CATS/catni_files/') 
#     def doc_name(self): 
#         return self.docfile.name.split('/')[-1]
#     def button(self):
#         return mark_safe('<a href="{% url "printsome" %}" >Import to DB</a>')    
#     button.allow_tags = True
        
# class UploadDocument(models.Model):
#     docfile = models.FileField(upload_to='/home/shubham/Project/CATS/process_files/') 
#     def doc_name(self): 
#         return self.docfile.name.split('/')[-1]
#     def button(self):
#         return mark_safe('<a href="{% url "printsome" %}" >Import to DB</a>')    
#     button.allow_tags = True    