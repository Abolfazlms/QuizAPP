from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from quiz.models import Question, Choice, UserTestResult, UserAnswer, Test
from django.contrib.auth.decorators import login_required

import sweetify

# Create your views here.

def test_view(request):
    quiz = Question.objects.all()
    context = {'quiz':quiz}
    return render(request,'test.html',context)

# def quiz_single(request,qid):
    
#     quests = Question.objects.all()
#     quiz = get_object_or_404(quests,pk=qid)
#     nextquiz = quests.filter(id__gt = qid).first() 
#     if qid == 1 :  
#         sweetify.info(request, type='success',title='راهنما',text='برای شنیدن فایل صوتی راهنمای سوالات، بر روی علامت پخش موسیقی در بالا سمت راست تصویر کلیک کنید.', timer=4000)

#         if request.method == 'POST':
#             if request.POST.get('choice1'):
#                 quiz.choice = 1
#                 quiz.save()
#             if request.POST.get('choice2'):
#                 quiz.choice = 2
#                 quiz.save()
#             if request.POST.get('choice3'):
#                 quiz.choice = 3
#                 quiz.save()

#     content = {'quiz':quiz,'next':nextquiz,'all_quiz':quests.count(),'number':list(quests).index(quiz)+1}    
#     return render(request,'quiz/quiz-single.html',content)

@login_required
def quiz_single(request,qid):
    quests = Question.objects.all()
    quiz = get_object_or_404(quests,pk=qid)
    next_quiz = quests.filter(id__gt = qid).first()
    user = request.user

    #Ensure user have a UserTestResult
    test = quiz.test
    user_test_result, created = UserTestResult.objects.get_or_create(user=user, test=test)

    if qid == 1 :  
        sweetify.info(request, type='success',title='راهنما',text='برای شنیدن فایل صوتی راهنمای سوالات، بر روی علامت پخش موسیقی در بالا سمت راست تصویر کلیک کنید.', timer=4000)
    
    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        if selected_choice_id:
            selected_choice = get_object_or_404(Choice,id = selected_choice_id)
            UserAnswer.objects.create(user_test_result=user_test_result, question=quiz, choice=selected_choice)
            if next_quiz and selected_choice:
                return redirect('quiz:single', qid=next_quiz.id)
            else:
                return redirect('quiz:single', qid=quiz.id)
    choices = quiz.choices.all()
    content = {'quiz': quiz, 'next': next_quiz, 'all_quiz': quests.count(), 'number': list(quests).index(quiz) + 1, 'choices': choices,'user_test_result':user_test_result}
    return render(request, 'quiz/quiz-single.html', content)

@login_required
def quiz_result(request, result_id):
    user_test_result = get_object_or_404(UserTestResult, id=result_id, user=request.user)
    answers = user_test_result.answers.all()

    # تحلیل پاسخ‌ها بر اساس شاخص و روش تعریف شده
    analysis = {}
    for answer in answers:
        question_category = answer.question.category.name
        if question_category not in analysis:
            analysis[question_category] = []
        analysis[question_category].append(answer.choice.weight)

    # محاسبه میانگین برای هر دسته‌بندی
    category_averages = {category: sum(weights) for category, weights in analysis.items()}

    return render(request, 'quiz/test_result.html', {'user_test_result': user_test_result, 'category_averages': category_averages})
