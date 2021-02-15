from django.shortcuts import render
from visualapp.models import Tpm, Description
import pandas as pd

# Create your views here.
def mainView(request):
    des = Description.objects.all()
    treat_list = [x.treatment.split(',')[0] for x in des]
    tissue_list = [x.tissue for x in des]

    # query = request.GET.get("gene")
    # if str(query) == '':
    #     query = 'AT1G01010.1'
    # elif str(query) == 'None':
    #     query = 'AT1G01010.1'
    query = 'AT1G01010.1'
    gene_selected = Tpm.objects.filter(target_id=query)

    tpm_list = [x.tpm for x in gene_selected]
    tpm = tpm_list[0].split(',')

    data = [[x,y,z] for x,y,z in zip(tpm, treat_list, tissue_list)]
    df = pd.DataFrame(data, columns = ['tpm', 'treatment', 'tissue'])

    csv_files = []
    tissue_list_set = set(tissue_list)
    for x,y in zip(tissue_list_set, range(len(tissue_list_set))):
        m = df['tissue'] == x
        df_sort = df[m].sort_values(by=['treatment'])
        df_sort.to_csv('./visual_2app/static/%s.csv'%x, index=False)
        csv_files.append(x)
    print(csv_files)

    return_source = {
        'csv_files':csv_files,
        'query' : query,
        'tissue' : tissue_list_set
    }
    return render(request, 'visual_2app/main.html', return_source)