from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
	uno = models.CharField(max_length=100, blank=True, null=True)
	name = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField(max_length=100,blank=True, null=True)
	phone = models.CharField(max_length=100,blank=True, null=True)
	desc = models.TextField(max_length=100,blank=True, null=True)
	created_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.name

	#define own auto_now for date field
	# def save(self, *args, **kwargs):
        # On save, update timestamps
        # if not self.id:
        #     self.created_at = timezone.now()
        # self.updated_at = timezone.now()
        # return super(Contact, self).save(*args, **kwargs)	