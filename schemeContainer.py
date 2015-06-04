__author__='lataman'
import utilities, scheme
import re, copy


class schemeContainer(object):
    def __init__(self, lang):
        self.lang=lang
        #self.schemeList={"PL": "E:\\Skrypty\\PyVer\\standardRegex1.txt"}
        self.schemeList={"PL": "C:\\Users\\lataman\\Documents\\OCR\\PyVer\\ABIscript\\standardRegex1.txt"}

        self.setScheme(lang)


    def setScheme(self, lang):
        txtFile=utilities.fopen(self.schemeList[lang]).split('\n')
        currKey=""
        arrayReg=[]
        self.base=scheme.createObject()
        # print("setScheme")
        for line in txtFile:
            line=line.strip()
            takeKey=re.compile("^#([A-Z])\w+").search(line)
            if(utilities.hasValue((takeKey))):
                # print(takeKey.group())
                self.base.add(currKey, copy.deepcopy(arrayReg))
                currKey=takeKey.group().replace('#', '')
                arrayReg=[]
            else:
                arrayReg.append(copy.copy(line))
        # print(self.base.dict.keys())

    def getMethod(self, id):
        return self.base.getMethod(id)

    def getAlg(self, id, iter):
        return self.base.getAlg(id, iter)

    def seekPattern(self, id, textArray, seekFirstMatch = True):
        method=self.base.getMethod(id)
        matches=[]
        for alg in method:
            for pattern in alg:
                for line in textArray:
                    found=re.compile(pattern, flags = re.IGNORECASE).search(line)
                    if(utilities.hasValue(found)):
                        matches.append(found.group())
            # print(matches)
            # print("next alg")
            # print((seekFirstMatch and (utilities.isEmpty(matches))))
            if(seekFirstMatch and (not utilities.isEmpty(matches))):
                break
        return matches

def createObject(lang):
    return schemeContainer(lang)

