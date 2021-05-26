from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def add(request):
    from random2  import randint

    num_1 = randint(1,10)
    num_2 = randint(1,10)

    if request.method == "POST":
        answer = request.POST["answer"]
        old_num_1 = request.POST["old_num_1"]
        old_num_2 = request.POST["old_num_2"]

        if not answer:
            my_ansewr = 'You forgot to fill out the form!'

            return render(request, 'add.html', {
            'my_ansewr': my_answer,
            'answer': answer,
            'num_1' : num_1,
            'num_2' : num_2,
            })

        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "correct " + old_num_1 + " + " + old_num_2 + " = " + answer
        else:
            my_answer = "incorrect " + old_num_1 + " + " + old_num_2 + " is not " + answer

        return render(request, 'add.html', {
        'answer': answer,
        'my_answer': my_answer,
        'num_1' : num_1,
        'num_2' : num_2,
        })

    return render(request, 'add.html', {
        'num_1' : num_1,
        'num_2' : num_2,
        })

def subtract(request):
    return render(request, 'subtract.html', {})

def multiply(request):
    return render(request, 'multiply.html', {})

def divide(request):
    return render(request, 'divide.html', {})
