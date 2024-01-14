from django.db import models

class Resume(models.Model):
    name        = models.CharField(max_length=100)
    comment     = models.TextField()
    career      = models.TextField()
    role        = models.TextField()
    salary      = models.TextField()
    intro       = models.TextField()
    information = models.TextField()
    certificate = models.TextField()
    
    def __str__(self):
        return self.title