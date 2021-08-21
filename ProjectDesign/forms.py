from django import forms
from .models import (Home,
                     Product,
                     )


# Home Model
class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__


# Home Model
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__

