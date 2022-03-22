from django.shortcuts import render, redirect
from .models import *



# Create your views here.


def admin_log(request):
    return render(request, 'admin_log.html')

def admin_login(request):
    # try:
        if request.method == 'POST':
            if Admin_register.objects.filter(username = request.POST['username'], password = request.POST['password']).exists():
                member = Admin_register.objects.get(username = request.POST['username'], password = request.POST['password'])
                request.session['admid'] = member.reg_id
                
                return redirect('admin_dashboard')
            else:
                return redirect('admin_log')
        else:
            return redirect('admin_log')
    # except:
    #     return redirect('admin_log')
    
def admin_dashboard(request):
    admid = request.session['admid']
    adm = Admin_register.objects.filter(reg_id=admid)
    return render(request, 'admin_dashboard.html', {'adm':adm})