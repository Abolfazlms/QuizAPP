from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from quiz.models import Question

# Create your views here.
def test_view(request):
    quiz = Question.objects.all()
    context = {'quiz':quiz}
    return render(request,'test.html',context)

def quiz_single(request,qid):

    quests = Question.objects.all()
    quiz = get_object_or_404(quests,pk=qid)
    nextquiz = quests.filter(id__gt = qid).first()   

    content = {'quiz':quiz,'next':nextquiz,'all_quiz':quests.count(),'number':list(quests).index(quiz)+1}
    return render(request,'quiz/quiz-single.html',content)
