bcgenes = input('Enter Gene Name: ')
import requests
import numpy as np
import pandas as pd
import json
#converting gene names to Ensembl ids
import mygene
mg = mygene.MyGeneInfo()
mgres = mg.querymany(bcgenes, scopes='symbol,alias',fields='ensembl.gene', species='human')
def drugtable(bcgenes):
    drugfields = ['target.gene_info.symbol',
                  'target.target_class',
                  'evidence.target2drug.action_type',
                  'disease.efo_info.label',
                  'unique_association_fields.chembl_molecules','disease.id',
                  'drug','id']
    payload = {"target":bcgenes,'datatype':['known_drug'],'fields':drugfields,'size':35}
    r = requests.post('https://platform-api.opentargets.io/v3/platform/public/evidence/filter',json=payload)

    for e in r.json()['data']:
        yield (e['target']['gene_info']['symbol'],
              e['target']['target_class'][0],
              e["unique_association_fields"]['chembl_molecules'],
              e['evidence']['target2drug']['action_type'],
              e['drug']['molecule_name'],
              e['drug']['molecule_type'],
              e['drug']["max_phase_for_all_diseases"]['numeric_index'],
              e['disease']['id'],
              e['disease']['efo_info']['label'],
              e['id'],
              )

bcgenes_ensg = []
bcgenes_ensg[:1]
for x in mgres:
    try:
        bcgenes_ensg.append(x['ensembl']['gene'])
    except KeyError:
        pass
    except TypeError:
        bcgenes_ensg.append(x['ensembl'][0]['gene'])

genes_chunked = [bcgenes_ensg[i:i + 60] for i in range(0, len(bcgenes_ensg), 60)]

cols = ['Target','Target Class','Chembl Uri','MOA','Molecule Name','Molecule Type','Phase','EFO','Indication','ID']

drugtable = pd.concat([pd.DataFrame(drugtable(g), columns=cols) for g in genes_chunked])
numrows = drugtable.head().shape[0]
import csv
fixbool = False
dfObj = pd.DataFrame(columns=['Target','Target Class','Chembl Uri','MOA','Molecule Name','Molecule Type','Phase','EFO','Indication','ID'])
#dfObj = drugtable.copy()
with open('efo_hp_tags.csv', 'r') as f:
    reader = csv.reader(f)
    list_of_EFOs = list(reader)
    #print(list_of_EFOs)
    for a in range(0, numrows):
        drugstring = drugtable.head().iloc[a,7]
        if any (drugstring in s for s in list_of_EFOs):
            print("success")
            fixbool = True
            dfObj = dfObj.append(drugtable.head().iloc[a,:], ignore_index = True)
            #print(drugtable.head().iloc[a,:])
            #drugtable.head().iloc[a,:].to_json(r'/Users/dauphin/Documents/kfile.json')
            #dfObj = pd.DataFrame(drugtable).set_index('Target')[a,:].copy(deep=True)
        else:
            print("Non-CVD")
            #dfObj.drop(a, axis = 0)
            #dfObj.head().drop([dfObj.iloc[a,:]])
            #a = a+1
            #numrows = numrows - 1
if fixbool == True:
    dfObj.head().to_json(r'/Users/dauphin/Documents/kfile.json')
