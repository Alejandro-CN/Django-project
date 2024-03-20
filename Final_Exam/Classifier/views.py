from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .utils import predict_result


# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request, 'Classifier/home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


def classification(request):
    # Initialize empty list of sentences
    if 'sentence_results' not in request.session:
        request.session['sentence_results'] = []

    # Get input data from request
    if request.method == 'GET':
        input_text = request.GET.get('text')
        if input_text is not None:
            try:
                # Predict result
                predicted_label = predict_result(input_text)
                sentence_results = request.session['sentence_results']
                sentence_results.append({'sentence': input_text, 'result': predicted_label})
                request.session.modified = True
            except Exception as e:
                error = str(e)

    sentence_results = request.session.get('sentence_results', [])

    return render(request, 'Classifier/classification.html', {'sentence_results': sentence_results})


def cloud(request):
    return render(request, "Classifier/wordclouds.html")
