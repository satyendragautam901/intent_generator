from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, "index.html")

def get_intents(request): # this will call after generate button which accept data
    if request.method == "POST":
        data = json.loads(request.body)
        word = data.get("word", "")

        # Dummy intents 
        intents = [
            f"{word}_intent1",
            f"{word}_intent2",
            f"{word}_intent3",
            f"{word}_intent4",
            f"{word}_intent5",
            f"{word}_intent6",
            f"{word}_intent7",
        ]
        return JsonResponse({"intents": intents})