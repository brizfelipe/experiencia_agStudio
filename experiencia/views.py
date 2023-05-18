from django.shortcuts import render
from .forms import Question_forms
# Create your views here.
def form(request):
    context = {} 
    context['form'] = Question_forms()
    return render(request,'questionario/index.html',context)