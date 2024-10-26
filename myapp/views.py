from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from dateutil import parser


def index(request):
    return render(request,'index.html')



def booking_view(request):
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        adults = request.POST.get('adults')
        children = request.POST.get('children')



        # Check if required fields are filled
        if not check_in or not check_out:
            messages.error(request, "Please enter both check-in and check-out dates.")
            return redirect('/')  # Redirect to the same page with an error

        try:
            # Use dateutil's parser to convert the date format
            check_in_date = parser.parse(check_in, dayfirst=True).date()  # Convert to date
            check_out_date = parser.parse(check_out, dayfirst=True).date()  # Convert to date

            # Save booking data if validation passes
            Booking.objects.create(
                check_in=check_in_date,
                check_out=check_out_date,
                adults=int(adults),
                children=int(children)
            )
            messages.success(request, "Booking successfully created!")
            return redirect('/')

        except ValueError:
            messages.error(request, "Invalid date format. Please use DD/MM/YYYY.")
            return redirect('/')

    return render(request, '/')