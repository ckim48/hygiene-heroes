from django.db import models

# Steps to get from ERD to Model Code
# 1. Entities will become their own Class (eg. Category)
# 2. Attributes will become the properties (eg. name)
# 3. Foreign keys, drop the "_id" (eg. category_id in Material, it will just be category)
# 4. drop the id from the ERD

class Category(models.Model):
    name = models.CharField(max_length=200) # string

class Material(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='materials')
    name = models.CharField(max_length=200)
    media_type = models.CharField(max_length=200)

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Comment(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
