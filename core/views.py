from django.shortcuts import render
# core/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .run_model_1 import assess_keyword_clarity, get_intent_options

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, "index.html")

@csrf_exempt
def get_intents(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            keyword = data.get("word", "")
            print(" Received keyword:", keyword) 

            if assess_keyword_clarity(keyword):
                intents = [keyword] + get_intent_options(keyword)[:6]
            else:
                intents = get_intent_options(keyword)[:7]

            # Instead of calling Azure/OpenAI, I use dummy intents
            # intents = [
            #     f"Search info about {keyword}",
            #     f"Define {keyword}",
            #     f"Translate {keyword}",
            #     f"Use cases of {keyword}",
            #     f"Compare {keyword} with others",
            #     f"Examples of {keyword}",
            #     f"History of {keyword}"
            # ]


            return JsonResponse({"intents": intents})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)
