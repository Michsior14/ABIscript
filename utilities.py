__author__='lataman'
import codecs, os

def fopen(filepath):
    lines=[]
    # print(filepath)
    bytes=min(32, os.path.getsize(filepath))
    raw=open(filepath, 'rb').read(bytes)
    f=None
    if raw.startswith(codecs.BOM_UTF8):
        # print("BOM")
        encoding='utf-8-sig'
        f=open(filepath, 'r', encoding = encoding)
    else:
        f=open(filepath, 'r', encoding = 'utf-8')

    lines=f.read()
    return lines

def hasValue(item):
    return (item!=None and item!='')

def isEmpty(item):
    return (hasValue(item) and len(item)<=0)
