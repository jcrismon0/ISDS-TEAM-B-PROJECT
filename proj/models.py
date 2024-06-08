from django.db import models

# Create your models here.
class Topic(models.Model):
    """a todo list."""
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """return a string rep of model."""
        return self.text
class Entry(models.Model):
    """info about task"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name_plural = 'entries'
def _str_(self):
    """return a string represting entry."""
    return f"{self.text[50]}..."