from django.db import models
from django.utils import timezone

class Post(models.Model):   # models.Model represents that it is a django model, django will know that it should be saved in database, # Post is our object
    #defing our properties and methods down
	author = models.ForeignKey('auth.user')     # it has got a relation with another object(model)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


# Create your models here.
