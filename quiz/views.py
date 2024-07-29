from django.shortcuts import render, get_object_or_404, redirect
from quiz.models import Question, Choice, UserTestResult, UserAnswer, Test
from django.contrib.auth.decorators import login_required

import sweetify

# Create your views here.

def test_view(request):
    return render(request,'test.html')



@login_required
def quiz_single(request, qid):
    quests = Question.objects.all()
    quiz = get_object_or_404(quests, pk=qid)
    next_quiz = quests.filter(id__gt=qid).first()
    user = request.user

    # Ensure user have a UserTestResult
    test = quiz.test

    if qid == 1:
        # Delete previous UserTestResults for this user and test
        UserTestResult.objects.filter(user=user, test=test).delete()

        # Create a new UserTestResult for the new test attempt
        user_test_result = UserTestResult.objects.create(user=user, test=test)
        
        
        sweetify.toast(request, type='success', title='راهنما', text='برای شنیدن فایل صوتی راهنمای سوالات، بر روی علامت پخش صدا در بالا سمت چپ تصویر کلیک کنید.', timer=4000)
    else:
        user_test_result, created = UserTestResult.objects.get_or_create(user=user, test=test)

    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        if selected_choice_id:
            selected_choice = get_object_or_404(Choice, id=selected_choice_id)
            UserAnswer.objects.create(user_test_result=user_test_result, question=quiz, choice=selected_choice)
            if next_quiz:
                return redirect('quiz:single', qid=next_quiz.id)
            else:
                return redirect('quiz:result', result_id=user_test_result.id)
    
    choices = quiz.choices.all()
    content = {'quiz': quiz, 'next': next_quiz, 'all_quiz': quests.count(), 'number': list(quests).index(quiz) + 1, 'choices': choices, 'user_test_result': user_test_result}
    return render(request, 'quiz/quiz-single.html', content)

@login_required
def quiz_result(request, result_id):
    user_test_result = get_object_or_404(UserTestResult, id=result_id, user=request.user)
    answers = user_test_result.answers.all()

    analysis = {}
    for answer in answers:
        question_category = answer.question.category
        category_name = question_category.name
        if category_name not in analysis:
            analysis[category_name] = {
                'weights': [],
                'category': question_category
            }
        analysis[category_name]['weights'].append(answer.choice.weight)

    category_averages = {category: sum(data['weights']) for category, data in analysis.items()}

    context = {
        'user_test_result': user_test_result,
        'category_averages': category_averages,
        'analysis': analysis
    }

    return render(request, 'quiz/chart.html', context)

