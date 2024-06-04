from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from quiz.models import Question

import sweetify

# Create your views here.

def test_view(request):
    quiz = Question.objects.all()
    context = {'quiz':quiz}
    return render(request,'test.html',context)

def quiz_single(request,qid):
    
    quests = Question.objects.all()
    quiz = get_object_or_404(quests,pk=qid)
    nextquiz = quests.filter(id__gt = qid).first() 
    if qid == 1 :  
        sweetify.info(request, type='success',title='راهنما',text='برای شنیدن فایل صوتی راهنمای سوالات، بر روی علامت پخش موسیقی در بالا سمت راست تصویر کلیک کنید.', timer=4000)

        if request.method == 'POST':
            if request.POST.get('choice1'):
                quiz.choice = 1
                quiz.save()
            if request.POST.get('choice2'):
                quiz.choice = 2
                quiz.save()
            if request.POST.get('choice3'):
                quiz.choice = 3
                quiz.save()

    content = {'quiz':quiz,'next':nextquiz,'all_quiz':quests.count(),'number':list(quests).index(quiz)+1}    
    return render(request,'quiz/quiz-single.html',content)



