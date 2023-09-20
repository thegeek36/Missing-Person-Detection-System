from django.shortcuts import render,redirect
from .models import* 
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime
import face_recognition
import cv2
# Create your views here.
def home(request):
    return render(request,"index.html")

def detect(request):
    video_capture = cv2.VideoCapture(0)
    
    # Initialize a flag to track if a face has been detected in the current video stream
    face_detected = False
    
    while True:
        ret, frame = video_capture.read()
        
        # Find face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            # Compare detected face with stored face images
            for person in MissingPerson.objects.all():
                stored_image = face_recognition.load_image_file(person.image.path)
                stored_face_encoding = face_recognition.face_encodings(stored_image)[0]

                # Compare face encodings using a tolerance value
                #tolerance = 0.6  # Adjust this tolerance as needed
                matches = face_recognition.compare_faces([stored_face_encoding], face_encoding)

                if any(matches):
                    name = person.first_name + " " + person.last_name
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

                    # Check if a face has already been detected in this video stream
                    if not face_detected:
                        print("Hi " + name + " is found")
                        current_time = datetime.now().strftime('%d-%m-%Y %H:%M')
                        subject = 'Missing Person Found'
                        from_email = 'pptodo01@gmail'
                        recipientmail = person.email
                        context = {"first_name":person.first_name,"last_name":person.last_name,
                                    'fathers_name':person.father_name,"aadhar_number":person.aadhar_number,
                                    "missing_from":person.missing_from,"date_time":current_time,"location":"India"}
                        html_message = render_to_string('findemail.html',context = context)
                        # Send the email
                        send_mail(subject,'', from_email, [recipientmail], fail_silently=False, html_message=html_message)
                        face_detected = True  # Set the flag to True to indicate a face has been detected
                        break  # Break the loop once a match is found

        # Check if no face was detected in the current frame
        if not face_detected:
            name = "Unknown"
            #cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Camera Feed', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    video_capture.release()
    cv2.destroyAllWindows()
    return render(request, "surrivalence.html")

def surrivalence(request):
    return render(request,"surrivalence.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('fathers_name')
        date_of_birth = request.POST.get('dob')
        address = request.POST.get('address')
        phone_number = request.POST.get('phonenum')
        aadhar_number = request.POST.get('aadhar_number')
        missing_from = request.POST.get('missing_date')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        gender = request.POST.get('gender')
        aadhar = MissingPerson.objects.filter(aadhar_number=aadhar_number)
        if aadhar.exists():
            messages.info(request, 'Aadhar Number already exists')
            return redirect('/register')
        person = MissingPerson.objects.create(
            first_name = first_name,
            last_name = last_name,
            father_name = father_name,
            date_of_birth = date_of_birth,
            address = address,
            phone_number = phone_number,
            aadhar_number = aadhar_number,
            missing_from = missing_from,
            email = email,
            image = image,
            gender = gender,
        )
        person.save()
        messages.success(request,'Case Registered Successfully')
        current_time = datetime.now().strftime('%d-%m-%Y %H:%M')
        subject = 'Case Registered Successfully'
        from_email = 'pptodo01@gmail'
        recipientmail = person.email
        context = {"first_name":person.first_name,"last_name":person.last_name,
                    'fathers_name':person.father_name,"aadhar_number":person.aadhar_number,
                    "missing_from":person.missing_from,"date_time":current_time}
        html_message = render_to_string('regmail.html',context = context)
        # Send the email
        send_mail(subject,'', from_email, [recipientmail], fail_silently=False, html_message=html_message)

    return render(request,"register.html")