from django.shortcuts import render
from .models import Tpm, Description
import pandas as pd
import numpy as np
import json

def mainview(request):
    dic = {
    'Con' : 'Con',
    'Fusarium oxysporum' : 'F.oxysporum',
    'Hyaloperonospora arabidopsidis_Emoy2' : 'Emoy2',
    'Hyaloperonospora arabidopsidis_Waco9' : 'Waco9',
    'Plasmodiaphora brassicae' : 'P.brassicae',
    'Pseudomonas syringae effector_HopAM1' : 'HopAM1',
    'Pseudomonas syringae_pv.maculicola' : 'pv.maculicoal',
    'Sclerotinia sclerotiorum' : 'S.sclerotiorum',
    'Verticillium dahliae' : 'V.dahliae',
    'H2O' : 'H2O',
    }

    des = Description.objects.all()
    treat_list = [dic[x.treatment.split(',')[0]] for x in des]
    tissue_list = [x.tissue for x in des]
    dic = {}
    for x, y in zip(set(tissue_list), range(len(set(tissue_list)))):
        dic[x] = y
    print(dic)
    tissue_ix = list(map(lambda x : dic[x], tissue_list))
    query = request.GET.get("gene")
    
    if str(query) == '':
        query = 'AT1G01010.1'
    elif str(query) == 'None':
        query = 'AT1G01010.1'
    
    gene_selected = Tpm.objects.filter(target_id=query)

    tpm_list = [x.tpm for x in gene_selected]
    tpm = list(map(float, tpm_list[0].split(',')))


    # treat_tissue = [x+'/'+y for x,y in zip(treat_list, tissue_list)]

    data = [[x,y,z] for x,y,z in zip(tissue_list, treat_list, tpm)]
    df = pd.DataFrame(data, columns = ['x', 'Group', 'y'])
    # df_sort = df.sort_values(by=['tissue', 'treatment'])

    result = df.to_json(orient="records")
    parsed = json.loads(result)
    json_result = json.dumps(parsed, indent=1)

    # csv_file = '/static/output.csv'
    # df_sort.to_csv('./visualapp/static/output.csv', index=False)

    return_source = {
        'json' : json_result,
        'query' : query,
    }

    return render(request, 'visualapp/main.html', return_source)