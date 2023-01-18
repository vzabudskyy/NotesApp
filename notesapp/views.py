from django.shortcuts import render, redirect, Http404, HttpResponse
from notesapp.models import Notes
from notesapp.forms import NoteUpdateForm, NoteCreateForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from notesapp.text_to_speech import TxtToAudioConverter
from notesapp.image_to_text import ImgToTxtConverter
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class NoteView(LoginRequiredMixin, TemplateView):
    template_name = 'update_note_form.html'

    def get_context_data(self, **kwargs):
        note_id = kwargs.get('id')
        note = Notes.objects.get(id=note_id)
        form = NoteUpdateForm(instance=note)
        return {'note': Notes.objects.filter(id=note_id), 'form': form}

    def delete(self, request, *args, **kwargs):
        note_id = kwargs.get('id')
        Notes.objects.get(id=note_id).delete()
        return redirect('user_notes')

    def post(self, request, **kwargs):
        note_id = kwargs.get('id')
        form = NoteUpdateForm(request.POST)
        if not form.is_valid():
            # Тут взагалі треба видавати повідомлення про помилку.
            # Можна використати сигнали https://docs.djangoproject.com/en/4.1/topics/signals/
            return redirect('user_note')

        note = Notes.objects.get(id=note_id)
        note.title = form.cleaned_data['title']
        note.category = form.cleaned_data['category']
        note.text = form.cleaned_data['text']
        note.reminder = form.cleaned_data['reminder']
        note.save()
        return redirect('user_notes')


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
def create_note(request):
    if request.method == 'POST':
        form = NoteCreateForm(request.POST)
        form.save()
        return redirect('/notesapp/usernotes/')
    else:
        user = request.user
        form = NoteCreateForm(initial={"author": user})
        return render(request, 'create_note.html', context={'form': form})


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
