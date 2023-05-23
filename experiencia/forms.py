from django import forms

class Question_forms(forms.Form):
    CHOICES_find_us = [
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Indicação', 'Indicação'),
        ('Outros', 'Outros')
    ]
    CHOICES_location = [
        ('Bem Localizado', 'Bem Localizado'),
        ('Difício acesso', 'Difício acesso'),
        ('Falta sinalização', 'Falta sinalização'),
        ('Outros', 'Outros')
    ]
    CHOICES_organizacao = [
        ('Bem organizado e limpo', 'Bem organizado e limpo'),
        ('Não estava organizado quando fui', 'Não estava organizado quando fui'),
        ('Achei o ambiente desorganizado e sujo', 'Achei o ambiente desorganizado e sujo'),
        ('Outros', 'Outros')
    ]
    CHOICES_espera = [
        ('Fui atendida bem rápido, não precisei esperar muito.', 'Fui atendida bem rápido, não precisei esperar muito.'),
        ('Infelizmente precisei aguardar por alguns minutos.', 'Infelizmente precisei aguardar por alguns minutos.'),
    ]
    
    CHOICES_atendimento = [
        ('Minhas dúvidas foram esclarecidas', 'Minhas dúvidas foram esclarecidas'),
        ('Fui orientada sobre todos os cuidados pós procedimento.', 'Fui orientada sobre todos os cuidados pós procedimento.'),
        ('Fiquei confortável e me senti segura durante o procedimento.', 'Fiquei confortável e me senti segura durante o procedimento.'),
        ('Outros', 'Outros')
    ]
    CHOICES_about_our_employees = [
        ('Muito boa! São simpáticas e trabalham super bem.', 'Muito boa! São simpáticas e trabalham super bem.'),
        ('Muitas conversas paralelas e não me senti confortável.', 'Muitas conversas paralelas e não me senti confortável.'),
    ]
    CHOICES_do_you_intend_to_return = [
        ('Com certeza!', 'Com certeza!'),
        ('Hum, acho que não.', 'Hum, acho que não.'),
        ('Assim que possível.', 'Assim que possível.'),
    ]

    how_you_find_us = forms.ChoiceField(
        label="Como você nos encontrou?",
        choices=CHOICES_find_us,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    about_our_location = forms.ChoiceField(
        label="Sobre nossa localização:",
        choices=CHOICES_location,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    About_organization_space = forms.ChoiceField(
        label="Sobre a organização do espaço:",
        choices=CHOICES_organizacao,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    waitin_time = forms.ChoiceField(
        label="Tempo de espera:",
        choices=CHOICES_espera,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    about_our_service = forms.ChoiceField(
        label="Sobre o atendimento:",
        choices=CHOICES_atendimento,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    about_our_employees = forms.ChoiceField(
        label="Como foi sua experiência com nossas funcionárias?",
        choices=CHOICES_about_our_employees,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    do_you_intend_to_return = forms.ChoiceField(
        label="Você pretende voltar?",
        choices=CHOICES_do_you_intend_to_return,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )

    # criticize_or_praise = models.CharField(max_length=500)
    # rate = models.IntegerField()