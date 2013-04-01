from django.db import models


class Category(models.Model):
  title = models.CharField(max_length=200)

  def __unicode__(self):
    return self.title

class Piece(models.Model):
  title = models.CharField(max_length=200)
  blurb = models.TextField()
  image = models.ImageField(upload_to='pieces')
  category = models.ManyToManyField(Category)

  def __unicode__(self):
    return self.title
