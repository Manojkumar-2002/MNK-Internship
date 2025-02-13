from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io
from django.templatetags.static import static
from django.conf import settings
import base64


# Create your views here.

def index(request):
    experience_choices = Employee.EXPERIENCE_CHOICES
    if request.method == 'POST':
        try:
            
            full_name = request.POST.get('full_name','')
            email = request.POST.get('email','')
            phone = request.POST.get('phone','')
            position = request.POST.get('position', '')
            resume = request.FILES.get('resume', '')
            experience = request.POST.get('experience', '')
            emp = Employee.objects.create(full_name=full_name,email=email,phone=phone,position=position, experience=experience,resume=resume)
            messages.info(request,"Employee Created Successfully")

            return redirect('education',id = emp.id)
        except Exception as e:
            print(e)

    return render(request,'basic_details.html',{"experience_choices": experience_choices})

def education(request,id):
    if request.method == 'POST':
        if id:
            employee = Employee.objects.get(id=id)
            if hasattr(employee, 'education') and employee.education is not None:
                messages.info(request,"Eductaion Already Updated")
                return redirect('bank',id = id)
            
            highest_degree = request.POST.get('highest_degree','')
            university = request.POST.get('university','')
            graduation_year = request.POST.get('graduation_year','')
            graduation_year = int(graduation_year)
            specialization = request.POST.get('specialization','')
            percentage = request.POST.get('percentage','')
            percentage = float(percentage)
            education_proof = request.FILES.get('education_proof','')
            try:
                education = Education.objects.create(
                employee=employee,
                highest_degree=highest_degree,
                university=university,
                graduation_year=graduation_year,
                specialization=specialization,
                percentage = percentage,
                education_proof = education_proof
                )
                messages.info(request,"Eductaion Details Updated Successfully")
                return redirect('bank',id = id)
            except Exception as e:
                print(e)
        
    return render(request,'educational_details.html')

def bank(request, id):
    if request.method == 'POST':
        employee = Employee.objects.get(id=id)
        if hasattr(employee,'bank_details') and employee.bank_details is not None:
            messages.info(request,"Bank Details already Updated")
            return redirect('prev_emp',id = id)
        account_holder = request.POST.get('account_holder','')
        account_number = request.POST.get('account_number','')
        bank_name = request.POST.get('bank_name','')
        ifsc_code = request.POST.get('ifsc_code','')
        branch_name = request.POST.get('branch_name','')
        account_type = request.POST.get('account_type','')
        try:
            bank = BankDetails.objects.create(
            employee =employee,
            account_holder = account_holder,
            account_number = account_number,
            bank_name = bank_name,
            ifsc_code = ifsc_code,
            branch_name = branch_name,
            account_type = account_type
        )
            messages.info(request,"Bank Details entered successfully")
            if employee.experience.strip() == 'fresher' or employee.experience.strip() == 'Fresher':
                return render(request,'home.html',{'employee':employee})
            else:
                return redirect('prev_emp', id=id)
        except Exception as e:
            print(e)
    return render(request,'bank_details.html')

def prev_emp(request, id):
    if request.method == 'POST':
        if id:
            employee = Employee.objects.get(id=id)
            if hasattr(employee,'previous_employment') and employee.previous_employment is not None:
                messages.info(request,"Bank Details already Updated")
                return redirect('/',id = id)
            company_name = request.POST.get('company_name','')
            job_title = request.POST.get('job_title','')
            employment_duration = request.POST.get('employment_duration','')
            reason_for_leaving = request.POST.get('reason_for_leaving','')
            skills_acquired = request.POST.get('skills_acquired','')
            company_reference = request.POST.get('company_reference','')
            try:
                prev_emp = PreviousEmployment.objects.create(
                    employee = employee,
                    company_name= company_name,
                    job_title=job_title,
                    employment_duration= employment_duration,
                    reason_for_leaving = reason_for_leaving,
                    skills_acquired =skills_acquired,
                    company_reference =company_reference
                    )
                messages.info(request,"You have successfully filled all the forms")
                return redirect('home',id=id)
            except Exception as e:
                print(e)
        
    return render(request,'previous_employment_form.html')

def home(request,id):
    employee = Employee.objects.get(id=id)
    
    return render(request,'home.html',{'employee':employee})


def generate_employee_pdf(request, id):
    employee = Employee.objects.get(id=id)  
    resume_url = request.build_absolute_uri(employee.resume.url) if employee.resume else None
    proof_url = request.build_absolute_uri(employee.education.education_proof.url) if employee.education and employee.education.education_proof else None

    logo_path = request.build_absolute_uri(settings.STATIC_URL + 'images/mnk.png')
    sign_path = request.build_absolute_uri(settings.STATIC_URL + 'images/sign.png')
    template = get_template('employee_pdf.html')
  
    
    html = template.render({'employee': employee, 'resume_url': resume_url, 'proof_url': proof_url,'logo_path': logo_path,'sign_path':sign_path})  

  
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="employee_details.pdf"'
    
   
    pdf = io.BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf)

    if pisa_status.err:
        return HttpResponse('Error generating PDF', content_type='text/plain')

    response.write(pdf.getvalue())
    return response



