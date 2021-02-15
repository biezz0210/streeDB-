from django.shortcuts import render
from .models import Tpm, Description
import pandas as pd
import numpy as np

def mainview(request):

    des = Description.objects.all()
    treat_list = [x.treatment.split(',')[0] for x in des]
    tissue_list = [x.tissue for x in des]

    query = request.GET.get("gene")
    if str(query) == '':
        query = 'AT1G01010.1'
    elif str(query) == 'None':
        query = 'AT1G01010.1'
    
    gene_selected = Tpm.objects.filter(target_id=query)

    tpm_list = [x.tpm for x in gene_selected]
    tpm = tpm_list[0].split(',')

    treat_tissue = [x+'/'+y for x,y in zip(treat_list, tissue_list)]

    data = [[x,y,z] for x,y,z in zip(tpm, treat_tissue, tissue_list)]
    df = pd.DataFrame(data, columns = ['tpm', 'treatment', 'tissue'])
    df_sort = df.sort_values(by=['tissue', 'treatment'])
    csv_file = '/static/output.csv'
    df_sort.to_csv('./visualapp/static/output.csv', index=False)

    return_source = {
        'csv_file':csv_file,
        'query' : query,
    }

    return render(request, 'visualapp/main.html', return_source)