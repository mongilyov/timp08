from django.http import HttpResponse, JsonResponse
from solver import quadraticSolver

def index(request):
    return HttpResponse(f"Главная страница</h2>")



def user(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    (x1, x2) = quadraticSolver(int(a), int(b), int(c))
    if (x1 == "negative discriminant"):
        return JsonResponse({"x1": "Negative Discriminant", "x2": 0})
    return JsonResponse({"x1": x1, "x2": x2})