from .models import Product                                                                                 # Shu ilovadagi Product modelini import qiladi.
from django import forms                                                                                    # Django formalaridan foydalanish uchun forms modulini import qiladi.

class NewProductForm(forms.ModelForm):                                                                      # Product modeli bilan bog'langan yangi mahsulot formasini yaratadi.
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))                    # Bir nechta rasm tanlash imkoniga ega rasm maydonini belgilaydi.
    class Meta:                                                                                             # ModelForm uchun model va maydonlar sozlamalarini saqlaydi.
        model = Product                                                                                     # Forma Product modeli bilan ishlashini belgilaydi.
        fields = ('title', 'description', 'price', 'adress', 'category', 'phone_number', 'tg_username')     # Formada ko'rsatiladigan Product maydonlarini belgilaydi.

    def save(self, request, commit=True):
        product = self.instance
        product.author = request.user
        super().save(commit)
        return product


class ProductForm(forms.ModelForm):                                                                      
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))                    # 
    class Meta:                                                                                             # 
        model = Product                                                                                     # 
        fields = ('title', 'description', 'price', 'adress', 'category', 'phone_number', 'tg_username')     # 

