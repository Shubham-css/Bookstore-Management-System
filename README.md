# 📚 Bookstore Management System

Welcome to my Bookstore Management System! 
This is a beginner-friendly Django project that lets users register, log in, browse a list of books, view book details, and add books to a shopping cart using sessions. 
The project is built from scratch with a clean DevOps setup using Docker and Jenkins.

---

## ✅ Project Features

### 👨‍💻 User Features:
- User Registration
- User Login and Logout
- View a list of all books
- View book details
- Add books to a shopping cart (using Django Sessions)

### 🛠️ Admin Features:
- Admin login
- Admin can add, edit, and delete books
- Manage book inventory
- (Custom admin panel — not using Django Admin)

### 🔧 Technical Rules Followed:
- ✅ Only **Class-Based Views** (CBV) are used  
- ❌ No Function-Based Views (FBV)  
- ❌ No Django Forms — All forms are manually created with HTML  
- ✅ Sessions are used for cart logic  
- ✅ DevOps setup done with Docker & Jenkins  
- ✅ Project uses GitHub version control (manually pushed)  
- ✅ No use of Django's built-in admin panel  

---

## 🧰 Tech Stack

- **Python** 3.13
- **Django** 5.2
- **HTML and CSS** (manual forms)
- **Docker** and **Docker Compose**
- **Jenkins** (for CI/CD pipeline)
- **Git** + GitHub

---

## 🗃️ Project Folder

bookstore/
│
├── bookstore/         # Django settings and root project
├── store/             # App for books and cart logic
├── templates/         # All HTML templates
├── static/            # Static files like CSS (if any)
├── Dockerfile         # For Docker image
├── docker-compose.yml # Docker services
├── Jenkinsfile        # Jenkins pipeline
├── manage.py          # Django management script
└── README.md          # This file


📝 Notes
->🔒 CBV only, FBV strictly avoided
->🛑 Django Forms not used
->🛒 Cart handled using Sessions
->🧰 DevOps setup complete with Docker & Jenkins
->🧾 Created admin panel for managing books
