# OnlineLearningPlatform
This project is an online learning platform built using Django. The platform allows instructors to create courses and lessons, and students can enroll in these courses and track their progress. The project uses SQLite as its database.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **User Roles**: Users can register as either an instructor or a student.
- **Course Management**: Instructors can create, update, and delete courses.
- **Lesson Management**: Instructors can add lessons to their courses.
- **Enrollment**: Students can enroll in courses.
- **Progress Tracking**: Students can track their progress through a course based on lessons completed.
- **Interactive Dashboard**: Both instructors and students have personalized dashboards to manage their courses and progress.

## Images for the Student Portal

![o7](https://github.com/Syedz68/OnlineLearningPlatform/assets/107263740/6fcc4fdc-00e5-4067-b3d1-8bb282a1b160)
![o8](https://github.com/Syedz68/OnlineLearningPlatform/assets/107263740/5a900eef-3d5b-4ef1-97ab-b1aad37777f7)
![09](https://github.com/Syedz68/OnlineLearningPlatform/assets/107263740/63d1cc98-6be3-4222-a94f-3cbebd0e511a)

## Images for the Instructor Portal

![o1](https://github.com/Syedz68/OnlineLearningPlatform/assets/107263740/bbffb81b-b522-42c6-a0cf-e3c4e55f248f)
![o2](https://github.com/Syedz68/OnlineLearningPlatform/assets/107263740/92d8101f-abeb-4566-ac69-35b945eed3bf)
![o6](https://github.com/Syedz68/OnlineLearningPlatform/assets/107263740/4def7d57-bb22-43cf-b843-04c37806539f)
![o3](https://github.com/Syedz68/OnlineLearningPlatform/assets/107263740/7a16c40a-457a-438f-8543-34f00d9f311e)
![o4](https://github.com/Syedz68/OnlineLearningPlatform/assets/107263740/a7f87bf6-919c-4f67-983c-ba7739aa911f)
![05](https://github.com/Syedz68/OnlineLearningPlatform/assets/107263740/2ee662ba-3cc6-405b-b7d7-b8fc42b875bf)


## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Syedz68/onlinelearningplatform.git
    cd onlinelearningplatform
    ```

2. **Create a virtual environment:**

    ```bash
    python3.12 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000`.

## Requirements

- Python 3.12.4
- Django 5.0.6
- djangorestframework 3.14.0
- Pillow 10.3.0

