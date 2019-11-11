from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Tu Nombre'} # en este widget le pasaremos un atributo class con el valor form-control
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="email", required=True,  widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Tu Email'} 
    ), min_length=3, max_length=100)
    content = forms.CharField(label="contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3, 'placeholder':'Escribe tu mensaje'} # POdemos añadir todos los atributos html permitidos 
    ), min_length=10, max_length=500) 