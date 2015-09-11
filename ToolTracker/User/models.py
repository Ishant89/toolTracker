from django.db import models

# Create your models here.
from django.utils.timezone import now
from django.contrib.auth.models import User

class Tool(models.Model):
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=now())
    user = models.ForeignKey(User)
    description  = models.TextField()
    usage = models.TextField()
    file = models.FileField("Upload the file of the tool")




class ToolLocation(models.Model):
    tool = models.ForeignKey(Tool)
    location = models.TextField()

class Fields(models.Model):
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=now())
    description = models.TextField()
    field_type = (
        ("FT","File Type"),
        ("INT","Integer Type"),
        ("FLT","Float Type"),
        ("STR","String Type"),

    )

    type = models.CharField("Type of argument",choices=field_type,max_length=500)
    env = models.CharField("Env variables",help_text="Specify env var as name=$value",max_length=100000)
    tool = models.ForeignKey(Tool)

