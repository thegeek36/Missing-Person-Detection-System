# 🕵️‍♂️ Bharatiya Rescue:Missing Person Detection System! 📸
Bharatiya Rescue is an innovative project aimed at leveraging cutting-edge technology to help reunite missing individuals with their loved ones. Our user-friendly system, built using Django, HTML, CSS, JavaScript, OpenCV, and the `facerecognition` library, combines a smooth UI with robust functionality to ensure an efficient and seamless experience for all users.

## How It Works
1. **Register a missing person complaint** with essential details like a recent photograph, name, address, Aadhar number, email, and mobile number.
2. **Surveillance mode**: The system uses facial recognition to detect the missing person's face. If a match is found, an email alert is automatically sent to the parents and the police.
3. **Location storage**: The system stores the missing person's last known location in a secure database.
4. **Admin management**: Admins can remove entries when the missing person is found, maintaining an up-to-date and efficient system.

## Future Enhancements
- Integration with advanced AI algorithms and machine learning models for improved face recognition accuracy.
- Use of geospatial technology for real-time tracking.
- Integration with social media and public alert systems to increase community response.
- Collaboration with law enforcement and technology innovators for continuous improvements.

## Other Developers
- Akash Mohanty
- Sarin Sahu


## Some Screenshorts:
<ul>
<li> Landing Page <br> <img src = "https://github.com/thegeek36/Missing-Person-Detection-System/assets/76440306/0e2f4438-5a1d-4428-aa09-28ba492e91e5"></img> </li>
  <li>Report Missing Case <br>
      <img src = "https://github.com/thegeek36/Missing-Person-Detection-System/assets/76440306/5ecd1289-d542-4eb2-b567-46fca0b60d18"></img>
      </li>
  <li> Face Detection <br> 
      <img src = "https://github.com/thegeek36/Missing-Person-Detection-System/assets/76440306/86b9e088-d699-4ab4-a053-aa6e328ddf1d"></img>
    </li>
  <li> Mail <BR>
    <img src = "https://github.com/thegeek36/Missing-Person-Detection-System/assets/76440306/7058fee9-80c3-4b8b-8841-558c5ed7c483"> </img>
        </li>
</ul>

## Getting Started
### Prerequisites
- Python 3.x
- `pip` (Python package installer)

### Clone the Repository
```bash
git clone https://github.com/thegeek36/Missing-Person-Detection-System.git
cd Missing-Person-Detection-System
```

### Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create a New Database
Delete the existing `db.sqlite3` file (if present):
```bash
rm db.sqlite3  # For Windows, use: del db.sqlite3
```

Create a new database:
```bash
python manage.py migrate
```

### Create Admin Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin username, email, and password.

### Run the Server
```bash
python manage.py runserver
```
Open your browser and navigate to `http://127.0.0.1:8000` to view the application.

### Important Note
Ensure to change the SMTP details in `core/core/settings.py` to enable the email alert functionality.

## Star the Repository
If you like the project, don't forget to star the repository!


