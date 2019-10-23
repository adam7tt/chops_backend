from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Citations)
admin.site.register(Keywords)
admin.site.register(KeywordsCitations)
admin.site.register(Academics)
admin.site.register(AcademicCitations)
# admin.site.register(Users)
admin.site.register(University)
admin.site.register(Schools)
admin.site.register(SchoolsAcademics)
admin.site.register(Departments)
