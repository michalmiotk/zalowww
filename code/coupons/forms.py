from django.forms import forms

class CouponApplyForm(forms.Form):
    code = forms.CharField()