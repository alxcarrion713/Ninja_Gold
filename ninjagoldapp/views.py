from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold']= 0
    if 'activity_log' not in request.session:
        request.session ['activity_log'] =[]
    request.session['activity_log'].reverse()
    request.session['activity_log']= request.session['activity_log'][:4]
    return render(request, "gold.html")

def process(request, location):
    print (request.POST)
    print(location)
    if request.POST['location']== 'farm':
        goldearned = random.randint(10,20)
        request.session['totalgold']+= goldearned
        event= f"Went to farm and earned: {goldearned}"
        request.session['activity_log'].append(event)

    elif request.POST['location']== 'cave':
        goldearned = random.randint(2,5)
        request.session['totalgold']+= goldearned
        event= f"Went to cave and earned: {goldearned}"
        request.session['activity_log'].append(event)
    
    elif request.POST['location']== 'house':
        goldearned = random.randint(5,10)
        request.session['totalgold']+= goldearned
        event= f"Went to house and earned: {goldearned}"
        request.session['activity_log'].append(event)

    elif request.POST['location']== 'casino':
        goldearned = random.randint(-50,50)
        request.session['totalgold']+= goldearned
        if goldearned >=0:
            event= f"Went to casino and earned: {goldearned}"
        else:
            event= f"Went to casino and lost: {abs(goldearned)}"
        request.session['activity_log'].append(event)

        

    return redirect("/")
