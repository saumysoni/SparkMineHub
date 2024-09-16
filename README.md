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
- **Database**: Relational Database (AWS RDS or local setup) and ChromaDB (For storing embeddings)
- **Storage**: AWS S3 for media files
- **Deployment**: AWS EC2 (Optional for cloud deployment)
- **AI Integration**: RAG Chatbot (fine-tuned on google/flan-t5-base), AWS Comprehend, AWS Rekognition
- **APIs**: Flask APIs for profanity and relevance check

## Installation

### Prerequisites
- Python 3.x
- Django 4.x
- PostgreSQL/MySQL (or SQLite for local development)
- AWS account (for S3 bucket, RDS setup, EC2, Sagemaker, Bedrock, Comprehend and Rekognition)

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

## Steps to setup APIs
1. **Create and Activate a Virtual Environment**:
   ```bash
   cd APIs
   python3 -m venv api_env
   source api_env/bin/activate  # On Windows use `api_env\Scripts\activate`

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Run the all 3 APIs using flask**:
    ```bash
    python API.py # This runs the explicit image check for images using AWS Rekognition
    python text_API.py # This runs the profanity check on the text data
    python text_relevence_API.py # This runs the text_relevence_API for which you will be required to make a AWS comprehend endpoint

4. **Test APIs**:
    ```bash
    python check.py # Change the URL to the API url and test the API using an Image on the S3
    python text_check.py # Change the URL to the text_API url 
    python text_relevence_check.py # Change the URL to the text_relevence_API url

## Steps to setup Chatbot
1. **Create and Activate a Virtual Environment**:
   ```bash
   cd Chatbot
   python3 -m venv chatbot_env
   source chatbot_env/bin/activate  # On Windows use `chatbot_env\Scripts\activate`

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Install Model**:
   ```bash
   git lfs install
   git clone https://huggingface.co/MBZUAI/LaMini-Flan-T5-783M

4. **Move the knowledge base PDFs to doc folder**:

5. **Run Chatbot using chainlit**:
   ```bash
   python embeddings.py
   chainlit run app.py # add --host: Specifies a different host to run the server on / --port: Specifies a different port to run the server on as required

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

## Future Improvements
- **Multi-Factor Authentication**: Adding an extra layer of security requiring users to verify their identity via OTP or authentication apps during registration and login.
- **Post Interaction**: Add reaction, comment, share, and report post functionality for improved user engagement.
- **Improved Chatbot**:
   - Introduce voice interaction for more natural communication with the chatbot.
   - Implement web scraping to automatically update the chatbot with fresh data from mining websites and news sources.
- **Market Place for miners**: A place where miners and companies come to buy and sell mining equipment


