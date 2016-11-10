import numpy as np

from os import listdir
from os.path import isfile, join

from scipy.io import loadmat




meta_clsloc_file = "meta_clsloc.mat"


synsets = loadmat(meta_clsloc_file)["synsets"][0]

synsets_imagenet_sorted = sorted([(int(s[0]), str(s[1][0])) for s in synsets[:1000]],
                                 key=lambda v:v[1])

corr = {}
for j in range(1000):
    corr[synsets_imagenet_sorted[j][0]] = j

corr_inv = {}
for j in range(1,1001):
    corr_inv[corr[j]] = j

def depthfirstsearch(id, out=None):
    if out == None:
        out = []
    if type(id) == int:
        pass
    else:
        id = next(int(s[0]) for s in synsets if s[1][0] == id)
        
    out.append(id)
    children = synsets[id-1][5][0]
    for c in children:
        depthfirstsearch(int(c), out)
    return out
    
def synset_to_dfs_ids(synset):
    ids = [x for x in depthfirstsearch(synset) if x <= 1000]
    ids = [corr[x] for x in ids]
    return ids
    

def synset_to_id(synset):
    a = next((i for (i,s) in synsets if s == synset), None)
    return a


def id_to_synset(id):
    return str(synsets[corr_inv[id]-1][1][0])
    

def id_to_words(id):
    return synsets[corr_inv[id]-1][2][0]

def pprint_output(out, n_max_synsets=10):
    best_ids = out.argsort()[::-1][:10]
    for u in best_ids:
        print("%.2f"% round(100*out[u],2)+" : "+id_to_words(u))
