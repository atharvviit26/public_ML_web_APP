


# Software Requirements Specification for Online College Admission System

## 1 INTRODUCTION

### 1.1 DOCUMENT PURPOSE
This Software Requirements Specification (SRS) document outlines the requirements for the Online College Admission System. The current revision is 1.0, and it aims to provide a detailed description of the software requirements that will guide the development team in building the application. This SRS covers both the user interface and functional requirements, as well as performance criteria, for the system to ensure it meets the needs of students and administrative staff effectively.

### 1.2 PRODUCT SCOPE
The Online College Admission System is designed to facilitate the college admission process for prospective students in an efficient and user-friendly manner. The primary purpose of this product is to streamline the application process, allowing students to easily submit their applications and relevant documents online. Key benefits include reducing administrative workload for college staff, minimizing application processing time, and enhancing the overall user experience for applicants. The system aims to improve transparency and communication between students and administrative personnel, ultimately contributing to higher satisfaction rates for all stakeholders involved.

### 1.3 INTENDED AUDIENCE AND DOCUMENT OVERVIEW
This document is intended for multiple audiences, including:
- **Developers**: To understand the system requirements and the architecture that will guide the development process.
- **Project Managers**: To track project progress and ensure alignment with requirements.
- **Quality Assurance Teams**: To develop testing strategies and verify the application meets the specified requirements.
- **End Users**: To understand the features available to them and how to interact with the system.

The SRS is organized into several sections. After this introduction, the document details overall product descriptions, including functionality and constraints, before specifying detailed requirements in subsequent sections.

### 1.4 DEFINITIONS, ACRONYMS AND ABBREVIATIONS
- **SRS**: Software Requirements Specification
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Admin**: The role responsible for managing application reviews, approvals, and rejections.
- **User**: The prospective student applying for college admission.
- **HTML**: Hypertext Markup Language, the standard markup language for documents designed to be displayed in a web browser.
- **CSS**: Cascading Style Sheets, a style sheet language used for describing the presentation of a document written in HTML.
- **ORM**: Object-Relational Mapping, a programming technique for converting data between incompatible type systems in object-oriented programming languages.

### 1.5 DOCUMENT CONVENTIONS
This document follows IEEE formatting standards, utilizing Arial font size 11 for body text. Comments and notes are indicated using italics. The text is single-spaced with 1-inch margins. Section and subsection titles adhere to the specified template structure.

### 1.6 REFERENCES AND ACKNOWLEDGMENTS
- DataFlair Team for project guidelines and initial setup resources.
- Django documentation for framework specifications and best practices.
- Bootstrap documentation for front-end design and responsive web development.

## 2 OVERALL DESCRIPTION

### 2.1 PRODUCT OVERVIEW
The Online College Admission System is a new web application that serves as an online platform for managing college admissions. It is not a follow-on product but rather a self-contained system designed to meet the specific needs of both students and administrative staff in the admissions process. The system allows students to submit applications and supporting documents electronically while providing administrators with tools to manage and review applications efficiently.

