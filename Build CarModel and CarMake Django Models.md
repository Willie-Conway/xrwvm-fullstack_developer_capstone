
# 👨🏿‍💻 **Best Cars Dealership - Build CarModel and CarMake Django Models** 🚙

Welcome to the **Best Cars Dealership** project! This application is built using **Django** and serves as a simple platform for managing **car models** and **dealership reviews**. Users can view car listings, add reviews, and manage their accounts.

![Build CarModel and CarMake Django Models.gif](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/265bce3c0e1eb253ee32777bbb10d9dbb44437eb/Screenshots/Build%20CarModel%20and%20CarMake%20Django%20Models.gif)


---

## 🔧 **Features**

- **User Authentication**: Register, login, and log out functionality 🔑
- **Car Listings**: Display a list of car makes and models 🚗
- **Dealer Reviews**: Add and view reviews for car dealerships 📝
- **Responsive Design**: Works across devices 📱

---

## 🛠️ **Technologies Used**

- **Backend**: Django 3.2 ⚙️
- **Database**: SQLite (default for Django) 🗄️
- **Frontend**: (Optional) Future enhancements will use HTML, CSS, and JavaScript 🎨
- **API**: RESTful API for communication 📡

---

## ⚡ **Setup Instructions**

### Step 1: Clone the Repository

```bash
git clone https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

### Step 2: Create a Virtual Environment

```bash
python3 -m venv djangoenv
source djangoenv/bin/activate  # On Windows, use `djangoenv\Scripts\activate`
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations

```bash
python manage.py migrate
```

### Step 5: Run the Development Server

```bash
python manage.py runserver
```

You can access the project in your browser at [http://localhost:8000](http://localhost:8000).

---

## 🚀 **API Endpoints**

- **POST `/register`**: User registration (username, password, first name, last name, email)
- **POST `/login`**: User login (username, password)
- **POST `/logout`**: User logout
- **GET `/get_cars`**: Get a list of available car models and makes

---

## 🖼️ **Screenshots for Peer Review**

- **Car and Model List**: A screenshot of the list of car models and makes.
  ![Car and Model List](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/d5da88f699cede94099ca5dbbe2a8b74f556b091/Screenshots/cars.png)

- **Car Models in Django Admin**: A screenshot of the car models section in the Django Admin interface.
 ![Car Models in Django Admin](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/d5da88f699cede94099ca5dbbe2a8b74f556b091/Screenshots/car%20models.png)

- **Admin Login**: A screenshot after logging in to the Django Admin.
  ![Admin Login](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/d5da88f699cede94099ca5dbbe2a8b74f556b091/Screenshots/admin_login.png)

- **Admin Logout**: A screenshot of the admin logout page, which redirects to the login page.
  ![Admin Logout](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/d5da88f699cede94099ca5dbbe2a8b74f556b091/Screenshots/admin_logout.png)

---

## 👨🏿‍💻 **Contributors**

- **Willie Conway** - Developer 👨🏿‍💻

Feel free to open an issue or submit a pull request if you'd like to contribute! 🤝

---

## 📜 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📢 **Acknowledgments**

- Thanks to **Django** for providing a robust web framework 🖤
- Inspiration from various tutorials on building RESTful APIs 🌐


