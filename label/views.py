import base64
from io import BytesIO, StringIO
from django.shortcuts import render
import pandas as pd

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
import datetime
from PIL import Image

def current_datetime(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    df = pd.read_excel(request.FILES['file'].read())
    df_new = df[['NAMA', 'ALAMAT', 'NOMER WA']]
    df_new.dropna(subset = ["NAMA"], inplace=True)
    df_new.rename(columns={'NOMER WA': 'WA'}, inplace=True)
    logo_file = request.FILES['logo']
    if logo_file.size > 2000000:
            return HttpResponseBadRequest()
    logo = Image.open(logo_file)
    output = BytesIO()
    logo.save(output, "PNG")
    print(output)
    contents = base64.b64encode(output.getvalue())
    return render(request, 'label.html', {
        'data': df_new, 
        'logo': contents.decode('utf-8'),
        'pengirim': request.POST['pengirim'],
        'alamat_pengirim': request.POST['alamat_pengirim'],
        'telepon_pengirim': request.POST['telepon_pengirim'],
    })