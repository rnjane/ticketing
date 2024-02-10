from django.forms import ModelForm, widgets

from dashboard.models import Ticket

class TicketForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['created_by', 'status']
        widgets = {
            'summary': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
        }
