from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # The current date & time is assigned when an instance of this class is created
    created_on = models.DateTimeField(auto_now_add=True)
    # The current date & time is assigned when an instance of this class is saved,
    # Whenever you edit an instance of this class.
    last_modified = models.DateTimeField(auto_now=True)
    # link our models for categories and posts in such a way that many categories can be assigned to many posts
    # By adding a related_name of posts, we can access category.posts to give us a list of posts with that category
    categories = models.ManyToManyField('Category', related_name='posts')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # One post should have many comments, many to one, but you can't have a comment that corresponds to many post
    # If a post is deleted, then we don't want the comments related to it hanging around
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
