from django.db import models

class Citations(models.Model):
    # '''
    #     Collaborators field may be taken out
    # '''
    abstract = models.CharField('abstract', max_length=10000, blank=False)
    collaborators = models.CharField('collaborator', max_length=255)
    title = models.CharField('title', max_length=255, blank=False)
    date = models.DateField('date', blank=False)
    paper = models.TextField('paper', blank=False)

    orcid = models.CharField('orcid', max_length=255, unique=True, default=None)
    doi = models.CharField('doi', max_length=255, unique=True, default=None)

    date_created = models.DateTimeField('date_created', auto_now=True)
    word_occurrences: models.TextField('word_occurrences')

    def __str__(self):
        return 'Citation\n\tTitle: {}\n\tDate: {}'.format(self.title, self.date)

class Keywords(models.Model):
    name = models.CharField('name', max_length=255, blank=False)

    def __str__(self):
        return 'Keyword\n\tname: {}'.format(self.name)


class KeywordsCitations(models.Model):
    # '''
    #     IMPORTANT
    #         Django doens't let us do Composite PKs
    #         so we need to change DB schema to avoid duplicates
    # '''
    keyword_id = models.ForeignKey(Keywords, on_delete=models.DO_NOTHING, blank=False)
    citation_id = models.ForeignKey(Citations, on_delete=models.DO_NOTHING, blank=False)

    def __str__(self):
        return 'KeywordCitation\n\tkeyword_id: {}\n\tcitation_id {}'.format(self.keyword_id, self.citation_id)

class Academics(models.Model):
    name = models.CharField('name', max_length=255, blank=False)

    def __str__(self):
        # ideally outputs the academic name and citation name
        return 'Academic\n\tid: {}\n\tname:'.format(self.id, self.name)

class AcademicCitations(models.Model):
    # '''
    #     IMPORTANT
    #         Django doens't let us do Composite PKs
    #         so we need to change DB schema to avoid duplicates
    # '''
    academic_id = models.ForeignKey(Academics, on_delete=models.DO_NOTHING, blank=False)
    citation_id = models.ForeignKey(Citations, on_delete=models.DO_NOTHING, blank=False)

    def __str__(self):
        # ideally outputs the academic name and citation name
        return 'AcademicCitation\n\tacademic_id: {}\n\tcitation_id: {}'.format(self.academic_id, self.citation_id)


class Users(models.Model):
    academic_id = models.ForeignKey(Academics, on_delete=models.DO_NOTHING, blank=False)
    username = models.CharField('username', max_length=255, blank=False)
    email = models.EmailField('email', blank=False)
    password = models.CharField('password', max_length=255, blank=False)
    date_create = models.DateTimeField('date_created', auto_now=True)

    def __str__(self):
        return 'User\n\tname: {}\n\temail: {}'.format(self.username, self.email)

class University(models.Model):
    name = models.CharField('name', max_length=255, blank=False)

    def __str__(self):
        return 'University\n\tname: {}'.format(self.name)

class Schools(models.Model):
    name = models.CharField('name', max_length=255, blank=False)
    university_id = models.ForeignKey(University, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'School\n\tid: {}\n\tname: {}\n\tuniv_id: {}'.format(self.id, self.name, self.university_id)

class SchoolsAcademics(models.Model):
    # '''
    #     IMPORTANT
    #         Django doens't let us do Composite PKs
    #         so we need to change DB schema to avoid duplicates
    # '''
    school_id = models.ForeignKey(Schools, on_delete=models.DO_NOTHING, blank=False)
    academic_id = models.ForeignKey(Academics, on_delete=models.DO_NOTHING, blank=False)

    def __str__(self):
        return 'SchoolsAcademics\n\tschool_id: {}\n\tacademic_id: {}'.format(self.school_id, self.academic_id)

class Departments(models.Model):
    name = models.CharField('name', max_length=255, blank=False)
    school_id = models.ForeignKey(Schools, on_delete=models.DO_NOTHING, blank=False)

    def __str__(self):
        return 'Departments\n\tname: {}'.format(self.name)
