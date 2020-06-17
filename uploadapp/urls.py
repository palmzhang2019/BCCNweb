from django.conf.urls import url, include
from uploadapp.views import FileUploadView


urlpatterns = [
    url(r'$', FileUploadView.as_view())
    ]