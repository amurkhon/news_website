from django.forms import ModelForm
from .models import Contact, Comment

class ContactForm(ModelForm):

  class Meta:
    model = Contact
    fields = "__all__"

class CommentForm(ModelForm):
  
  class Meta:
    model = Comment
    fields = ['body']