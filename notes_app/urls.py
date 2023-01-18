"""notes_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from notesapp.views import (user_notes, group_notes,
                            create_note, get_audio_from_text,
                            get_text_from_image, NoteView)


urlpatterns = [
    path('notesapp/usernote/<int:id>/', NoteView.as_view(), name="user_note"),
    path('notesapp/usernotes/', user_notes, name="user_notes"),
    path('notesapp/groupnotes/', group_notes, name="group_notes"),
    path('notesapp/createnote/', create_note, name="create_note"),
    path('notesapp/getaudio/', get_audio_from_text, name="get_audio"),
    path('notesapp/gettextfromimage/', get_text_from_image, name="get_text_from_image"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
