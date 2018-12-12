from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from database.forms import UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import Institutes, Subinstitutes, States, People, Groups, Papers
from .forms import *

def index(request):
    return render(request, 'base.html')

@login_required
def special(request):
    return HttpResponse(" Bienvenido !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('base'))

def base(request):
    Aguascalientes = States.objects.get(name = 'Aguascalientes')
    BajaCaliNort = States.objects.get(name = 'Baja California')
    BajaCaliSur = States.objects.get(name = 'Baja California Sur')
    Campeche = States.objects.get(name = 'Campeche')
    Chiapas = States.objects.get(name = 'Chiapas')
    Chihuahua = States.objects.get(name = 'Chihuahua')
    Colima = States.objects.get(name = 'Colima')
    Coahuila = States.objects.get(name = 'Coahuila')
    CiudadMX = States.objects.get(name = 'Ciudad de México')
    Durango = States.objects.get(name = 'Durango')
    Guanajuato = States.objects.get(name = 'Guanajuato')
    Guerrero = States.objects.get(name = 'Guerrero')
    Hidalgo = States.objects.get(name = 'Hidalgo')
    Jalisco = States.objects.get(name = 'Jalisco')
    EstadoMex = States.objects.get(name = 'Estado de México')
    Michoacan = States.objects.get(name = 'Michoacán')
    Morelos = States.objects.get(name = 'Morelos')
    Nayarit = States.objects.get(name = 'Nayarit')
    NuevoLeo = States.objects.get(name = 'Nuevo León')
    Oaxaca = States.objects.get(name = 'Oaxaca')
    Puebla = States.objects.get(name = 'Puebla')
    Queretaro = States.objects.get(name = 'Querétaro')
    QuintanaRoo = States.objects.get(name = 'Quintana Roo')
    SanLuisPotosi = States.objects.get(name = 'San Luis Potosí')
    Sinaloa = States.objects.get(name = 'Sinaloa')
    Sonora = States.objects.get(name = 'Sonora')
    Tabasco = States.objects.get(name = 'Tabasco')
    Tamaulipas = States.objects.get(name = 'Tamaulipas')
    Tlaxcala = States.objects.get(name = 'Tlaxcala')
    Veracruz = States.objects.get(name = 'Veracruz')
    Yucatan = States.objects.get(name = 'Yucatán')
    Zacatecas = States.objects.get(name = 'Zacatecas')
    return render(request, 'base.html', context={'Aguascalientes' : Aguascalientes,
    'BajaCaliNort' : BajaCaliNort, 'BajaCaliSur' : BajaCaliSur, 'Campeche' : Campeche,
    'Chiapas' : Chiapas, 'Chihuahua' : Chihuahua, 'Coahuila' : Coahuila, 'Colima' : Colima,
    'CiudadMX' : CiudadMX, 'Durango' : Durango, 'Guanajuato' : Guanajuato,
    'Guerrero' : Guerrero, 'Hidalgo' : Hidalgo, 'Jalisco' : Jalisco,
    'EstadoMex' : EstadoMex, 'Michoacan' : Michoacan, 'Morelos' : Morelos,
    'Nayarit' : Nayarit, 'NuevoLeo' : NuevoLeo, 'Oaxaca' : Oaxaca, 'Puebla' : Puebla,
    'Queretaro' : Queretaro, 'QuintanaRoo' : QuintanaRoo, 'SanLuisPotosi' : SanLuisPotosi,
    'Sinaloa' : Sinaloa, 'Sonora' : Sonora, 'Tabasco' : Tabasco, 'Tamaulipas' : Tamaulipas,
    'Tlaxcala' : Tlaxcala, 'Veracruz' : Veracruz, 'Yucatan' : Yucatan, 'Zacatecas' : Zacatecas})

def user_signup(request):
    registered = False
    institutes = Institutes.objects.all().order_by('name')
    subinstitues = Subinstitutes.objects.all().order_by('name')
    states = States.objects.all().order_by('name')
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            name = profile_form.cleaned_data.get('name')
            username_normalize = name.replace(' ','')
            email = profile_form.cleaned_data.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username_normalize, email, password)
            user.save()
            profile.user = user
            profile.url_name = username_normalize
            profile.save()
            registered = True
            user.is_active = False
            current_site = get_current_site(request)
            mail_subject = 'Activa tu cuenta de RENAIN'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':default_token_generator.make_token(user),
            })
            to_email = profile_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Se te ha enviado un correo de confirmación a tu correo para completar el registro')
        else:
            return HttpResponse(" Datos invalidos: " + str(profile_form.errors))
    else:
        profile_form = UserProfileInfoForm()
    return render(
        request, 'signup.html', context={'institutes':institutes, 'subinstitutes': subinstitues, 'states': states,})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user_ac = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user_ac = None
    if user_ac is not None and default_token_generator.check_token(user_ac, token):
        user_ac.is_active = True
        person = People.objects.get(user=user_ac)
        person_state = person.state
        state = States.objects.get(name=str(person_state))
        value_old = int(state.value)
        value_new = value_old + 1
        state.value = value_new
        state.save()
        user_ac.save()
        login(request, user_ac)
        return redirect(reverse('profile',args=(user_ac.username,)))
    else:
        return HttpResponse('El link de activación es inválido')

