from django.db import models

# # Create your models here.
# class Song(models.Model):
#     title = models.TextField()
#     artist = models.TextField()
#     image = models.ImageField()
#     audio_file = models.FileField(blank=True, null=True)
#     audio_link = models.CharField(max_length=200, blank=True, null=True)
#     duration = models.CharField(max_length=20)
#     paginate_by = 2

#     def __str__(self):
#         return self.title


# Song Model to store each song's data
class Songs(models.Model):
    title = models.CharField(("title"), max_length=100)
    artiste = models.CharField(("artiste"), max_length=100)
    album = models.CharField(("album"), max_length=100)
    media_thumbnail = models.URLField()
    media_url = models.URLField()
    likes = models.IntegerField(default=0)
    time_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        # ordering = ("time_added")
        ordering =["time_added"]
    def __str__(self):
        return f"{self.title} by {self.artiste}"