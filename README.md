# Learning Management System (LMS) Backend using Django

## Overview

This project is a Learning Management System (LMS) backend application built using Django, designed to facilitate online learning and course management. It provides features for managing courses, users, assignments, grades, and more.

## Features

- **Course Management:** Create, edit, and manage courses.
- **User Management:** Manage users, including students and instructors.
- **Quiz:** Allow students to take quizzes and automatically review them.
- **Resource Management:** Upload and manage course materials, such as documents and videos.

## URL Endpoints


### Authentication

- **Registration:** `api/v1/users/`
- **Login:** `api/v1/token/login/`
- **Logout:** `api/v1/token/logout/`


### Courses

- **Course categories List:** `api/v1/courses/get_categories/`
- **Courses List:** `api/v1/courses/`
- **Courses List (with category as query param):** `api/v1/courses/?category_id=<uuid:id>`
- **Get latest courses:** `api/v1/courses/latest/`
- **Create Course:** `api/v1/courses/create/`
- **Create Lesson:** `api/v1/courses/create-lesson/<course-slug>/`
- **Get author course:** `api/v1/courses/get_author_courses/<int:user_id>/`
- **Course detail lesson view:** `api/v1/courses/<course-slug>/`



### Activity

- **Get active courses:** `api/v1/activities/get_active_courses/`
- **Course track started:** `api/v1/activities/track_started/<slug:course_slug>/<slug:lesson_slug>/`
- **Course mark as done:** `api/v1/activities/mark_as_done/<slug:course_slug>/<slug:lesson_slug>/`


### Comments

- **Create Comment:** `api/v1/courses/<slug:course_slug>/<slug:lesson_slug>/`
- **Get comments:** `api/v1/courses/<slug:course_slug>/<slug:lesson_slug>/get-comments/`


### Quiz

- **Get quiz:** `api/v1/courses/<slug:course_slug>/<slug:lesson_slug>/get-quiz/`






## Installation

### Prerequisites

- Python 3.x
- Django

### Steps

1. Clone the repository:

```bash
git clone https://github.com/armshahs/lms_backend_django.git
```

2. Navigate to the project directory:

```bash
cd lms_backend_django
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

## Usage

1. Register for a new account or login if you already have one.
2. Create courses by navigating to the Courses section and adding course details.
3. View and complete course material as a student. Add comments on lessons if needed.
6. Upload course materials and resources for students.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/my-feature` or `git checkout -b bugfix/fix-issue`.
3. Make your changes and commit them: `git commit -am 'Add new feature'`.
4. Push to your branch: `git push origin feature/my-feature`.
5. Submit a pull request detailing your changes.
