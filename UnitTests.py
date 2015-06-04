__author__='lataman'

import unittest
import re
import main, regexReader, scheme, schemeContainer, utilities

class TestScheme(unittest.TestCase):

    def test_AddScheme(self):
        sch=scheme.createObject()
        sch.add("NIP", [re.compile("a|b|c")])
        sch.add("NIP", [re.compile("c|b")])
        print("AddScheme finished")
        self.assertTrue(utilities.hasValue(sch))


    def test_SimpleScheme(self):
        sch=scheme.createObject()
        sch.add("NIP", [re.compile("a|b|c")])
        sch.add("NIP", [re.compile("c|b")])
        alg=sch.getAlg("NIP")
        met=sch.getMethod("NIP")
        print("TestSimpleScheme finished")
        self.assertTrue(alg!=None)
        self.assertTrue(met!=None)

    def test_WrongGetScheme(self):
        sch=scheme.createObject()
        non1=sch.getMethod("UUU")
        non2=sch.getAlg("UUU")
        print("WrongGetScheme finished")
        self.assertTrue(non1==None)
        self.assertTrue(non2==None)


class schemeContainerTest(unittest.TestCase):
    def testConstructorSchemeContainer(self):
        self.assertTrue(schemeContainer.createObject("PL")!=None)
        print("ConstructorSchemeContainer finished")

    def testGetMethodContainer(self):
        container=schemeContainer.createObject("PL")
        self.assertTrue(container.getMethod("NIP_client")!=None)
        # print(container.getMethod("InvoiceNumber"))
        self.assertTrue(container.getMethod("NIP_saler")!=None)
        print("GetMethodContainer finished")


    def testSeekPattern(self):
        container=schemeContainer.createObject("PL")
        #tArray=utilities.fopen("E:\\Skrypty\\OutTxt\\1433376962.txt").split('\n')
        tArray=utilities.fopen("C:\\Users\\lataman\\Documents\\OCR\\1433376962.txt").split('\n')
        NIPclient=container.seekPattern("NIP_client", tArray)
        print("NIP_Client: "+str(NIPclient))
        NIPclient=container.seekPattern("NIP_saler", tArray)
        print("NIP_Saler: "+str(NIPclient))
        NIPclient=container.seekPattern("NIP_bruteforce", tArray)
        print("NIP_Bruteforce: "+str(NIPclient))
        NIPclient=container.seekPattern("InvoiceNumber", tArray)
        print("InvoiceNumber: "+str(NIPclient))

if __name__=='__main__':
    unittest.main()
