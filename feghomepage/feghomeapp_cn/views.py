from django.shortcuts import render , redirect
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib import messages


# # 회사소개 페이지

# def intro_cn(request):
#     return render(request, 'intro/intro_cn.html')

# def history_cn(request):
#     return render(request, 'intro/history_cn.html')

# def ogchart_cn(request):
#     return render(request, 'intro/ogchart_cn.html')

# # 주요업무 페이지

# Create your views here.
def home_cn(request):
    return render(request, 'home_cn.html')

# 회사소개 페이지
def intro_cn(request):
    return render(request, 'intro/intro_cn.html')

def history_cn(request):
    return render(request, 'intro/history_cn.html')

def ogchart_cn(request):
    return render(request, 'intro/ogchart_cn.html')

def sponsorship_cn(request):
    return render(request, 'intro/sponsorship_cn.html')

def access_cn(request):
    return render(request, 'intro/access_cn.html')

# 주요업무 페이지
def sea_cn(request):
    return render(request, 'maintask/sea_cn.html')

def air_cn(request):
    return render(request, 'maintask/air_cn.html')


# fegsquare 페이지

def inquiry_cn(request):
    return render(request, 'fegsquare/inquiry_cn.html')
def price_cn(request):
    return render(request, 'fegsquare/price_cn.html')
def service_cn(request):
    return render(request, 'fegsquare/service_cn.html')

# def inquiry_cn(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
        
#         if form.is_valid():
#             company = form.cleaned_data['company']
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']
#             message = form.cleaned_data['message']
#             imex = form.cleaned_data['imex']
#             incoterms = form.cleaned_data['incoterms']
#             shippingmode = form.cleaned_data['shippingmode']


            
#             html = render_to_string('fegsquare/email.html',{
                
#                 'company' : company,
#                 'name':name,
#                 'email': email,
#                 'phone' : phone,
#                 'message' : message,
#                 'imex' : imex,
#                 'incoterms' : incoterms,
#                 'shippingmode' : shippingmode,


#             })
            
#             # email = EmailMessage(
#             # 'Hello',                # 제목
#             # 'Body goes here',       # 내용
            
#             #  # 보내는 이메일 (settings에서 설정해서 작성안해도 됨)
#             # to=['mkt@familexp.com'],  # 받는 이메일 리스트
#             #         )
#             # email.send()
                        
#             send_mail('문의사항이 도착했습니다.','This is the message','sales@familyexp.com',['matthew@glsconsol.com'],html_message=html)
#             messages.success(request,'문의사항이 성공적으로 접수되었습니다.')
#             return render(request, 'fegsquare/inquiry_cn.html')
            
#     else:
#         form = ContactForm()
#         return render(request, 'fegsquare/inquiry_cn.html', {
#     'form':form
#     })

def simfullo_cn(request):
    return render(request, 'simfullo_cn.html')

def travel_cn(request):
    return render(request, 'travel_cn.html')






