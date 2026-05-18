# 🏠 Home Care — Centralized Household Services Platform

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap Version](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Home Care** is a premium, centralized web-based platform designed to bridge the gap between household service customers and verified professionals in **Belagavi (Belagaum), Karnataka**. Built using Django and Bootstrap 5, it offers an elegant, fast, and secure way to book household helper services including deep cleaning, professional cooking, childcare, elderly care, and home nursing.

---

## 📖 Table of Contents
* [🚀 Key Features](#-key-features)
* [🧠 Intelligent Worker Assignment (NEW)](#-intelligent-worker-assignment)
* [💻 Tech Stack](#-tech-stack)
* [📁 Project Architecture & Modules](#-project-architecture--modules)
* [🛠️ Installation & Setup](#️-installation--setup)
* [⚙️ Configuration & Environment](#️-configuration--environment)
* [📸 Screenshots](#-screenshots)
* [🔮 Future Enhancements](#-future-enhancements)
* [📄 License](#-license)
* [📧 Contact & Support](#-contact--support)

---

## 🚀 Key Features

* 🔐 **Multi-Role Authentication:** Secure login, registration, and onboarding for Customers, Service Providers (Workers), and Administrators.
* 📅 **Seamless Booking Engine:** Fully interactive service browsing with custom-priced visits, hourly rates, or daily pricing plans.
* 📍 **Location-Based Matching:** Smart provider allocation utilizing local regions/neighborhoods in Belagavi.
* 💳 **Razorpay Integration:** Secure online payment gateway for digital transactions.
* 💬 **Verified Testimonials:** Live review system with star ratings and comments to maintain high service quality.
* 🖼️ **Work Evidence Uploads:** Before/after job photos submitted by service providers for quality control and customer approval.
* 📊 **Jazzmin Admin Dashboard:** A state-of-the-art admin control panel for handling categories, booking approvals, payments, and users.
* ✨ **[NEW] Smart Worker Availability Checking:** Prevents booking unverified or offline providers.
* ✨ **[NEW] Rating-Based Prioritization:** Highest-rated workers are prioritized when automatically assigning bookings.

---

## 🧠 Intelligent Worker Assignment

The platform now features a highly advanced, automated backend system for assigning service providers to bookings. This prevents human-error and eliminates the need for manual dispatching.

* **First-Come-First-Serve Auto Assignment:** The moment a customer successfully books a service, the system queries the database to find the absolute best match.
* **Strict Eligibility Filtering:** The engine guarantees the worker is **verified**, **marked as available**, and **services the customer's specific neighborhood**.
* **Smart Time Slot Conflict Handling:** Using mathematical time-range calculations, the system checks all active jobs of potential workers. If a provider is booked for a specific date/time block (plus job duration), they are safely skipped to **prevent double-booking**.
* **Race Condition Protection:** The entire assignment block runs wrapped in Django's `transaction.atomic()` database lock. If 1,000 customers book at the same millisecond, the database handles them strictly one at a time, ensuring zero duplicate assignments.

---

## 💻 Tech Stack

* **Backend Framework:** [Django](https://www.djangoproject.com/) (Web Framework for perfectionists with deadlines)
* **Frontend Design:** HTML5, CSS3, Vanilla JS, and [Bootstrap 5](https://getbootstrap.com/)
* **Database:** [SQLite](https://www.sqlite.org/) (Development) / PostgreSQL (Production ready)
* **Payment Processing:** [Razorpay Payment Gateway](https://razorpay.com/)
* **Admin Interface:** [Django Jazzmin Theme](https://github.com/farridav/django-jazzmin)
* **Styling Extensions:** Django Crispy Forms & Crispy Bootstrap 5

---

## 📁 Project Architecture & Modules

The platform is constructed of highly cohesive Django applications structured as follows:

* 👤 **`accounts`**: Custom User model, worker profiles, registration pipelines, location mappings, and multi-role dashboard management.
* 📅 **`bookings`**: Booking state machine, intelligent assignment logic, scheduling system, and work photo uploads (`WorkPhoto`).
* 🏠 **`core`**: Homepage views, search algorithms, user testimonials/reviews, and region configurations (`Area`).
* 💳 **`payments`**: Digital payment processing, invoice generation, checkout pipelines, and callback handlers.
* 🛠️ **`services`**: Service categories (e.g., Cleaning, Childcare), item specifications, active pricing per unit.

---

## 🛠️ Installation & Setup

Follow these steps to run the platform locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/amansanadi07/household_service_platform.git
cd household_service_platform/household_service_platform-main
```

### 2. Set Up a Virtual Environment
Create an isolated environment using Python 3.12 (or 3.10+):
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Project Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Create and Migrate Database
Run Django's database schema creation:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Seed Demo Data (Optional but Recommended)
Populate your local database with default regions, services, and reviews:
```bash
python setup_areas.py
python update_prices.py
python add_demo_reviews.py
```

### 6. Create an Admin Account
```bash
python manage.py createsuperuser
```

### 7. Fire Up the Development Server
```bash
python manage.py runserver
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser to experience the platform!

---

## ⚙️ Configuration & Environment

For production deployments, rename `.env.example` to `.env` in your root folder and set your credentials. **Never commit real keys to version control.**

```env
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=your_secure_django_secret_key_here

# Debug Mode (set to False in production)
DEBUG=True

# Allowed Hosts
ALLOWED_HOSTS=127.0.0.1,localhost

# Razorpay Keys (Get these from Razorpay Dashboard)
RAZORPAY_KEY_ID=rzp_test_placeholder_key_id
RAZORPAY_KEY_SECRET=placeholder_key_secret_key
```

---

## 📸 Screenshots

| Customer Dashboard | Booking Assignment Workflow |
| :---: | :---: |
| ![Homepage Placeholder](https://images.unsplash.com/photo-1581578731548-c64695cc6952?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80) | ![Dashboard Placeholder](https://images.unsplash.com/photo-1484154218962-a197022b5858?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80) |

---

## 🔮 Future Enhancements

- 📱 **Mobile Application:** Building a React Native companion app for service workers on the go.
- 🔔 **Push Notifications:** WebSockets and FCM integration for live booking status updates.
- 💬 **In-App Messaging:** Real-time chat system between customers and assigned workers.
- 🗺️ **Live Tracking:** Google Maps API integration to track workers when their status is "On the Way".

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 📧 Contact & Support

* **Author:** Aman Sanadi
* **Project Repository:** [https://github.com/amansanadi07/household_service_platform](https://github.com/amansanadi07/household_service_platform)
* **Email:** amansanadi07@gmail.com
