from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # After successful making of post this method redirects to the required page.
    # Here we have used the reverse method that will return the string of a particular page.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})