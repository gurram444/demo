from .models import appointment
import datetime
from django.http import HttpResponse

def bookappointment(request):
    if request.session.has_key(username):
        hospital_name=request.post('hospital_name')
        doctor_name=request.post('doctor_name')
        time=request.post('time')
        bookappontment=appointment(hospital_name='hospital_name',doctor_name='doctor_name',time='time')
        bookappointment.save()
        appointment=appointment.objects.get(username=username)
        return render(userappointment.html,{'appointment':appointment})
    else:
        return redirect(userlogin.html)