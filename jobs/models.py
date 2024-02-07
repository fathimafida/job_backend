from django.db import models


class PostJob(models.Model):
    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    jobType = models.CharField(max_length=255)

    def __str__(self):
        return self.title
