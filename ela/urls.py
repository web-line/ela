from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from ela.sites import (main_admin_site, student_admin_site, teacher_admin_site)

urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(main_admin_site.urls), name="admin"),
    url(r"^student/", include(student_admin_site.urls), name="student"),
    url(r"^teacher/", include(teacher_admin_site.urls), name="teacher"),
    url(r"^account/", include("usr.urls")),
    url(r"^account/", include("account.urls")),
    url(r"^notifications/", include("pinax.notifications.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
