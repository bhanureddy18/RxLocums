from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from rxApp.models import Hospital , Physician , Nurse ,  Contact , PhyFile , NurFile , NurFile , State, StateAssignment , HosFile
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import user_passes_test
from django.http import FileResponse , Http404
import os
from django.conf import settings


# Create your views here.


def download_file(request, file_path):
    print(f"File path: {file_path}")
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)
    print(f"File path: {file_path}")
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        raise Http404

def home(request):
    return render(request, 'index.html')

def hospitals(request):

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        resumes = request.FILES.getlist('resume')

        print(resumes)


        hospitalData = Hospital.objects.create(fullname=fullname, email=email, address=address, phone=phone, message=message)
        for resume_file in resumes:
                file_instance = HosFile.objects.create(file=resume_file)
                hospitalData.resumes.add(file_instance)

        messages.info(request, 'Your Request has been submitted successfully')
        return redirect('/hospitals')


    return render(request, 'hospital.html')

def nurses(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        resumes = request.FILES.getlist('resume')
        selectedStates = request.POST.get('selectedStates').split(',')

        print("===========================> " , selectedStates)
        if not selectedStates or selectedStates[0] == "":
            messages.error(request, 'Please select at least one state')
            return redirect('/physicians')


        nursesData = Nurse.objects.create(fullname=fullname, email=email, address=address, phone=phone, message=message)
        physician_content_type = ContentType.objects.get_for_model(Nurse)


        for state_name in selectedStates:
                state, created = State.objects.get_or_create(name=state_name)
                StateAssignment.objects.create(state=state, content_type=physician_content_type, object_id=nursesData.id)


        

        
        for resume_file in resumes:
                file_instance = NurFile.objects.create(file=resume_file)
                nursesData.resumes.add(file_instance)
       
        messages.info(request, 'Your Request has been submitted successfully')
        return redirect('/nurses')

    return render(request, 'nurse.html')
   


def physicians(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        resumes = request.FILES.getlist('resume')
        selectedStates = request.POST.get('selectedStates').split(',')

        print("===========================> " , selectedStates)
        if not selectedStates or selectedStates[0] == "":
            messages.error(request, 'Please select at least one state')
            return redirect('/physicians')


        physician = Physician.objects.create(fullname=fullname, email=email, address=address, phone=phone, message=message)
        physician_content_type = ContentType.objects.get_for_model(Physician)


        for state_name in selectedStates:
                state, created = State.objects.get_or_create(name=state_name)
                StateAssignment.objects.create(state=state, content_type=physician_content_type, object_id=physician.id)


        
        for resume_file in resumes:
                file_instance = PhyFile.objects.create(file=resume_file)
                physician.resumes.add(file_instance)

        messages.info(request, 'Your Request has been submitted successfully')
        return redirect('/physicians')

    return render(request, 'physician.html')

def contact(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')


        visa = Contact.objects.create(fullname=fullname, email=email,  phone=phone, message=message )
        visa.save()
        messages.info(request, 'Your Request has been submitted successfully')
        return redirect('/contact')
    return render(request, 'contact.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if user exists
        if(User.objects.filter(email=email_address).exists()):
            messages.info(request, 'Email is already taken')
            return redirect( '/register')

        # Check if password & confirm password are same if not then create user
        if(password != confirm_password):
            messages.info(request, 'Password & Confirm Password must be same')
            return redirect( '/register')
        else:
            user = User.objects.create_user(username=email_address, first_name=first_name, last_name=last_name, email=email_address)
            user.set_password(password)
            user.save()
            messages.info(request, 'Account Created Successfully')
            return redirect( '/login_page')
      
    return render(request, 'register.html')





def login_page(request):

    if request.method == 'POST':
        email_address = request.POST.get('email_address')
        password = request.POST.get('password')

        # Check if user exists
        if not User.objects.filter(username=email_address).exists():
            messages.info(request, 'No User Found')
            return redirect( '/login_page')


        user = authenticate(username=email_address, password=password)

        if user is None:
            messages.info(request, 'Invalid Credentials')
            return redirect( '/login_page')
        else:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_page') 
            else:
                return redirect('home')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('home')



#------------------------------------------------------------ADMIN PANEL------------------------------------------------------------

#-----------------------------------------------------Get all data from database-----------------------------------------------------

@login_required()
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    if request.method == 'GET':
        data = Hospital.objects.all()  
        return render(request, 'admin.html', {'hospitals': data})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_physician(request):
    if request.method == 'GET':
        data = Physician.objects.all() 
        return render(request, 'admin-physician.html',{'physicians': data})





@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_nurse(request):
     if request.method == 'GET':
        data = Nurse.objects.all()  
        print(data)
        return render(request, 'admin-nurse.html',{'nurses': data})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_contact(request):
    if request.method == 'GET':
        data = Contact.objects.all()  
        return render(request, 'admin-contact.html',{'contacts': data})



#-------------------------------------------------------- Get single data from database based on id --------------------------------------------


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_hospital_detail(request, id):
    if request.method == 'GET':
        data = Hospital.objects.get(id=id)
        return render(request, 'admin-hospital-detail.html', {'hospital': data})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_physician_detail(request, id):
    if request.method == 'GET':
        physician = Physician.objects.get(id=id)
        physician_content_type = ContentType.objects.get_for_model(physician)
        state_assignments = StateAssignment.objects.filter(content_type__pk=physician_content_type.id, object_id=physician.id)
        return render(request, 'admin-physician-detail.html', {'physician': physician, 'state_assignments': state_assignments})





@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_nurse_detail(request, id):
    if request.method == 'GET':
        nurse = Nurse.objects.get(id=id)
        nurse_content_type = ContentType.objects.get_for_model(nurse)
        state_assignments = StateAssignment.objects.filter(content_type__pk=nurse_content_type.id, object_id=nurse.id)
        return render(request, 'admin-nurse-detail.html', {'nurse': nurse, 'state_assignments': state_assignments})



@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_contact_detail(request, id):
    if request.method == 'GET':
        data = Contact.objects.get(id=id)
        return render(request, 'admin-contact-detail.html', {'contact': data})
