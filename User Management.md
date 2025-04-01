
# 🚗 **Best Cars Dealership - User Management** 👨🏿‍💻

![User Management](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/c15693aa972f35033c7b8901ab84b3f7eb01ef2b/Screenshots/User%20Management.gif)

Welcome to the **Best Cars Dealership**! This repository contains a Django backend with a React frontend for managing users, including features like **Registration**, **Login**, and **Logout**. This guide will walk you through setting up and using the application. 🚀

## 🛠️ **Features**
- **Registration**: Allows users to create a new account 📝.
- **Login**: Authenticates users with their credentials 🔑.
- **Logout**: Logs users out of the system 🚪.

---

## 🚀 **Setup and Installation** 

### Backend (Django) Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd your-repository/server
   ```

3. **Install Required Packages:**

   - Create a virtual environment:

     ```bash
     python3 -m venv djangoenv
     source djangoenv/bin/activate  # For Mac/Linux
     djangoenv\Scripts\activate  # For Windows
     ```

   - Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

4. **Create Superuser for Admin Access:**

   ```bash
   python3 manage.py createsuperuser
   ```

5. **Run the Server:**

   ```bash
   python3 manage.py runserver
   ```

6. **Access the Admin Panel**:
   Open `http://localhost:8000/admin/` and log in with the superuser credentials you just created. 🔑

---

### Frontend (React) Setup

1. **Navigate to the Client Directory:**

   ```bash
   cd frontend
   ```

2. **Install Frontend Dependencies:**

   ```bash
   npm install
   ```

3. **Build the React Application:**

   ```bash
   npm run build
   ```

4. **Run the React Development Server:**

   ```bash
   npm start
   ```

---

## 💻 **Features Walkthrough**

### 1. **Registration** 📝
   - Navigate to the **Sign Up** page.
   - Fill in the details:
     - **Username**
     - **First Name**
     - **Last Name**
     - **Email**
     - **Password**
   - On successful registration, the user will be logged in and redirected to the homepage.

### 2. **Login** 🔑
   - Navigate to the **Login** page.
   - Enter your **username** and **password**.
   - After successful authentication, the username will be displayed in the header, and you'll have a **Logout** button.

### 3. **Logout** 🚪
   - Click the **Logout** button in the header to log out.
   - Once logged out, you will be redirected to the homepage, and the username will no longer be displayed.

---

## 🧪 **Testing**

1. After setting up the backend and frontend, test the following:
   - **Sign-up**: Register a new user and confirm they are logged in immediately.
   - **Login**: Log in with the newly registered user credentials.
   - **Logout**: Log out and confirm the session is cleared.

2. **Screenshots** 📸:
   - Take screenshots after **signing up**, **logging in**, and **logging out**. Name them accordingly:
     - **Signing Up**: ![Signing Up Screenshot](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/a0b0927b7a2548a3b5ff32960aad03f5c71837f1/Screenshots/sign-up.png)
     - **Logging In**: ![Logging In Screenshot](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/a0b0927b7a2548a3b5ff32960aad03f5c71837f1/Screenshots/login.png)
     - **Logging Out**: ![Logging Out Screenshot](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/a0b0927b7a2548a3b5ff32960aad03f5c71837f1/Screenshots/logout.jpg)

---

## 📝 **Notes**

- Make sure your **Django server** and **React app** are running concurrently for smooth integration.
- The **superuser** allows you to access the Django Admin Panel and manage users through the admin interface.

---

## 💡 **Troubleshooting**

- **If you get errors while installing packages**, ensure you're using a compatible version of Python and Node.js.
- **If login doesn’t work**, verify that the username and password are correct. You can also check the Django logs for errors.
- **Ensure CORS is properly configured** to allow communication between the frontend and backend if running on different ports.

---

## 📌 **Contribution**

- Fork the repository 🏠
- Create a new branch 👨🏿‍💻
- Implement features or fix bugs 🛠️
- Open a Pull Request 📬

---

## 👨‍💻 **Author**
- **Willie Conway** | [GitHub](https://github.com/Willie-Conway) | [LinkedIn](https://linkedin.com/in/willieconway)

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thanks for checking out this project! 😊
```
