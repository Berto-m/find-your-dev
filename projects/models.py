from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    #null = true means that we can create a record of this value if there's no description
    #black = true means when we submit a form or post request, we can leave it blank
    #one is for the database and other one is for django to know

    #auto_now_add = true generates the time at the time of creation
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    #without this method, the admin know what to read 
    #so django reads it as project object with a uniquie id
    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'down Vote'),
    )
    #owner = 
    # this specifies the action we want the a project is deleted
    # on_delete.cascade will delete all the review for that project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    # choices will create dropdown the VOTE TYPE tuple
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)