import pickle
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Tests,Question,UserResponse

@login_required
def rooms(request):
    rooms=Tests.objects.all()
    return render(request,'tests.html',{'rooms':rooms})

@login_required
def aptitude_test(request):
    if request.method == 'POST':
        # Clear previous responses
        UserResponse.objects.filter(user=request.user).delete()

        # Process the submitted answers
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])
                selected_option = value
                question = Question.objects.get(id=question_id)
                score = 1 if selected_option == question.correct_option else 0
                UserResponse.objects.create(
                    user=request.user,
                    question=question,
                    selected_option=selected_option,
                    score=score,
                    section=question.section
                )
        return redirect('results')
    else:
        logical_reasoning_questions = Question.objects.filter(section='logical_reasoning')
        numerical_ability_questions = Question.objects.filter(section='numerical_ability')
        verbal_ability_questions = Question.objects.filter(section='verbal_ability')
        context = {
            'logical_reasoning_questions': logical_reasoning_questions,
            'numerical_ability_questions': numerical_ability_questions,
            'verbal_ability_questions': verbal_ability_questions
        }
        return render(request, 'aptitude.html', context)

@login_required
def results(request):
    user_responses = UserResponse.objects.filter(user=request.user)
    logical_reasoning_score = sum(response.score for response in user_responses if response.section == 'logical_reasoning')
    numerical_ability_score = sum(response.score for response in user_responses if response.section == 'numerical_ability')
    verbal_ability_score = sum(response.score for response in user_responses if response.section == 'verbal_ability')

    # Load the model and predict the career path
    model_path = settings.BASE_DIR / 'career_model.pkl'
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    predicted_career = model.predict([[logical_reasoning_score, numerical_ability_score, verbal_ability_score]])

    return render(request, 'results.html', {'predicted_career': predicted_career[0]})