from django.shortcuts import render
from .forms import Question_forms
from functions.database import insert_answer_to_questionnaire
from django.contrib import messages
from .models import Answers,Question
import pandas as pd

# Create your views here.
def form(request):
    context = {} 
    context['form'] = Question_forms()
    if request.method == 'POST':
        iter_items = iter(request.POST.items())
        next(iter_items)  # pula o primeiro item
        answers = {i: (int(v) if i == 'rate' else v) for i, v in iter_items}
        rate_depara = {1:"Péssimo",2:"Ruim",3:"Regular",4:"Bom",5:"Ótimo"}
        answers['rate'] = rate_depara[answers['rate']]

        if not insert_answer_to_questionnaire(answers):
            messages.error(request,"Ops! Algo deu errado. Por favor, tente novamente mais tarde. Desculpe pelo inconveniente!")
        else:
            if answers['rate'] == "Péssimo":
                msg = "Agradecemos pelo seu feedback. Vamos trabalhar duro para melhorar."
            elif answers['rate'] == "Ruim":
                msg = "Muito obrigado pela sua avaliação. Seus comentários nos ajudam a crescer."
            elif answers['rate'] == "Regular":
                msg = "Obrigado por nos avaliar. Valorizamos sua opinião e continuaremos a melhorar."
            elif answers['rate'] == "Bom":
                msg = "Apreciamos sua avaliação positiva. Estamos felizes em saber que você teve uma boa experiência conosco."
            elif answers['rate'] == "Ótimo":
                msg = "Uau! Obrigado pela avaliação incrível. Seu feedback nos motiva a continuar oferecendo um serviço excepcional."
            messages.success(request,msg)

    return render(request,'questionario/index.html',context)

def experiencia(request):
    context = {}
    context['cards'] = []
    
    # get the all values to Answer and questio db and make a join with pandas
    df_answer = pd.DataFrame.from_records(Answers.objects.filter().all().values())
    df_question = pd.DataFrame.from_records(Question.objects.filter().all().values())

    df = pd.merge(df_question,df_answer,left_on='id', right_on='question_id', how='inner')

    # get all question to make a for 
    for index,question in enumerate([q['question'] for q in list(Question.objects.all().values('question'))]):
        results = {}
        filter_df = df[(df['question'])==question]
        new_df = filter_df[['answer','results','percentage']]
        new_df['percentage'] = new_df['percentage'].astype(float)
        dict_new_df = new_df.to_dict('records')
        results['question'] = question
        results['values'] = dict_new_df
        results['div_id_question'] = f'question-id-{index}'
        results['div_id_progress'] = f'progres-bar-id-{index}'
        results['index'] = index

        context['cards'].append(results)
    return render(request,'perfil/index.html',context)
