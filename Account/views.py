from django.shortcuts import render

# Create your views here.


def account(request):
    resp = render(request, 'index.html')
    return resp

def account_details(request):
    
    account_holders = [
        {"name":"Sonam","accountNo":978496,"age":25,"mobile":7649834,"adress":"Delhi"},
        {"name":"Nidhi","accountNo":87008865,"age":28,"mobile":7876834,"adress":"Noida"},
        {"name":"Sona","accountNo":98794035,"age":22,"mobile":925783,"adress":"Kanpur"}
    ]
    
    return render(request,'acountDetails.html',context= {"ah":account_holders})