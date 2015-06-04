Sub ABI_OnLoad
	Dim cmd, cur, dtm, res, etm
	Dim NIPclient, NIPsaler, NIPbrutforce, InvoiceNumber
	dtm = Timer
	
	Set wshShell = CreateObject("WScript.Shell")
	cmd = "C:\Python34\python.exe E:\Skrypty\PyVer\main.py " & """" & allText & """"
	Set WshShellExec = WshShell.Exec(cmd)	
	strErrorOutput = WshShellExec.StdErr.ReadAll
	NIPclient = WshShellExec.StdOut.ReadLine()
	NIPsaler = WshShellExec.StdOut.ReadLine()
	NIPbrutforce = WshShellExec.StdOut.ReadLine()
	InvoiceNumber = WshShellExec.StdOut.ReadLine()

	etm = Timer
	res = etm - dtm
	EKOManager.StatusMessage("Time: " & res)
	EKOManager.StatusMessage("Time2: " & res2)
	EKOManager.StatusMessage("Errors: " & strErrorOutput)
	EKOManager.StatusMessage("NIP_client: " & NIPclient)
	EKOManager.StatusMessage("NIP_saler: " & NIPsaler)
	EKOManager.StatusMessage("NIP_bruteforce: " & NIPbrutforce)
	EKOManager.StatusMessage("InvoiceNumber: " & InvoiceNumber)
	
	Set KDocument = KnowledgeObject.GetFirstDocument
	If Not(KDocument Is Nothing) Then
		Set PTopic = KnowledgeObject.GetPersistenceTopic()
		Set Topic = KnowledgeContent.GetTopicInterface

		If Not(Topic Is Nothing) Then
			Topic.Replace "~USR::NIP_CLIENT~", NIPclient
			Topic.Replace "~USR::NIP_SALER~", NIPsaler
			Topic.Replace "~USR::NIP_BRUTEFORCE~", NIPbrutforce
			Topic.Replace "~USR::INVOCENUMBER~", InvoiceNumber
		Else
			KnowledgeObject.Status = 2 'KO_STATUS_BAD
			EKOManager.ErrorMessage("No Topic Found")
		End If
	Else
		KnowledgeObject.Status = 2 'KO_STATUS_BAD
		EKOManager.ErrorMessage("No KDocument Found")
	End If
End Sub

Sub ABI_OnUnload

End Sub
