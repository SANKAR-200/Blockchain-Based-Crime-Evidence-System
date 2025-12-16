from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from datetime import date
import json
from web3 import Web3, HTTPProvider

global username
global contract, web3
global usersList, evidenceList

#function to call contract
def getContract():
    global contract, web3
    blockchain_address = 'http://127.0.0.1:9545'
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    compiled_contract_path = 'Evidence.json' #Evidence contract file
    deployed_contract_address = '0x8ee09176412Fe32B29e6E864a97f41CA097fe7C8' #contract address
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    file.close()
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
getContract()

def getUsersList():
    global usersList, contract
    usersList = []
    count = contract.functions.getUserCount().call()
    for i in range(0, count):
        user = contract.functions.getUsername(i).call()
        password = contract.functions.getPassword(i).call()
        phone = contract.functions.getPhone(i).call()
        email = contract.functions.getEmail(i).call()
        address = contract.functions.getStationaddress(i).call()
        usersList.append([user, password, phone, email, address])

def getEvidenceList():
    global evidenceList, contract
    evidenceList = []
    count = contract.functions.getEvidenceCount().call()
    for i in range(0, count):
        cid = contract.functions.getEvidenceid(i).call()
        officer = contract.functions.getOfficername(i).call()
        crime = contract.functions.getReportedcrime(i).call()
        details = contract.functions.getCrimedetails(i).call()
        evidence_details = contract.functions.getEvidencedetails(i).call()
        area = contract.functions.getCrimearea(i).call()
        witness = contract.functions.getWitnessname(i).call()
        witness_phone = contract.functions.getWitnesscontact(i).call()
        crime_date = contract.functions.getCrimedate(i).call()
        evidenceList.append([cid, officer, crime, details, evidence_details, area, witness, witness_phone, crime_date])
getUsersList()
getEvidenceList()

def ViewEvidence(request):
    if request.method == 'GET':
        global uname, evidenceList
        output='<table border=1 align=center width=100%><tr><th><font size="3" color="black">Evidence ID</th><th><font size="3" color="black">Investigating Officer</th>'
        output+='<th><font size="3" color="black">Reported Crime</th><th><font size="" color="black">Crime Details</th>'
        output+='<th><font size="3" color="black">Evidence Details</th><th><font size="3" color="black">Crime Area</th>'
        output+='<th><font size="3" color="black">Witness Name</th><th><font size="3" color="black">Witness Phone</th><th><font size="3" color="black">Crime Date</th>'
        output+='<th><font size="3" color="black">Evidence Image</th></tr>'
        output+='</tr>'
        for i in range(len(evidenceList)):
            elist = evidenceList[i]
            output+='<tr><td><font size="3" color="black">'+elist[0]+'</td><td><font size="3" color="black">'+str(elist[1])+'</td>'
            output+='<td><font size="3" color="black">'+elist[2]+'</td><td><font size="3" color="black">'+str(elist[3])+'</td>'
            output+='<td><font size="3" color="black">'+elist[4]+'</td>'
            output+='<td><font size="3" color="black">'+elist[5]+'</td>'
            output+='<td><font size="3" color="black">'+elist[6]+'</td>'
            output+='<td><font size="3" color="black">'+elist[7]+'</td>'
            output+='<td><font size="3" color="black">'+elist[8]+'</td>'
            output+='<td><img src="/static/files/'+elist[0]+'.png" width="200" height="200"></img></td>'
        output+= "</table></br></br></br></br>"        
        context= {'data':output}
        return render(request, 'AdminScreen.html', context)

def ViewOfficer(request):
    if request.method == 'GET':
        global uname, usersList
        output='<table border=1 align=center width=100%><tr><th><font size="3" color="black">Officer Name</th><th><font size="3" color="black">Password</th>'
        output+='<th><font size="3" color="black">Phone No</th><th><font size="" color="black">Email ID</th>'
        output+='<th><font size="3" color="black">Police Station Address</th>'
        output+='</tr>'
        for i in range(len(usersList)):
            ulist = usersList[i]
            output+='<tr><td><font size="3" color="black">'+ulist[0]+'</td><td><font size="3" color="black">'+str(ulist[1])+'</td>'
            output+='<td><font size="3" color="black">'+ulist[2]+'</td><td><font size="3" color="black">'+str(ulist[3])+'</td>'
            output+='<td><font size="3" color="black">'+ulist[4]+'</td></tr>' 
        output+= "</table></br></br></br></br>"        
        context= {'data':output}
        return render(request, 'AdminScreen.html', context)