def user_profile(request):
    if request.method == 'POST':
        new_user_form = NewProfile(data=request.POST)
        if new_user_form.is_valid():
            new_user = new_user_form.save()
            new_user.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Ocurrio un error inesperado')
    else:
        return render(request, 'profile.html', {})


def user_login(request):
    if request.method == 'POST':
        email_request = request.POST.get('email')
        password = request.POST.get('password')
        try:
             person = People.objects.get(email=email_request)
        except:
            return HttpResponse(" Usuario no registrado")
        name_normalize = name.replace(' ','')
        user = authenticate(username=name_normalize, password=password)
        slug = name_normalize
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('profile',args=(slug,)))
            else:
                return HttpResponse(" Tu cuenta aun no esta activa ")
        else:
            print(" Datos incorrectos")
            print(" Email: {} Password: {}".format(
                email_request, password))
            return HttpResponse(" Ingresaste el password o nombre incorrectos")
    else:
        return render(request, 'login.html', {})

def email_reset(request):
    if request.method == 'POST':
        to_email = request.POST.get('email')
        try:
            user = User.objects.get(email = str(to_email))
            current_site = get_current_site(request)
            mail_subject = 'Petición cambio de contraseña RENAIN'
            message = render_to_string('change_pass_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':default_token_generator.make_token(user),
            })
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Se te ha enviado un correo para cambiar tu contraseña')
        except:
            return HttpResponse("Ingresaste un correo no registrado en el sistema")
    else:
        return render(request, 'password_reset.html', {})

def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password = request.POST.get('password')
            user.set_password(str(password))
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'changePassword.html', {})
    else:
        return HttpResponse('El link de activación es inválido')

def user_search(request):
    required = request.POST.get('entry')
    people = People.objects.filter(name__icontains=required)
    institutes = Institutes.objects.filter(name__icontains=required)
    subinstitutes = Subinstitutes.objects.filter(name__icontains=required)
    groups = Groups.objects.filter(name__icontains=required)
    papers = Papers.objects.filter(topic__icontains=required)
    return render(request, "search.html", context={'people':people, 'institutes':institutes, 'subinstitutes':subinstitutes, 'groups':groups, 'papers':papers,'required':required})

def paper_list(request):
    papers = Papers.objects.all()
    return render(request,'paper_list.html',{
    'papers':papers
    })

def upload_paper(request):
    if request.method == 'POST':
        form = PapersForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('paper_list')
    else:
        form = PapersForm()
    return render(request,'upload_paper.html',{
        'form': form
    })
