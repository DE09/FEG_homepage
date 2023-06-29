from django.shortcuts import render , redirect
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib import messages

def home_jp(request):
    return render(request, 'home_jp.html')

# 회사소개 페이지
def intro_jp(request):
    return render(request, 'intro_jp/intro.html')

def history_jp(request):
    return render(request, 'intro_jp/history.html')

def ogchart_jp(request):
    return render(request, 'intro_jp/ogchart.html')

def sponsorship_jp(request):
    return render(request, 'intro_jp/sponsorship.html')

def access_jp(request):
    return render(request, 'intro_jp/access.html')

# 주요업무 페이지
def sea_jp(request):
    return render(request, 'maintask_jp/sea.html')

def air_jp(request):
    return render(request, 'maintask_jp/air.html')

def customs_jp(request):
    return render(request, 'maintask_jp/customs.html')

# fegsquare 페이지
def corevalue_jp(request):
    return render(request, 'corevalue_jp/corevalue_jp.html')

def rational_price_jp(request):
    return render(request, 'corevalue_jp/rational_price_jp.html')


def simfullo_jp(request):
    return render(request, 'simfullo_jp.html')

def travel_jp(request):
    return render(request, 'travel_jp.html')

def inquiry_jp(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            company = form.cleaned_data['company']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            imex = form.cleaned_data['imex']
            incoterms = form.cleaned_data['incoterms']
            shippingmode = form.cleaned_data['shippingmode']


            
            html = render_to_string('inquiry/email.html',{
                
                'company' : company,
                'name':name,
                'email': email,
                'phone' : phone,
                'message' : message,
                'imex' : imex,
                'incoterms' : incoterms,
                'shippingmode' : shippingmode,


            })
            
            # email = EmailMessage(
            # 'Hello',                # 제목
            # 'Body goes here',       # 내용
            
            #  # 보내는 이메일 (settings에서 설정해서 작성안해도 됨)
            # to=['mkt@familexp.com'],  # 받는 이메일 리스트
            #         )
            # email.send()
                        
            send_mail('문의사항이 도착했습니다.','This is the message','sales@familyexp.com',['matthew@glsconsol.com'],html_message=html)
            messages.success(request,'문의사항이 성공적으로 접수되었습니다.')
            return render(request, 'inquiry/inquiry_jp.html')
            
    else:
        form = ContactForm()
        return render(request, 'inquiry/inquiry_jp.html', {
    'form':form
    })