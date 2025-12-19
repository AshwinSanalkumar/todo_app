from django.shortcuts import render

# Create your views here.

 

def index(request):
    # Simple static list of tasks
    tasks = ["Learn Django", "Build a To-Do App", "Drink Coffee","WorkOut","Sleep"]
    return render(request, "index.html", {"tasks": tasks})

   