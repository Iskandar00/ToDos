from django.db import models


class ToDo(models.Model):
    todo = models.TextField(max_length=1000)
    done = models.BooleanField(default=False)

