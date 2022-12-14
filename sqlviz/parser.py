# AUTOGENERATED! DO NOT EDIT! File to edit: ../02_parser.ipynb.

# %% auto 0
__all__ = ['parse_operations']

# %% ../02_parser.ipynb 3
from collections import defaultdict
from fastcore.test import *
from sqlglot import parse_one
from sqlglot.expressions import Expression
from .utils import *

# %% ../02_parser.ipynb 4
def parse_operations(sql:str) -> dict:
    
    "Given a query string, return a dictionary of parsed SQL operations."
    
    ops = defaultdict(lambda: list())
    
    ast = parse_one(sql)
    for exp in ast.walk():
        item, parent, key = exp
        if parent == ast:
            ops[key].append(item.sql())
    
    ops['select'] = ops['expressions']
    ops.pop('expressions')
    
    try: ops['limit'] = ops['limit'][0][6:]
    except: pass
    try: ops['from'] = ops['from'][0][5:]
    except: pass
    try: ops['joins'] = ops['joins']
    except: pass
    try: ops['where'] = ops['where'][0][6:]
    except: pass
    try: ops['group'] = ops['group'][0][9:]
    except: pass
    try: ops['having'] = ops['having'][0][7:]
    except: pass
    try: ops['order'] = ops['order'][0][9:]
    except: pass
    
    res = {}
    for k,v in ops.items():
        if v == []: pass
        else: res[k] = v
            
    res['_ops'] = list(res.keys())
    
    return res
