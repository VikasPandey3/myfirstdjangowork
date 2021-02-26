from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from .models import Iot
from .serializers import IotSerializers
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model


def api_data(request, pk):
    try:
        snippet = Iot.objects.get(pk=pk)
    except Iot.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = IotSerializers(snippet)
        return JsonResponse(serializer.data)


def update(request, pk):
    t = Iot.objects.get(id=pk)
    pin = request.GET.get('pin')
    val = request.GET.get('state')
    t.state = val
    t.pin_no = pin
    if pin == '3':
        t.pin3 = val
    elif pin == '5':
        t.pin5 = val
    elif pin == '7':
        t.pin7 = val
    elif pin == '11':
        t.pin11 = val
    elif pin == '13':
        t.pin13 = val
    elif pin == '15':
        t.pin15 = val
    elif pin == '19':
        t.pin19 = val
    elif pin == '21':
        t.pin21 = val
    t.save()
    return redirect('/iotapp/main')


@cache_control(must_revalidate=True, no_store=True)
@login_required(login_url="/iotapp/Login")
def main(request):
    logged_in_user = request.user
    key = logged_in_user.api_key
    t = Iot.objects.get(id=key)
    dic = {'t': t, 'user': logged_in_user}
    return render(request, 'account/home.html', dic)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            f = Iot()
            y = get_user_model()
            f.id = y.objects.order_by('-id').first().api_key
            f.save()

            return redirect('/iotapp/Login')
        else:
            return HttpResponse("invalid credential<br>"
                                "Your password cant be too similar to your other personal information")
    else:
        form = CustomUserCreationForm
        args = {'form': form}
        return render(request, 'signup/index.html',args)


"""def signup_form(request):
    return render(request, 'signup/index.html')"""


def auth_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/iotapp/main')
            # Redirect to a success page.
        else:
            return HttpResponse("your account is disabled")
            # Return a 'disabled account' error message
    else:
        return render(request, 'Login/index.html', {'message': 'Invalid username or password'})
        # Return an 'invalid login' error message.


@cache_control(must_revalidate=True, no_store=True)
def login_form(request):
    return render(request, 'Login/index.html')
