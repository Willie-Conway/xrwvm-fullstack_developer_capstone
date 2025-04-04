
# 🏢 **Best Cars Dealership - Add Dynamic pages** - Fullstack Capstone Project 👨🏿‍💻🚗

Welcome to the **Best Cars Dealership - Add Dynamic pages**! In this project, we have created a web application that allows users to view a list of car dealerships, see details for each dealer, and add reviews. The app integrates sentiment analysis to show if a review is positive, neutral, or negative.

---

## 🚀 **Getting Started**

These instructions will guide you through setting up and running the project locally.

### 📦 **Prerequisites**

- **Django** for backend
- **React** for frontend
- **MongoDB** for database
- **Node.js** & **npm** (or **yarn**) for frontend dependencies
- **Python 3.x** and **virtualenv** for backend setup

### 🛠️ **Installation Steps**

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone.git
    cd xrwvm-fullstack_developer_capstone
    ```

2. **Set up the Django Environment**:
   - Create a virtual environment:

     ```bash
     cd server
     pip install virtualenv
     virtualenv djangoenv
     source djangoenv/bin/activate  # On Windows use djangoenv\Scripts\activate
     ```

   - Install the required dependencies:

     ```bash
     python3 -m pip install -U -r requirements.txt
     ```

   - Apply migrations to set up the database:

     ```bash
     python3 manage.py makemigrations
     python3 manage.py migrate
     ```

   - Start the Django server:

     ```bash
     python3 manage.py runserver
     ```

3. **Set up the React Frontend**:
   - Navigate to the frontend directory:

     ```bash
     cd frontend
     ```

   - Install the required dependencies:

     ```bash
     npm install
     ```

   - Build the React app:

     ```bash
     npm run build
     ```

4. **Start the Frontend Development Server**:
   - Run the React development server:

     ```bash
     npm start
     ```

---

## 🧰 **Tech Stack**

- **Backend**: Django 🐍, Django REST Framework, SQLite Database
- **Frontend**: React.js ⚛️, Axios, React Router
- **Database**: MongoDB 🗃️
- **Sentiment Analysis**: NLTK (Natural Language Toolkit) 🤖
- **Deployment**: Docker 🐳 (optional)

---

## 🌟 **Features**

- **Dealer Listing**: View a list of car dealerships.
- **Dealer Details**: Click on a dealer to see reviews and details.
- **Post Reviews**: Logged-in users can post reviews for dealers.
- **Sentiment Analysis**: Reviews are analyzed to determine their sentiment (positive, neutral, negative).
- **Search by State**: Filter dealerships by state.
- **Responsive UI**: Built with a focus on usability and design.

---

## 📝 **API Endpoints**

### 1. **GET /djangoapp/get_dealers/**

- **Description**: Fetches the list of dealers.
- **Response**:

    ```json
    {
      "dealers": [
        {
          "id": 1,
          "name": "XYZ Dealership",
          "location": "California"
        },
        {
          "id": 2,
          "name": "ABC Motors",
          "location": "New York"
        }
      ]
    }
    ```

### 2. **POST /djangoapp/add_review**

- **Description**: Add a new review for a dealer.
- **Request Body**:

    ```json
    {
      "name": "John Doe",
      "dealership": 1,
      "review": "Great service!",
      "purchase": true,
      "purchase_date": "2025-04-03",
      "car_make": "Toyota",
      "car_model": "Camry",
      "car_year": 2020
    }
    ```

- **Response**:

    ```json
    {
      "status": 200,
      "message": "Review added successfully."
    }
    ```

### 3. **GET /djangoapp/get_cars**

- **Description**: Get a list of available car models.
- **Response**:

    ```json
    {
      "CarModels": [
        {
          "CarMake": "Toyota",
          "CarModel": "Camry"
        },
        {
          "CarMake": "Honda",
          "CarModel": "Civic"
        }
      ]
    }
    ```

---

## 🔧 **Steps for Development**

### 1. **Add Dynamic Pages**

- Add the **Dealers** component to the `frontend/src/App.js` and route to `/dealers`:

    ```javascript
    import Dealers from './components/Dealers/Dealers';

    <Route path="/dealers" element={<Dealers />} />
    ```

- Update the **Django** `urls.py` to serve the `index.html` for `/dealers`:

    ```python
    path('dealers/', TemplateView.as_view(template_name="index.html")),
    ```

### 2. **Create Dealer Review Page**

- Add a **PostReview** page where authenticated users can add reviews.

    - Import **PostReview** in `frontend/src/App.js`:

      ```javascript
      import PostReview from './components/Dealers/PostReview';
      ```

    - Add a route for `/postreview/:id`:

      ```javascript
      <Route path="/postreview/:id" element={<PostReview />} />
      ```

- Update `urls.py` in Django to add path for the **Post Review** page:

    ```python
    path('postreview/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),
    ```

---

## 📸 **Screenshots**

- **Dealer List**:
    - View a list of all dealers in a table format. **Screenshot**: `get_dealers.png`
    
- **Dealer Reviews**:
    - View reviews for a specific dealer. **Screenshot**: `dealer_id_reviews.png`
    
- **Post a Review**:
    - Add a review for a dealer. **Screenshot**: `dealership_review_submission.jpg`

- **Dealer Details (Logged In)**:
    - View dealer details after logging in. **Screenshot**: `get_dealers_loggedin.png`

---

## 🔄 **How to Contribute**

Feel free to fork the repository and submit pull requests for any changes or improvements.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-xyz`)
5. Open a pull request

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 **Contact**

If you have any questions or need help, feel free to contact me:

- **Email**: willie.conway@example.com 📧
- **GitHub**: [@Willie-Conway](https://github.com/Willie-Conway) 🐙

---

## 🎉 **Acknowledgements**

Special thanks to the open-source community for their contributions! 🙏
```
