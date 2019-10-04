from django import forms

from .models import Invoice


class LoginForm(forms.Form):
    pass

class InvoiceForm(forms.ModelForm):
    send_text = forms.BooleanField(label="Отправить краткий текст", required=False)
    send_full_text = forms.BooleanField(label="Отправить полный текст", required=False)
    class Meta:
        model = Invoice
        fields = ('text',
                  'full_text',
                  'image',
                  'departure_date',
                  'receive_date',
                  'send_text',
                  'send_full_text')
        widgets = {
            'departure_date': forms.DateTimeInput(attrs={'type': 'datetime', 'class': 'datetimepicker'}),
            'receive_date': forms.DateTimeInput(attrs={'type': 'datetime', 'class': 'datetimepicker'}),
        }