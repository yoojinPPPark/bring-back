from unicodedata import decimal
from django.db import models
from datetime import datetime

class Capsule(models.Model):
    user_id = models.CharField(max_length = 10)
    user_nickname = models.CharField(max_length = 15)
    capsule_shape = models.IntegerField()
    #shape은 정해져 있으니까 1,2,3,4로 디비저장하자(1:알약, 2:하트, 3: 별, 4: 다이아몬드)
    capsule_color = models.CharField(max_length = 10)
    capsule_title = models.CharField(max_length = 20)
    capsule_deadline = models.DateField()
    capsule_message = models.TextField()
    
    

