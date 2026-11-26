import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen4 import T
import os
out=os.path.join(os.path.dirname(__file__), '..', '..', 'i18n', 'locales')
LANGS=sys.argv[1:] or ['it','en']
for idx,code in enumerate(['it','en','fr','de']):
    if code not in LANGS: continue
    tree={}
    for k,v in T.items():
        val=v[idx]
        if val=='' and k not in ('hero.h1b',) and code!='it' and idx>1: continue  # chiavi ancora da tradurre: niente voce (fallback)
        node=tree; parts=k.split('.')
        for p in parts[:-1]: node=node.setdefault(p,{})
        node[parts[-1]]=val
    json.dump(tree,open(f'{out}/{code}.json','w'),ensure_ascii=False,indent=1)
    print(code,len(T))
