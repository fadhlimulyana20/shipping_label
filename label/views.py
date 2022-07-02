from django.shortcuts import render
import pandas as pd

# Create your views here.
from django.http import HttpResponse
import datetime

def current_datetime(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    df = pd.read_excel(request.FILES['file'].read())
    df_new = df[['NAMA', 'ALAMAT', 'NOMER WA']]
    df_new.dropna(subset = ["NAMA"], inplace=True)
    df_new.rename(columns={'NOMER WA': 'WA'}, inplace=True)
    return render(request, 'label.html', {'data': df_new})