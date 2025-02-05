import cv2         # OpenCV library for computer vision tasks
import threading   # Threading for running tasks concurrently
import playsound   # Library to play alarm sound
import smtplib     # Library to send email alerts

# Load the pre-trained fire detection cascade model
fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')

# Access the camera: "0" for built-in webcam, "1" for external camera
vid = cv2.VideoCapture(0)

# Boolean variable to ensure email is sent only once
runOnce = False

# Function to play alarm sound in a separate thread
def play_alarm_sound():
    playsound.playsound('fire_alarm.mp3', True)  # Play fire alarm sound (MP3 file)
    print("Fire alarm ended")  # Print message in the console after alarm ends

# Function to send email alert when fire is detected
def send_alert_email():
    recipient_email = "recipient_email@example.com"  # Replace with actual recipient's email
    recipient_email = recipient_email.lower()  # Convert email to lowercase
    
    try:
        # Set up the SMTP server for sending the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()  # Identify to the server
        server.starttls()  # Start TLS for security
        server.login("sender_email@example.com", 'your_password')  # Sender's email ID and password
        server.sendmail(
            'sender_email@example.com', recipient_email, 
            "Warning: Fire accident has been reported"
        )  # Send email with the message
        print(f"Alert email sent successfully to {recipient_email}")
        server.close()  # Close the SMTP server connection
    except Exception as e:
        print(f"Error: {e}")  # Print error message if email fails to send

# Main loop to continuously check for fire in the video stream
while True:
    ret, frame = vid.read()  # Read a frame from the video stream
    if not ret:
        break  # If frame not read successfully, exit loop
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale for better detection
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)  # Detect fire in the frame using the cascade classifier
    
    # Loop through detected fire regions in the frame
    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x-20, y-20), (x+w+20, y+h+20), (255, 0, 0), 2)  # Draw rectangle around detected fire
        
        print("Fire alarm initiated")
        
        # Start a new thread to play alarm sound
        threading.Thread(target=play_alarm_sound).start()

        # Ensure email is sent only once
        if not runOnce:
            print("Email alert initiated")
            threading.Thread(target=send_alert_email).start()  # Start a new thread to send email alert
            runOnce = True  # Set runOnce to True to prevent multiple emails

        if runOnce:
            print("Email alert has already been sent once")

    # Display the processed video frame with rectangles around fire
    cv2.imshow('Fire Detection', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
vid.release()
cv2.destroyAllWindows()
