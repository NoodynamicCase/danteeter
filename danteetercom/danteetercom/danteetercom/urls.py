from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import TemplateView
from email_me import views as emailme_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('css_template_basic/', TemplateView.as_view(template_name="css_template_basic.html"), name="css_template_basic"),
    path('css_template_1/', TemplateView.as_view(template_name="css_template_1.html"), name="css_template_1"),
    path('css_template_2/', TemplateView.as_view(template_name="css_template_2.html"), name="css_template_2"),
    path('css_template_3/', TemplateView.as_view(template_name="css_template_3.html"), name="css_template_3"),
    path('email_me/', emailme_views.email_me, name="email_me"),
    # INCLUDE
    path('blog/', include('blog.urls')),
    path('contacts/', include('contacts.urls')),
    path('shopping/', include('shopping.urls')),
    path('humancapital/', include('humancapital.urls')),
    path('to_do_list/', include('to_do_list.urls')),
    path('hobbies/', include('hobbies.urls')),
    path('timer/', include('timer.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',
    serve, {'document_root':settings.MEDIA_ROOT, }),
    ]







"""danteetercom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
