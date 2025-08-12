# Transcript_Vault

## Table of Contents
- [Project Introduction](#project-introduction)
- [Part 1 - Idea & Planning Phase](#part-1---idea--planning-phase)
- [Part 2 - Design Phase (ER Diagram)](#part-2---design-phase-er-diagram)
- [Part 3 - Start Building (Development Phase Begins)](#part-3---start-building-development-phase-begins)
- [Part 4 - Development Phase Continues](#part-4---development-phase-continues)
- [Part 5 - Polish, Test & User Review](#part-5---polish-test--user-review)
- [Part 6 - Feedback Implementation](#part-6---feedback-implementation)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Project Timeline](#project-timeline)

---

## Project Introduction 
Many universities face delays, manual processes, and long queues when students request access to their academic transcripts. **Transcript_Vault** aims to solve this problem by providing a **secure, digital backend system** for transcript management.

With **Transcript_Vault**:
- Staff can upload and manage academic records per student, semester, and course.
- Students can securely log in and view their transcripts in real time.
- The platform ensures accuracy, reduces waiting time, and eliminates the need for paper-based requests.

---

## Part 1 - Idea & Planning Phase
The first phase focuses on clearly defining the problem and mapping out a solution. 
The idea for Transcript_Vault came from recognizing the need for a digital, efficient, and secure transcript management system. In this stage, the project scope, core features, Django app structure, and database design were planned, along with a simple weekly development roadmap.


## Main Features
  - User Authentication: Only authorized users can log in to upload or manage transcripts.
  - Student Account Access: Students can log in securely to view their academic records.
  - Student Profile Management: Admins can add and manage student data such as name, index number, program, and level.
  - Course Management: Admins can add courses with titles, codes, and credit hours for various programs.
  - Grade Entry: Admins can upload grades for students per course, semester, and academic year.
  - Transcript Viewing: Students can view their academic transcript grouped by semester or level.
  - Export transcript as a clean, readable PDF using a PDF generation tool.

## API 
 A PDF generation library [WeasyPrint](https://weasyprint.org/) will be used for exporting transcripts in PDF format..

## Models
- User (extend Django's AbstractUser)
- Student
- Course
- Grade

## Timeline (5-Week Plan)
Week          <>  Task
- Week 1    - Choose Project, outline features, models, and API endpoints 
- Week 2    - Draw (Entity Relationship Diagram) showing models and how they relate
- Week 3    - Set up Django project, create models, Add authentication
- Week 4    - Build APIs for students, courses, and grades; add transcript logic
- Week 5    - Final testing, optional PDF export, documentation, Project Submission


---


## Part 2 - Design Phase (ER Diagram)
The design phase involves creating an Entity Relationship Diagram (ERD) to map out the data flow and structure of the system. 

  ### Objective
  To design the Entity Relationship Diagram (ERD) for Transcript_Vault, mapping out the main entities, their attributes, and relationships to      guide database implementation in Django.

  ## Entities and Attributes
  ### User (Stores authentication details for all system users, including students and administrative staff.)
    - id (PK)
    - username
    - email
    - password
    - is_staff (Boolean: True for admin, False for student)
    - date_joined

  ### Student (Student Data - Holds personal and academic profile information)
    - id (PK)
    - first_name
    - last_name
    - index_number (Unique)
    - program (e.g., BSc ICT)
    - level (e.g., Level 100)
    - user_id (FK → User, mandatory for login access)

  ### Course (Stores course details offered in different programs.)
    - id (PK)
    - course_code (e.g., ICT101)
    - course_title
    - credit_hours


  ### Grade (Stores academic performance for each student in a given course, semester, and academic year.)
    - id (PK)
    - student_id (FK → Student)
    - course_id (FK → Course)
    - grade (e.g., A, B+, C)
    - semester (e.g., First, Second)
    - level (Matches student level)
    - academic_year (e.g., 2023/2024)

    


  ### Relationships
    - User → Student: One-to-One 

    - Student → Grade: One-to-Many (a student can have multiple grades)
    - Linked to User via a required user_id field to enforce secure, authenticated access to transcripts.

    - Course → Grade: One-to-Many (a course can have grades for multiple students)
    - Acts as a junction table linking Student and Course

    - Grade acts as a junction table linking students and courses.

---

## Part 3 - Start Building (Development Phase Begins)
The development phase will begin with setting up the Django project and creating the required applications. This includes implementing an authentication system, setting up the database, and building the core models for students, courses, grades, and transcripts.

---

## Part 4 - Development Phase Continues
During this stage, the main functionalities will be implemented. Staff upload and management features are added, allowing transcript data to be entered and updated. The student dashboard for transcript viewing is developed, and CRUD operations for all related models are completed.

---

## Part 5 - Polish, Test & User Review
The system will be tested for bugs and usability issues. The interface is refined for a better user experience. A pilot version will be shared with a sample of staff and students to gather feedback on functionality, speed, and usability.


---

## Part 6 - Feedback Implementation
User feedback will be reviewed, and changes implemented to improve the system’s performance and user experience. Final deployment preparations will be made to ensure the application is ready for full-scale use.


---

## Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite for development
- **Frontend:** Django Templates
- **Authentication:** Django’s built-in authentication system
- **Optional API:** PDF generation API for downloadable transcripts

---

## Installation & Setup
To run Transcript_Vault locally, 
- Clone the repository
- Set up a virtual environment.
- Run migrations, and
- Start the development server.
