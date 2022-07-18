from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.views import View
# Create your views here.


class TradeIndex(View):
    def get(self, request):
        return render(request, 'trade/index.html')