def AccessEvidenceAction(request):
    if request.method == 'POST':
        global evidenceList
        eid = request.POST.get('t1', False)
        output='<table border=1 align=center width=100%><tr><th><font size="3" color="black">Evidence ID</th><th><font size="3" color="black">Investigating Officer</th>'
        output+='<th><font size="3" color="black">Reported Crime</th><th><font size="" color="black">Crime Details</th>'
        output+='<th><font size="3" color="black">Evidence Details</th><th><font size="3" color="black">Crime Area</th>'
        output+='<th><font size="3" color="black">Witness Name</th><th><font size="3" color="black">Witness Phone</th><th><font size="3" color="black">Crime Date</th>'
        output+='<th><font size="3" color="black">Evidence Image</th></tr>'
        output+='</tr>'
        for i in range(len(evidenceList)):
            elist = evidenceList[i]
            if elist[0] == eid:
                output+='<tr><td><font size="3" color="black">'+elist[0]+'</td><td><font size="3" color="black">'+str(elist[1])+'</td>'
                output+='<td><font size="3" color="black">'+elist[2]+'</td><td><font size="3" color="black">'+str(elist[3])+'</td>'
                output+='<td><font size="3" color="black">'+elist[4]+'</td>'
                output+='<td><font size="3" color="black">'+elist[5]+'</td>'
                output+='<td><font size="3" color="black">'+elist[6]+'</td>'
                output+='<td><font size="3" color="black">'+elist[7]+'</td>'
                output+='<td><font size="3" color="black">'+elist[8]+'</td>'
                output+='<td><img src="/static/files/'+elist[0]+'.png" width="200" height="200"></img></td>'
        output+= "</table></br></br></br></br>"        
        context= {'data':output}
        return render(request, 'OfficerScreen.html', context)

def AccessEvidence(request):
    if request.method == 'GET':
        global evidenceList
        output = '<tr><td><font size="3" color="black">Choose&nbsp;Evidence&nbsp;ID</td>'
        output += '<td><select name="t1">'
        for i in range(len(evidenceList)):
            elist = evidenceList[i]
            output += '<option value="'+elist[0]+'">'+elist[0]+'</option>'
        output +='</select></td></tr>'
        context= {'data1':output}
        return render(request, 'AccessEvidence.html', context)    

def AddEvidencesAction(request):
    if request.method == 'POST':
        global username, evidenceList
        eid = str(len(evidenceList) + 1)
        crime = request.POST.get('t1', False)
        crime_details = request.POST.get('t2', False)
        evidence = request.POST.get('t3', False)
        area = request.POST.get('t4', False)
        witness = request.POST.get('t5', False)
        witness_phone = request.POST.get('t6', False)
        crime_date = request.POST.get('t7', False)               
        image = request.FILES['t8']
              
        fs = FileSystemStorage()
        msg = contract.functions.createEvidence(eid, username, crime, crime_details, evidence, area, witness, witness_phone, crime_date).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(msg)
        if os.path.exists('EvidenceApp/static/files/'+eid+".png"):
            os.remove('EvidenceApp/static/files/'+eid+".png")
        filename = fs.save('EvidenceApp/static/files/'+eid+".png", image)
        evidenceList.append([eid, username, crime, crime_details, evidence, area, witness, witness_phone, crime_date])
        context= {'data':"Evidence & crome details saved in Blockchain with Evidence ID = "+eid+"<br/><br/>"+str(tx_receipt)}
        return render(request, 'AddEvidences.html', context)         

def AddEvidences(request):
    if request.method == 'GET':
       return render(request, 'AddEvidences.html', {})    
    
def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})    

def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})
    
def OfficerLogin(request):
    if request.method == 'GET':
       return render(request, 'OfficerLogin.html', {})

def AddOfficer(request):
    if request.method == 'GET':
       return render(request, 'AddOfficer.html', {})

def AddOfficerAction(request):
    if request.method == 'POST':
        global usersList
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        contact = request.POST.get('t3', False)
        email = request.POST.get('t4', False)
        address = request.POST.get('t5', False)
        count = contract.functions.getUserCount().call()
        status = "none"
        for i in range(0, count):
            user1 = contract.functions.getUsername(i).call()
            if username == user1:
                status = "exists"
                break
        if status == "none":
            msg = contract.functions.createUser(username, password, contact, email, address).transact()
            tx_receipt = web3.eth.waitForTransactionReceipt(msg)
            usersList.append([username, password, contact, email, address])
            context= {'data':'<font size="3" color="blue">New Officer Details added to Blockchain with below Block Details</font><br/><br/>'+str(tx_receipt)}
            return render(request, 'AddOfficer.html', context)
        else:
            context= {'data':'Given username already exists'}
            return render(request, 'AddOfficer.html', context)

def AdminLoginAction(request):
    if request.method == 'POST':
        global username, contract, usersList, usertype
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        status = "AdminLogin.html"
        output = 'Invalid login details'
        if username == "admin" and password == "admin":
            status = "AdminScreen.html"
            output = '<font size="3" color="blue">Welcome '+username+"</font>"                  
        context= {'data':output}
        return render(request, status, context)

def OfficerLoginAction(request):
    if request.method == 'POST':
        global username, contract, usersList
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        status = "OfficerLogin.html"
        output = 'Invalid login details'
        for i in range(len(usersList)):
            ulist = usersList[i]
            user1 = ulist[0]
            pass1 = ulist[1]
            if user1 == username and pass1 == password:
                status = "OfficerScreen.html"
                output = '<font size="3" color="blue">Welcome '+username+"</font>"
                break        
        context= {'data':output}
        return render(request, status, context)
    

