from django import forms


class DriverForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(label="Last name", min_length=2, max_length=100)
    phone_number = forms.CharField(label="Phone number", max_length=30)


class FarmerForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(label="Last name", min_length=2, max_length=100)
    street = forms.CharField(label="Street")
    zipcode = forms.CharField(label="Zipcode", max_length=10)
    house_no = forms.IntegerField(label="House number", min_value=1)
    house_suffix = forms.CharField(label="House number suffix", required=False)
    phone_number = forms.CharField(label="Phone number", max_length=30)
