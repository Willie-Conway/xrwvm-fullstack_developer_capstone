# 👨🏿‍💻 Best Cars Dealership - Build CarModel and CarMake Django Models 🚙

Welcome to the **Best Cars Dealership - Build CarModel and CarMake Django Models**! This project is built using **Django** for the backend and provides an API for managing **car models** and **dealership reviews**. It's designed for a seamless user experience in handling car data and user authentication.

---

## 🌐 Live Demo

You can try out the live demo [here]() 🚀

---

## 🔧 Features

- **User Authentication**: Register, login, and log out functionality 🔑
- **Car Listings**: Display a list of car makes and models 🚗
- **Dealer Reviews**: Add and view reviews for car dealerships 📝
- **Responsive Design**: Works across devices 📱

---

## 🛠️ Technologies Used

- **Backend**: Django 3.2 ⚙️
- **Database**: SQLite (default for Django) 🗄️
- **Frontend**: (Optional) For future enhancements, HTML, CSS, and JavaScript will be used 🎨
- **API**: RESTful API for communication 📡

---

## ⚡ Setup Instructions

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

## 🚀 API Endpoints

- **POST `/register`**: User registration (username, password, first name, last name, email)
- **POST `/login`**: User login (username, password)
- **POST `/logout`**: User logout
- **GET `/get_cars`**: Get list of available car models and makes

---

## 👨🏿‍💻 Contributors

- **Willie Conway** - Developer 👨🏿‍💻

Feel free to open an issue or submit a pull request if you'd like to contribute! 🤝

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📢 Acknowledgments

- Thanks to **Django** for providing a robust web framework 🖤
- Inspiration from various tutorials on building RESTful APIs 🌐