![System Architecture Diagram](https://via.placeholder.com/600x400.png?text=System+Architecture+Diagram)  
*Note: Replace this placeholder with a diagram illustrating the system architecture, components, and interactions.*

### 2.2 PRODUCT FUNCTIONALITY
The system encompasses the following major functions:
- User registration and authentication (login/logout).
- Application form submission with document uploads (e.g., marksheets).
- Application editing and resubmission upon rejection.
- Admin dashboard for managing application statuses (approved, pending, rejected).
- Notification system for users regarding application updates.

### 2.3 DESIGN AND IMPLEMENTATION CONSTRAINTS
- The system must be developed using the Django framework.
- Front-end design must utilize HTML, CSS, and Bootstrap for responsive layouts.
- The application should leverage Django’s ORM for database management.
- Hosting requirements necessitate a server environment compatible with Django applications.
- User data must be stored securely, adhering to relevant data protection regulations.

### 2.4 ASSUMPTIONS AND DEPENDENCIES
- Users are assumed to have basic internet access and familiarity with web applications.
- The project assumes that all users will have valid email addresses for communication and notifications.
- The application relies on third-party services for email notifications and file storage, which must be available and functional throughout the project lifecycle.

---























---

## 3 SPECIFIC REQUIREMENTS

### 3.1 EXTERNAL INTERFACE REQUIREMENTS

#### 3.1.1 User Interfaces
The Online College Admission System will feature a web-based user interface accessible via standard web browsers. The primary user interface will include:
- **Application Dashboard**: Users can view the status of their applications, access forms, and receive notifications.
- **Application Form**: An interactive form that allows students to input their personal and educational details and upload supporting documents.
- **Admin Panel**: A dedicated interface for administrators to manage applications, review submissions, and communicate with students.

**User Interaction**: Users will interact with the interface primarily through a point-and-click mechanism, navigating via menus and buttons. The design will be responsive to support various device types, including desktops, tablets, and smartphones.

#### 3.1.2 Hardware Interfaces
The system will interface primarily with:
- **Web Servers**: To host the application and manage incoming user requests.
- **Storage Devices**: For saving uploaded documents and application data securely.
- **User Devices**: Users will access the system via personal computers or mobile devices using web browsers.

#### 3.1.3 Software Interfaces
The Online College Admission System will interact with:
- **Database Management System**: To store user data, application forms, and document uploads. It will utilize Django’s ORM for interactions with the database.
- **Email Service Provider**: To send notifications and updates to users regarding their application status.

### 3.2 FUNCTIONAL REQUIREMENTS
The functional requirements describe the specific behaviors and functionalities the system must provide.

#### 3.2.1 F1: User Registration
The system shall allow users to create an account by providing personal details, including name, email, and password.

#### 3.2.2 F2: User Authentication
The system shall authenticate users upon login, allowing access to their respective dashboards and application forms.

#### 3.2.3 F3: Application Submission
The system shall enable users to fill out and submit an online application form, including uploading necessary documents (e.g., marksheets).

#### 3.2.4 F4: Application Editing
The system shall permit users to edit and resubmit their application if initially rejected by the admin, ensuring the user can rectify any issues.

#### 3.2.5 F5: Admin Application Review
The system shall provide an admin interface to review submitted applications, approve or reject them, and communicate decisions to users.

### 3.3 USE CASE MODEL
A use case diagram will encapsulate the entire system and its actors, including students and admin users. 

#### 3.3.1 Use Case #1: Submit Application (U1)
- **Author**: Atharv Sawant
- **Purpose**: To allow students to submit their applications online.
- **Requirements Traceability**: F1, F3, F4
- **Priority**: High
- **Preconditions**: User must be registered and logged in.
- **Postconditions**: Application is stored in the database and is available for admin review.
- **Actors**: Student
- **Flow of Events**:
  1. Basic Flow:
     - The user navigates to the application form.
     - The user fills out personal and educational details.
     - The user uploads required documents.
     - The user submits the application.
  2. Alternative Flow: 
     - If required fields are missing, the system prompts the user to fill them.
  3. Exceptions:
     - If the document upload fails, the system notifies the user and allows retry.
- **Includes**: F2 (User Authentication)
- **Notes/Issues**: Ensure file size limits for document uploads.

#### 3.3.2 Use Case #2: Admin Review Application (U2)
- **Author**: Atharv Sawant
- **Purpose**: To allow admin users to review applications and update their status.
- **Requirements Traceability**: F5
- **Priority**: High
- **Preconditions**: Admin must be logged in.
- **Postconditions**: Application status is updated in the database, and the user is notified.
- **Actors**: Admin
- **Flow of Events**:
  1. Basic Flow:
     - The admin views a list of applications.
     - The admin selects an application to review.
     - The admin approves or rejects the application, optionally providing a reason.
  2. Alternative Flow: 
     - If no applications are pending, the admin receives a notification.
  3. Exceptions:
     - If there’s a system error during status update, an error message is displayed.
- **Includes**: None
- **Notes/Issues**: Ensure reason for rejection is communicated to users.

---

## 4 OTHER NON-FUNCTIONAL REQUIREMENTS

### 4.1 PERFORMANCE REQUIREMENTS
- **P1**: The system shall process application submissions within 2 seconds under normal operating conditions.
- **P2**: The admin dashboard shall load within 3 seconds when accessed by up to 100 concurrent users.

### 4.2 SAFETY AND SECURITY REQUIREMENTS
- **SR1**: All user data must be stored securely using encryption at rest and in transit to prevent unauthorized access.
- **SR2**: The system must implement user authentication measures, including secure password storage and session management.
- **SR3**: User sessions shall expire after 15 minutes of inactivity to minimize the risk of unauthorized access.

### 4.3 SOFTWARE QUALITY ATTRIBUTES

#### 4.3.1 Reliability
The system shall maintain 99.9% uptime to ensure availability for users, implementing redundancy measures to handle server failures.

#### 4.3.2 Usability
The user interface shall be intuitive and user-friendly, allowing new users to complete their applications without needing external assistance. The system should aim for an average task completion time of less than 5 minutes for application submissions.

#### 4.3.3 Maintainability
The codebase shall adhere to standard coding conventions and documentation practices to facilitate future enhancements and bug fixes. The system should support modular design principles, allowing for the easy addition of new features.

---





























---

## 5 OTHER REQUIREMENTS

This section outlines additional requirements not covered in other sections of this SRS.

### 5.1 Database Requirements
- **DR1**: The system must use a relational database management system (RDBMS) to store user data, application forms, and documents. The preferred choice is PostgreSQL for its reliability and support for complex queries.
- **DR2**: The database schema must support normalization to reduce redundancy and improve data integrity.

### 5.2 Internationalization Requirements
- **IR1**: The application must support multiple languages, allowing users to select their preferred language from a dropdown menu on the login page.
- **IR2**: Date formats must be adaptable to user locale settings (e.g., MM/DD/YYYY or DD/MM/YYYY).

### 5.3 Legal Requirements
- **LR1**: The system must comply with data protection regulations, including GDPR for users in the EU, ensuring proper data handling, user consent, and the right to be forgotten.
- **LR2**: The system must provide users with a privacy policy outlining how their data will be used and protected.

### 5.4 Reuse Objectives
- **RO1**: The system should be designed with reusable components, allowing future projects to leverage existing functionality, particularly in user authentication and application processing workflows.

---

## APPENDIX A – DATA DICTIONARY

The data dictionary provides definitions for the various variables, states, and functional requirements mentioned in this document.

| **Data Item**         | **Description**                                               | **Type**        | **Possible Values**               | **Related Operations**                     |
|-----------------------|---------------------------------------------------------------|-----------------|-----------------------------------|-------------------------------------------|
| User ID               | Unique identifier for each user                               | Integer         | Positive integers                  | Create, Read, Update, Delete              |
| User Name             | Full name of the user                                        | String          | Alphanumeric (up to 50 characters) | Create, Read, Update                       |
| Email                 | User's email address                                         | String          | Valid email format                 | Create, Read, Update                       |
| Password              | User's encrypted password                                     | String          | Encrypted string                   | Create, Read (authentication)             |
| Application ID        | Unique identifier for each application                        | Integer         | Positive integers                  | Create, Read, Update, Delete              |
| Application Status    | Current status of the application                             | String          | Pending, Approved, Rejected       | Read, Update                               |
| Document Upload       | File uploaded by the user                                    | File            | Various formats (PDF, DOCX, JPG)  | Create (upload), Read                      |
| Submission Date       | Date when the application was submitted                      | Date            | YYYY-MM-DD                        | Create, Read                               |

---

## APPENDIX B - GROUP LOG

### Group Meeting Minutes

#### Meeting 1: Kickoff Meeting
**Date**: 11/10/24  
**Attendees**: Atharv ,Rajdeep, Vishal,Swapnil  
**Notes**: 
- Discussed project goals and objectives.
- Assigned roles: [Names and roles].
- Set initial deadlines for SRS completion.

#### Meeting 2: Requirements Gathering
**Date**: 17/10/24  
**Attendees**: Atharv ,Rajdeep, Vishal,Swapnil
**Notes**: 
- Conducted interviews with stakeholders.
- Collected functional and non-functional requirements.
- Drafted the first version of the SRS.

#### Meeting 3: Review and Feedback
**Date**: 21/10/24  
**Attendees**: Atharv ,Rajdeep, Vishal,Swapnil
**Notes**: 
- Reviewed the first draft of the SRS.
- Gathered feedback for improvements.
- Assigned tasks for revisions.

#### Meeting 4: Final Review
**Date**: 31/10/24  
**Attendees**: Atharv ,Rajdeep, Vishal,Swapnil
**Notes**: 
- Finalized the SRS document.
- Ensured all sections are complete and meet requirements.
- Discussed submission plans and next steps.

### Group Activities
- Drafted individual sections of the SRS document.
- Collaborated using shared online tools for document editing and tracking changes.
- Regular communication through [communication platform].

### Effort Summary
- Total hours spent on the project: 9 hrs
- Individual contributions tracked through [Online Meet].

---


