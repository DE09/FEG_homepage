from django.shortcuts import render , redirect
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

# 회사소개 페이지
def intro(request):
    return render(request, 'intro/intro.html')

def history(request):
    return render(request, 'intro/history.html')

def ogchart(request):
    return render(request, 'intro/ogchart.html')

def sponsorship(request):
    return render(request, 'intro/sponsorship.html')

def access(request):
    return render(request, 'intro/access.html')

# 주요업무 페이지
def sea(request):
    return render(request, 'maintask/sea.html')

def air(request):
    return render(request, 'maintask/air.html')

def customs(request):
    return render(request, 'maintask/customs.html')

# fegsquare 페이지
def fegsquare(request):
    return render(request, 'fegsquare/fegsquare.html')

def inquiry(request):
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


            html = render_to_string('fegsquare/email.html',{
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
                        
            send_mail('문의사항이 도착했습니다.','This is the message','sales@familyexp.com',['sales@familyexp.com'],html_message=html)
            if request.POST['language'] == 'English' :
                messages = ' Thank you for getting in touch! Your enquiry has been passed on to a member of the team. We will respond to you as soon as possible.'
                context = {'messages': messages }
                return render(request, 'inquiry_eng.html', context)
            elif request.POST['language'] == 'Korean':
                messages = '문의사항이 접수되었습니다.'
                context = {'messages': messages }
                return render(request, 'fegsquare/inquiry.html', context)
            elif request.POST['language'] == 'Chinese' :
                messages = '感谢您的询价。'
                context = {'messages': messages }
                return render(request, 'fegsquare/inquiry_cn.html', context)
            else:
                messages = 'お問い合わせいただきありがとうございます。'
                context = {'messages': messages }
                return render(request, 'inquiry/inquiry_jp.html', context)

            context = {'messages': messages }
            return render(request, 'fegsquare/inquiry.html', context)

            # return render(request, 'fegsquare/inquiry.html')
            
    else:
        form = ContactForm()
        return render(request, 'fegsquare/inquiry.html', {
    'form':form
    })

def simfullo(request):
    return render(request, 'simfullo.html')

def travel(request):
    return render(request, 'travel.html')

