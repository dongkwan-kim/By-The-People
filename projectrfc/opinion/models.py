from django.db import models

class Speaker(models.Model):
    profile = models.URLField()
    name = models.CharField(max_length=5, primary_key=True)

    fact = models.FloatField(default=0)
    non_fact = models.FloatField(default=0)
    undecided = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Mention(models.Model):
    hash_id = models.CharField(max_length=56)
    speaker = models.ManyToManyField("Speaker")
    date_time = models.DateTimeField()
    md_sentence = models.ManyToManyField("Sentence")

    def __str__(self):
        return "~".join([self.hash_id[:7]])

class Sentence(models.Model):
    hash_id = models.CharField(max_length=56)
    text = models.TextField()
    fact = models.CharField(max_length=15, default="undecided")
    md_comment = models.ManyToManyField("Comment", default=None)

    def __str__(self):
        return "~".join([self.text[:20], self.fact])

class Comment(models.Model):
    hash_id = models.CharField(max_length=56)
    uid = models.CharField(max_length=56)
    crowd_id = models.CharField(max_length=12)
    md_children = models.ManyToManyField("self", default=None)

    text = models.TextField()

    vote_up = models.IntegerField(default=0)
    vote_down = models.IntegerField(default=0)

    assert_kind = models.CharField(max_length=10, default="undecided")

class Crowd(models.Model):
    crowd_id = models.CharField(max_length=12)
    name = models.CharField(max_length=12)
    score = models.IntegerField(default=0)
