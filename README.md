# MineHub

MineHub is a Django-based platform designed to develop a social connection for mining community. The platform allows users to connect with each other, create posts, and interact via a chatbot, which integrates mining regulations, news, and AI-powered features.

## Features
- **User Authentication**: Users can sign up, log in, and manage their profiles.
- **Post Creation**: Users can create posts with text, images, and multimedia content.
- **Chatbot Integration**: A chatbot is available to assist with inquiries, mining regulations, and news.
- **Cloud Storage**: Images and files are uploaded and stored in an AWS S3 bucket.

## Technologies Used
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Backend**: Django, Python
- **Database**: Relational Database (AWS RDS or local setup)
- **Storage**: AWS S3 for media files
- **Deployment**: AWS EC2 (Optional for cloud deployment)
- **AI Integration**: RAG Chatbot (fine-tuned on google/flan-t5-base), AWS Comprehend, AWS Rekognition
- **APIs**: Flask APIs for profanity and relevance check

## Installation

### Prerequisites
- Python 3.x
- Django 4.x
- PostgreSQL/MySQL (or SQLite for local development)
- AWS account (for S3 bucket and RDS setup)

### Steps to Install and Run Locally

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/saumysoni/minehub.git
   cd minehub
2. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Set Up AWS Credentials**:
   ```bash
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   AWS_STORAGE_BUCKET_NAME=your_s3_bucket_name

5. **Configure Database Settings**:
   
   In settings.py, set up your database configuration. For local development, you can use SQLite. For production, use PostgreSQL/MySQL.
6. **Apply Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
7. **Create a Superuser (for admin access)**:
    ```bash
    python manage.py createsuperuser
8. **Run the Development Server**:
    ```bash
    python manage.py runserver

## Application Interface

### Registration Page
![image](https://github.com/user-attachments/assets/20dc6370-eada-432b-83fa-7775a2dbaa5e)

### Login Page
![image](https://github.com/user-attachments/assets/92fa86e2-2b6a-4fb6-90d2-d8cd614fb4c7)

### Home Page
![image](https://github.com/user-attachments/assets/55794af7-9b5e-41bb-9dbc-eee8bf538ca6)

![image](https://github.com/user-attachments/assets/84e77431-b329-472b-a8f8-2a5766e39a33)
### Post Creation Page
![image](https://github.com/user-attachments/assets/5c246b29-aa77-49f4-a1e1-293d0e4fa45a)

### ChatBot
![image](https://github.com/user-attachments/assets/9d6a0465-9514-4721-a2aa-59c035f72947)

