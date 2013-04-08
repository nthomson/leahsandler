# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from portfolio.models import Piece, Category

def index(request):
    caties = []
    cats = Category.objects.all()
    pieces = {}
    for cat in cats:
        pieces = Piece.objects.filter(category=cat)
        if pieces.count > 0:
            caties.append({
                'thumb': pieces[0].image,
                'title': cat.title,
                'pieces': pieces
            })
    return render(request, 'portfolio.html', {'categories': caties})
    
    
    
"""

[
    {
        title: "Paintings",
        thumb: {url: "http://..."},
        pieces: [{title: "self portrait", img: ...}],
    }
]


"""