from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from contacts.models import Contact, Message

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message)
        contact.save()

        send_mail(
            'Propert Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into admin panel for more info.',
            'aloneme0015@gmail.com',
            [realtor_email, 'rabin.maharjan0015@gmail.com'],
            fail_silently= False
        )
        messages.success(request,'Your request has been submitted,a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)


def landMessage(request):
     if request.method == 'POST':
        land_id = request.POST['land_id']
        land = request.POST['land']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        message = Message(land=land, land_id=land_id, name=name, email=email, phone=phone, message=message)
        message.save()

        send_mail(
            'Propert Listing Inquiry',
            'There has been an inquiry for ' + land + '. Sign into admin panel for more info.',
            'aloneme0015@gmail.com',
            [realtor_email, 'rabin.maharjan0015@gmail.com'],
            fail_silently= False
        )
        messages.success(request,'Your request has been submitted,a realtor will get back to you soon')
        return redirect('/lands/'+land_id)

    
