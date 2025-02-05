# Fire Detection Alert System

## Overview

The **Fire Detection Alert System** is a Python-based application that detects fire in real-time through the camera feed. Upon detecting fire, the system performs the following actions:

1. **Plays an alarm sound** to alert individuals nearby.
2. **Sends an email** to a specified recipient to inform them about the fire.

This system uses OpenCV for fire detection, threading for parallel execution of tasks, and smtplib to send email notifications.

---

## Features

- **Fire Detection**: The system uses a pre-trained fire detection model (`fire_detection_cascade_model.xml`) to identify fire in real-time camera feed.
- **Alarm Sound**: An audio file (`fire_alarm.mp3`) is played when fire is detected, providing an audible alert.
- **Email Alert**: An email is automatically sent to a predefined recipient to warn them about the fire.
- **Real-Time Processing**: The system continuously processes video frames to detect fire in real-time.
- **Threading**: Alarm sound and email sending run concurrently, ensuring the system is efficient.

---

## Prerequisites

- Python 3.x
- Libraries:
  - OpenCV (`opencv-python`)
  - playsound
  - smtplib (part of the standard Python library)

You can install the necessary libraries with the following commands:

```bash
pip install opencv-python playsound
```

---

## Setup

### 1. Clone the repository:
```bash
git clone https://github.com/FathimaSheerin/Fire-Detection-Alert-System.git
```

### 2. Add the required files:
- **fire_detection_cascade_model.xml**: This is a pre-trained model used for detecting fire in the camera feed. You can find or train your own fire detection model if needed.
- **fire_alarm.mp3**: This is the alarm sound that will play when a fire is detected. You can replace this with any other alarm sound file.
  
### 3. Configure Email:
Edit the `send_alert_email()` function with your actual email credentials and recipient email address:

```python
recipient_email = "recipient_email@example.com"
server.login("your_email@example.com", "your_password")
```

Make sure to replace these placeholders with your real email credentials.

---

## How It Works

1. **Start Camera**: The system accesses the camera using `cv2.VideoCapture(0)`. You can change the argument to "1" if you are using an external USB camera.
2. **Fire Detection**: The system continuously reads frames from the camera and processes them using the `fire_detection_cascade_model.xml`.
3. **Trigger Alarm**: If fire is detected, the system:
   - Draws a rectangle around the detected fire in the camera feed.
   - Plays the alarm sound using a background thread.
   - Sends an email alert to the recipient.
4. **Terminate**: Press 'q' to exit the application.

---

## Usage

1. Run the Python script:

```bash
python fire_detection_alert_system.py
```

2. The application will open a window showing the live video feed from the camera. If fire is detected, the following actions will occur:
   - A rectangle will be drawn around the detected fire in the video.
   - The alarm sound (`fire_alarm.mp3`) will play.
   - An email will be sent to the recipient.

3. To exit the application, press `q`.

---

## Files

- `fire_detection_alert_system.py`: Main script for fire detection, alarm sound, and email alert.
- `fire_detection_cascade_model.xml`: Pre-trained model for fire detection.
- `fire_alarm.mp3`: Audio file for alarm sound.

---

## Future Enhancements

- Integrate cloud-based alert systems like SMS or push notifications.
- Improve the fire detection accuracy with a more advanced model.
- Add logging features to track system alerts and errors.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
