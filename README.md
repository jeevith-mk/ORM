# Ex02 Django ORM Web Application
## Date: 6/10/2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import Vehicle_Details_DB,Vehicle_Details_DBAdmin
admin.site.register(Vehicle_Details_DB,Vehicle_Details_DBAdmin)

models.py
from django.db import models
from django.contrib import admin
class Vehicle_Details_DB(models.Model):
    company=models.CharField(max_length=20)
    model=models.CharField(max_length=10)
    reg_no=models.IntegerField()
    myear=models.IntegerField()
    onwer_name=models.CharField(max_length=20)
    owner_address=models.TextField()
    licence_num=models.CharField(max_length=10,primary_key=True)
    num_plate=models.IntegerField()
class Vehicle_Details_DBAdmin(admin.ModelAdmin):
    list_display=["company","model","reg_no","myear","onwer_name","owner_address","licence_num","num_plate"]

```

## OUTPUT
![alt text](<Screenshot (9).png>)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
