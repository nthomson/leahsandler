# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from portfolio.models import Piece, Category

def index(request):
    cats = Category.objects.all()
    pieces = {}
    for cat in cats:
        pieces[cat.title] = Piece.objects.filter(category=cat)
    return render(request, 'index.html', {'categories': cats, 'cat_pieces': pieces})