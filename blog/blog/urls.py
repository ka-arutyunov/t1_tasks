from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from blog_api.views import auth

schema_view = get_schema_view(title='Blog API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog_api.urls'), name='blog'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title="Blog API", description="Simple Blog API")),
    path('schema/', schema_view),
    path('github_auth/', auth),
    url('', include('social_django.urls', namespace='social'))

]
