from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import *
import random


def quiz(request):
    context = {'category' : request.GET.get('category')}

    return render(request, 'quiz.html',context)

def get_quiz(request):
    try:
    
        question_objs = list(Question.objects.all())
        data =[]
        random.shuffle((question_objs))

        for question_obj in question_objs:
            
            data.append({
                "uid" : question_obj.uid,
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks" :   question_obj.marks,
                "answer": question_obj.get_answer(),
            })
        
        payload = {'status': True, 'data':data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong")
