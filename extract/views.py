from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    context={
        "text":"Hello, validition NID"
    }
    return render(request,"extract/index.html",context)



def government_name(gev_code):
    gev = {
        "01":"Cairo",
        "02":"Alexandria",
        "03":"Port Said",
        "04":"Suez",
        "11":"Damietta",
        "12":"Dakahlia",
        "13":"Sharqia",
        "14":"Qalyubia",
        "15":"Kafr El Sheikh",
        "16":"Gharbia",
        "17":"Monufia",
        "18":"Beheira",
        "19":"Ismailia",
        "21":"Giza",
        "22":"Beni Suef",
        "23":"Fayoum",
        "24":"Minya",
        "25":"Assiut",
        "26":"Sohag",
        "27":"Qena",
        "28":"Aswan",
        "29":"Luxor",
        "31":"Red Sea",
        "32":"New Valley",
        "33":"Matrouh",
        "34":"North Sinai",
        "35":"South Sinai",
        "88":"Outside the Republic",

        }
    return gev[gev_code] 

def valid_national_id(id):
    id_valid= False
    exctract_id_data={}
    # valid the Id is 14 digits and geverment listed
    if len(id)==14:
         if (int(id[7:9]) in range(1,28) or id[7:9] =="88" ):
            gev = government_name(id[7:9])
            # must strat with 2-> 19s or 3 ->2000s
            if id[0] in  ["2","3"]:
                id_valid =True
                year=int("19"+id[1:3]) if id[0]=="2" else int("20"+id[1:3]) 
                month=int(id[3:5])
                day=int(id[5:7])
                db = datetime(year,month,day)
                age = datetime.now().year -db.year
                gender = "female" if int(id[12])%2 ==0 else "male"

                exctract_id_data={
                    "date of birth " : db.strftime('%Y-%m-%d'),
                    "government" : gev,
                    "age" : age,
                    "gender":gender,
                
                }
                
    response_data = {
        "id_valid" : id_valid,
        "NID": id,
        "id_data":exctract_id_data
        
    }
            
    return  response_data



def validition(request):
    data= request.GET
    nid =data["nid"]
    response = valid_national_id(nid)
    context = {
        "valid_national_id":response
    }
    return render(request,"extract/validition.html",context)