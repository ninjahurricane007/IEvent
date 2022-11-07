from http import client
import datetime
from django.contrib import messages
from members.models import Profile
from django.shortcuts import redirect, render
from .models import Events,Registered,Fests,Payments
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
import razorpay
client = razorpay.Client(auth=(settings.KEY,settings.SECRET))
# Create your views here.


def welcome(request):
    return render(request,'welcome/index.html')

@login_required(login_url='/auth/login')
def fests(request):
    desc = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sapien finibus sapien nec ornare. Sed venenatis pulvinar enim at porttitor. Proin lectus justo, condimentum id ipsum ac, elementum laoreet elit. Nam odio dui, euismod ut lacinia ac, luctus vel dolor. Nulla facilisi. Nunc feugiat congue nisl, sed ultricies nibh varius non. Integer dapibus ultrices interdum.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sapien finibus sapien nec ornare. Sed venenatis."
    today_date = datetime.datetime.now()
    fests = Fests.objects.filter(fest_date__gte=today_date)
    context = {'fests':fests,'festdesc':desc}
    return render(request,'homepage/fests.html',context);

@login_required(login_url='/auth/login')
def addfest(request):
    if request.user.profile.isCordinator:
        if request.method=='POST':
            fest_name = request.POST.get('festname')
            fest_img = request.FILES.get('festimg')
            venue = request.POST.get('festvenue')
            desc = request.POST.get('festdesc')
            print(desc)
            fdate = request.POST.get('festdate')
            if(fest_name and fest_img and venue):
                Fests.objects.create(fest_name=fest_name,fest_venue=venue,fest_img=fest_img,fest_desc=desc,fest_author=request.user,fest_date=fdate)
            return redirect('/fests')
    else:
        return redirect('/fests');
    return render(request,'CreateFest/createfest.html');
    
def events(request,id):
    fest = Fests.objects.filter(pk=id).first()
    events = Events.objects.filter(event_fest=fest)
    
    return render(request,"Events/events.html",context={'events':events,'fest_poster':fest.fest_img})

def getyourevents(request):
    reg = Registered.objects.filter(user=request.user);
    context={
        'reg':reg
    }
    return render(request,'yourevents/yourevents.html',context)

def unregister(request,id):
    Registered.objects.filter(id=id).delete()
    return redirect('fests')

def regevent(request,id):
    event = Events.objects.filter(pk=id).first()
    print(event.id)
    tags = event.event_tags.split(',')
    context={
        'event':event,
        'tags':tags
    }
    return render(request,'registerpage/registerpage.html',context)

def checkout(request,id):

    eve=Events.objects.get(pk=id)
    userfest=Registered.objects.filter(user=request.user,event=eve)
    if len(userfest)!=0:
        messages.success(request,("Already registered for the event.."))
        return redirect('/fests')

    payment=None
    orderid=None
    event = Events.objects.filter(pk=id).first()
    amt=event.event_price
    action = request.GET.get('action')

    if action=="create_payment":
        if request.method=="POST":
            if(eve.event_price==0):
                Registered.objects.create(user=request.user,event=eve)
                messages.success(request,("Event registered successfully.."))
                return redirect('/fests')
            payment=client.order.create(data={'amount':amt*100,'currency':'INR','payment_capture':1})
            orderid = payment.get('id')
            pay = Payments(user=request.user,event=event,order_id=payment.get('id'))
            pay.save()

    context={
        'event':event,
        'payment':payment,
        'orderid':orderid
    }
    return render(request,'checkout/checkout.html',context)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def verify_payment(request):
    # event = Events.objects.filter(pk=id).first();
    if request.method=="POST":
        data=request.POST
        try:
            razor_pay_order_id = data['razorpay_order_id']
            razor_pay_payment_id = data['razorpay_payment_id']
            payment = Payments.objects.get(order_id=razor_pay_order_id)
            payment.payment_id = razor_pay_payment_id
            payment.status=True
            payment.save()

            print(razor_pay_order_id,"    ",razor_pay_payment_id)
            Registered.objects.create(user=payment.user,event=payment.event)
            messages.success(request,("Event registered successfully.."))
            return render(request,'paymentstatus/success.html')
        except:
            return render(request,'paymentstatus/fail.html')
    return redirect("/")

def eventcreate(request,id):
    if request.method=="POST":
        event_name = request.POST.get('evname')
        event_author = request.user
        event_img = request.FILES.get('evimg')
        event_tags = request.POST.get('evtag')
        event_desc = request.POST.get('evdesc')
        event_fest = Fests.objects.filter(pk=id).first()
        event_price = request.POST.get('evprice')
        event_prizepool = request.POST.get('evpool')
        event_team_size = request.POST.get('evteam')
        eve=Events(event_name=event_name,event_author=event_author,event_img=event_img,event_tags=event_tags,event_fest=event_fest,event_price=event_price,event_prizepool=event_prizepool,event_team_size=event_team_size,event_desc=event_desc)
        eve.save()
        return redirect("/cordinator")
    return render(request,'createevent/createevent.html')




def eventdelete(request,id):
    event = Events.objects.filter(id=id).delete()
    return redirect("/cordinator")

def festdelete(request,id):
    event = Fests.objects.filter(id=id).delete()
    return redirect("/cordinator")

@login_required(login_url='/auth/login')
def profile(request):
    all_data = User.objects.all()
    return render(request,"Profile/profile.html", {'key':all_data})

@login_required(login_url='/auth/login')
def editprofile(request):
    if request.method == 'POST':
        ph_num = request.POST.get('ph_num')
        clg_name = request.POST.get('clg_name')
        sem = request.POST.get('sem')
        brch = request.POST.get('brch')
        dp_img = request.FILES.get('dp_img')
        prof=Profile.objects.get(user=request.user)
        profile = Profile(ph_num=ph_num,clg_name=clg_name,sem=sem,brch=brch,dp_img=dp_img,user=request.user,isCordinator=prof.isCordinator)
        profile.save()
        return redirect('/profile')
    return render(request,'editprofile/editprofile.html')

from django.db.models import Count
def cordinator(request):
    reg1=None
    events = Events.objects.annotate(num_participants=Count('registered')).filter(event_author=request.user)
    fests=Fests.objects.filter(fest_author=request.user)
    reg=Registered.objects.filter(event__event_author=request.user)
    count_fest = len(fests)
    count_events = len(events)
    count_reg = len(reg)
    action = request.GET.get('action')
    if action=="filter_events":
        if request.method=="POST":
            idd = request.POST['event']
            reg = Registered.objects.filter(event__event_author=request.user,event__id=idd)
            if reg:
                reg1 = reg[0]
    
    context={ 'events':events, 'fests':fests, 'regis':reg,'count_fest':count_fest,'count_event':count_events,'count_reg':count_reg,'reg1':reg1}
    return render(request,'cordinator/coordinator.html',context)
