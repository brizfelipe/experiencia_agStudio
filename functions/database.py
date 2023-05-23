from experiencia.models import Question, Answers
from django.db import transaction
import pandas as pd
import numpy as np

def insert_answer_to_questionnaire(answers):
    try:
        with transaction.atomic():
       
            for question,answer in answers.items():
                print('------------------------------------------------------------- // -------------------------------------------------------------')
                
                print(f'\npergunta:( {question} ) <- & -> Resposta: ( {answer} )')
                # atualizar results
                question_id = Question.objects.filter(field=question).get().id
                answer_obj = Answers.objects.filter(question=question_id,answer=answer)
                answer_id = answer_obj.get().id
                old_results = answer_obj.get().results
                new_results = 1 if old_results is None else old_results + 1    
                update_restuls_to_answer = answer_obj.first()
                update_restuls_to_answer.results = new_results
                update_restuls_to_answer.save()
                print(f"succes! -->results atualizado de {old_results} para {new_results}\n")
                
                # calcular porcentagem
                print(f"succes! -->calculando porcentagem...")
                questions_obj = Answers.objects.filter(question=question_id)
                df_questioins_obj = pd.DataFrame.from_records(questions_obj.values())
                df_questioins_obj['percentage'] = (df_questioins_obj['results'] /df_questioins_obj['results'].sum()) * 100
                if df_questioins_obj['percentage'].isna().all():
                    df_questioins_obj['percentage'].fillna(0)
                dict_questioins_obj = df_questioins_obj.to_dict('records')
                print(df_questioins_obj)
                
                # inserir nova porcentagem no banco
                for dict in dict_questioins_obj:
                    answer_db = Answers(**dict)
                    answer_db.save()
                print(f'succes! -->Resposta salva com sucesso\n\n')
            
            print('------------------------------------------------------------- // -------------------------------------------------------------')
            return True
    
    except Exception as e:
        print(f'ERROR! -->{e}\n\n')
        return False
    