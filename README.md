🏠 RentEase – Rental Management System

 📌 Overview

**RentEase** is a full-stack rental management system that helps users browse, list, and manage rental properties efficiently.
It provides a seamless experience for both property owners and tenants with modern features like authentication, payments, and real-time communication.

---

 🚀 Features

* 🔐 **Authentication System**

  * Email & password login
  * Social login (Google, GitHub)

* 🏘️ **Property Management**

  * Add, edit, and delete properties
  * View property listings
  * Upload property images

* 💬 **Real-Time Chat**

  * User-to-user messaging
  * Instant communication between tenant & owner

* 📹 **Video Call Integration**

  * Virtual property viewing
  * Real-time video interaction

* 💳 **Online Payments**

  * Secure payment integration using Razorpay / Cashfree

* ⚡ **Caching**

  * Performance optimization using Memcached

---

 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Django
* Django REST Framework

### Database

* MySQL

### Other Tools & Integrations

* WebSockets (Django Channels)
* Google OAuth
* GitHub OAuth
* Razorpay / Cashfree Payment Gateway
* Memcached

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Nandhana2122/rental-management-system.git
cd rental-management-system
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your_secret_key
DEBUG=True

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_secret

GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_secret

CASHFREE_API_KEY=your_cashfree_key
RAZORPAY_KEY_ID=your_razorpay_key
RAZORPAY_SECRET=your_razorpay_secret
```

---

### 5️⃣ Apply migrations

```bash
python manage.py migrate
```

### 6️⃣ Run server

```bash
python manage.py runserver
```

---

## 📈 Future Enhancements

* AI-based property recommendations
* Advanced search filters
* Mobile app version

---
