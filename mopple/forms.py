from django import forms
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(UserCreationForm):
    facebook_id = forms.CharField(max_length=50)
    phone_number = forms.CharField()
    is_male = forms.BooleanField()
    account_number = forms.CharField(max_length=20)
    account_bank = forms.CharField(max_length=10)
    balance = forms.IntegerField()
    sms_key = forms.CharField(max_length=4)

    def clean_sms_key(self):
        sms_key = self.cleaned_data.get('sms_key', '')

        if sms_key:
            if sms_key != '1234':
                raise forms.ValidationError('인증 번호를 다시 확인해주세요')
        return sms_key
