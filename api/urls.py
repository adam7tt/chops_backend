from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    url(r'^academics/$', AcademicListAPIView.as_view(), name="create"),
    url(r'^citations/$', CitationListAPIView.as_view(), name="create"),
    url(r'^keywords/$', KeywordListAPIView.as_view(), name="create"),
    url(r'^universities/$', UniversityListAPIView.as_view(), name="create"),
    url(r'^departments/$', DepartmentListAPIView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
