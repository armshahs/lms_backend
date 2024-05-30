# Learning Management System (LMS) Backend using Django

## Overview

This project is a Learning Management System (LMS) backend application built using Django, designed to facilitate online learning and course management. It provides features for managing courses, users, assignments, grades, and more.

## Features

- **Course Management:** Create, edit, and manage courses.
- **User Management:** Manage users, including students, instructors, and administrators.
- **Assignment Submission:** Allow students to submit assignments and instructors to review them.
- **Grading:** Assign grades to assignments and track student performance.
- **Resource Management:** Upload and manage course materials, such as documents and videos.
- **Discussion Forums:** Enable discussion forums for course-related discussions.

## URL Endpoints

### Authentication

- **Registration:** `/register/`
- **Login:** `/login/`
- **Logout:** `/logout/`

### Courses

- **Create Course:** `/course/create/`
- **Edit Course:** `/course/<course_id>/edit/`
- **Delete Course:** `/course/<course_id>/delete/`

### Users

- **Create User:** `/user/create/`
- **Edit User:** `/user/<user_id>/edit/`
- **Delete User:** `/user/<user_id>/delete/`

### Assignments

- **Create Assignment:** `/assignment/create/`
- **Edit Assignment:** `/assignment/<assignment_id>/edit/`
- **Delete Assignment:** `/assignment/<assignment_id>/delete/`

### Grades

- **Assign Grade:** `/grade/assign/`
- **Edit Grade:** `/grade/<grade_id>/edit/`
- **Delete Grade:** `/grade/<grade_id>/delete/`

### Resources

- **Upload Resource:** `/resource/upload/`
- **Edit Resource:** `/resource/<resource_id>/edit/`
- **Delete Resource:** `/resource/<resource_id>/delete/`

### Discussion Forums

- **Create Forum:** `/forum/create/`
- **Edit Forum:** `/forum/<forum_id>/edit/`
- **Delete Forum:** `/forum/<forum_id>/delete/`


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
3. Enroll users in courses as students or instructors.
4. Create assignments and set deadlines for submission.
5. Grade assignments submitted by students and provide feedback.
6. Upload course materials and resources for students.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/my-feature` or `git checkout -b bugfix/fix-issue`.
3. Make your changes and commit them: `git commit -am 'Add new feature'`.
4. Push to your branch: `git push origin feature/my-feature`.
5. Submit a pull request detailing your changes.
