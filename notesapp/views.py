from django.shortcuts import render, redirect, Http404, HttpResponse
from notesapp.models import Notes
from notesapp.forms import NoteUpdateForm, NoteCreateForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from notesapp.text_to_speech import TxtToAudioConverter
from notesapp.image_to_text import ImgToTxtConverter
from pathlib import Path


# Create your views here.


@login_required
def user_notes(request):
    user = request.user
    return render(request, 'user_notes.html', context={'notes': Notes.objects.filter(author=user)})


@login_required
def group_notes(request):
    user = request.user
    user_groups = user.groups.all()
    notes = Notes.objects.filter(group__in=user_groups)
    return render(request, 'group_notes.html', context={'notes': notes})


@login_required
def delete_note(request):
    if request.method == 'POST':
        note_id = request.POST["delete"]
        Notes.objects.get(id=note_id).delete()
        return redirect('/notesapp/usernotes/')
    return Http404


@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteCreateForm(request.POST)
        form.save()
        return redirect('/notesapp/usernotes/')
    else:
        user = request.user
        form = NoteCreateForm(initial={"author": user})
        return render(request, 'create_note.html', context={'form': form})


@login_required
def update_note(request):
    if request.method == 'POST':
        form = NoteUpdateForm(request.POST)
        if form.is_valid():
            note = Notes.objects.get(id=request.session['note_id'])
            note.title = form.cleaned_data['title']
            note.category = form.cleaned_data['category']
            note.text = form.cleaned_data['text']
            note.reminder = form.cleaned_data['reminder']
            note.save()
            return redirect('/notesapp/usernotes/')
    else:
        if request.method == "GET":
            note_id = request.GET["update"]
        else:
            note_id = request.session['note_id']
        note = Notes.objects.get(id=note_id)
        form = NoteUpdateForm(instance=note)
        request.session['note_id'] = note_id
        return render(request, 'update_note_form.html', context={'note': Notes.objects.filter(id=note_id),
                                                                 'form': form})


@api_view(['GET'])
@login_required
def get_audio_from_text(request):
    if request.method == "GET":
        note = Notes.objects.get(id=request.GET["sound_note"])
        if request.user == note.author:
            note_text = "..." + note.title + \
                        "..." + note.reminder.strftime("%B . %d . %Y . %I . %M . %p") + \
                        "..." + note.text
            path = TxtToAudioConverter().generate(note_text, note.id)
            file = open(path, "rb")
            return HttpResponse(content=file, content_type="audio/mpeg")
    return Http404()


@api_view(['POST'])
@login_required
def get_text_from_image(request):
    if request.method == "POST":
        image_with_text = request.FILES["image_with_text"].file
        tesseract_path = r'C:\Users\Vladislav\AppData\Local\Tesseract-OCR\tesseract.exe'
        note_text = ImgToTxtConverter(tesseract_path).run(image_with_text.read())
        return HttpResponse(content=note_text, content_type="text")
