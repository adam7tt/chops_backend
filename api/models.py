from django.db import models

class Academic(models.Model):
    academic_id = models.AutoField('academic_id', primary_key=True)
    name = models.CharField('name', max_length=255, blank=False)
    citations = models.ManyToManyField('Citation')
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.name, self.university)

class Citation(models.Model):
    citation_id = models.AutoField('citation_id', primary_key=True)
    title = models.CharField('title', max_length=255, blank=False)
    date = models.DateField('date', blank=False)
    abstract = models.TextField('abstract', blank=False)
    paper = models.TextField('paper', blank=False)

    #collaborators = models.CharField('collaborator', max_length=255)
    keywords = models.ManyToManyField('Keyword')

    #orcid = models.CharField('orcid', max_length=255, unique=True, default=None)
    #doi = models.CharField('doi', max_length=255, unique=True, default=None)

    date_entered = models.DateTimeField('date_entered', auto_now=True)
    #word_occurrences: models.TextField('word_occurrences')

    def __str__(self):
        return self.title

class Keyword(models.Model):
    name = models.CharField('name', max_length=255, primary_key=True, blank=False)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField('name', max_length=255, primary_key=True, blank=False)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField('name', max_length=255, primary_key=True, blank=False)

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
