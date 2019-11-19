from django.db import models

"""
    Note that Django
        - gives each model a primary key id automatically
        - blank=False is by default, no need to add it
    https://docs.djangoproject.com/en/2.2/topics/db/models/#automatic-primary-key-fields
"""

class Academic(models.Model):
    name = models.CharField('name', max_length=255)
    citations = models.ManyToManyField('Citation')
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.name, self.university)

class Citation(models.Model):
    title = models.CharField('title', max_length=255)
    date = models.DateField('date')
    abstract = models.TextField('abstract')
    paper = models.TextField('paper')

    #collaborators = models.CharField('collaborator', max_length=255)
    keywords = models.ManyToManyField('Keyword')

    #orcid = models.CharField('orcid', max_length=255, unique=True, default=None)
    #doi = models.CharField('doi', max_length=255, unique=True, default=None)

    date_entered = models.DateTimeField('date_entered', auto_now=True)
    #word_occurrences: models.TextField('word_occurrences')

    def __str__(self):
        return self.title

class Keyword(models.Model):
    name = models.CharField('name', max_length=255)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField('name', max_length=255)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField('name', max_length=255)

    def __str__(self):
        return self.name
#    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False)

#class School(models.Model):
#    name = models.CharField('name', max_length=255, blank=False)
#    university_id = models.ForeignKey(University, on_delete=models.DO_NOTHING)

#class User(models.Model):
#    academic_id = models.ForeignKey(Academics, on_delete=models.DO_NOTHING, blank=False)
#    username = models.CharField('username', max_length=255, blank=False)
#    email = models.EmailField('email', blank=False)
#    password = models.CharField('password', max_length=255, blank=False)
#    date_create = models.DateTimeField('date_created', auto_now=True)
