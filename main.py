import schemeContainer, sys

def runScript():
    
    container=schemeContainer.createObject("PL")
    allText=sys.argv[1].split('\n')
    
    NIPclient=container.seekPattern("NIP_client", allText)
    NIPsaler=container.seekPattern("NIP_saler", allText)
    NIPbruteforce=container.seekPattern("NIP_bruteforce", allText)
    InvoiceNumber=container.seekPattern("InvoiceNumber", allText)
    
    sys.stdout.write(str(NIPclient)+"\n")
    sys.stdout.write(str(NIPsaler)+"\n")
    sys.stdout.write(str(NIPbruteforce)+"\n")
    sys.stdout.write(str(InvoiceNumber)+"\n")
    sys.exit(0)

if __name__=="__main__":
    runScript()
