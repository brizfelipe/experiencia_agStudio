from django import forms

class Question_forms(forms.Form):
    CHOICES_find_us = [
        ('option1', 'Facebook'),
        ('option2', 'Instagram'),
        ('option3', 'Indicação'),
        ('option4', 'Outros')
    ]
    CHOICES_location = [
        ('option1', 'Bem Localizado'),
        ('option2', 'Difício acesso'),
        ('option3', 'Falta sinalização'),
        ('option4', 'Outros')
    ]
    CHOICES_organizacao = [
        ('option1', 'Bem organizado e limpo'),
        ('option2', 'Não estava organizado quando fui'),
        ('option3', 'Achei o ambiente desorganizado e sujo'),
        ('option4', 'Outros')
    ]
    CHOICES_espera = [
        ('option1', 'Fui atendida bem rápido, não precisei esperar muito.'),
        ('option2', 'Infelizmente precisei aguardar por alguns minutos.'),
    ]
    
    CHOICES_atendimento = [
        ('option1', 'Minhas dúvidas foram esclarecidas'),
        ('option2', 'Fui orientada sobre todos os cuidados pós procedimento.'),
        ('option3', 'Fiquei confortável e me senti segura durante o procedimento.'),
        ('option4', 'Outros')
    ]
    CHOICES = [
        ('option1', ''),
        ('option2', ''),
        ('option3', ''),
        ('option4', '')
    ]
    CHOICES = [
        ('option1', ''),
        ('option2', ''),
        ('option3', ''),
        ('option4', '')
    ]


    find_us = forms.ChoiceField(
        label="Como você nos encontrou?",
        choices=CHOICES_find_us,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    location = forms.ChoiceField(
        label="Sobre nossa localização:",
        choices=CHOICES_location,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    organizacao = forms.ChoiceField(
        label="Sobre a organização do espaço:",
        choices=CHOICES_organizacao,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    espera = forms.ChoiceField(
        label="Tempo de espera:",
        choices=CHOICES_espera,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    atendimento = forms.ChoiceField(
        label="Sobre o atendimento:",
        choices=CHOICES_atendimento,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
