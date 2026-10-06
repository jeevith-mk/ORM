from django.db import models
from django.contrib import admin
class Vehicle_Details_DB(models.Model):
    company=models.CharField(max_length=20)
    model=models.CharField(max_length=20)
    reg_no=models.IntegerField()
    myear=models.IntegerField()
    onwer_name=models.CharField(max_length=20)
    owner_address=models.TextField()
    licence_num=models.CharField(max_length=10,primary_key=True)
    num_plate=models.IntegerField()
class Vehicle_Details_DBAdmin(admin.ModelAdmin):
    list_display=["company","reg_no","myear","onwer_name","owner_address","licence_num","num_plate"]
