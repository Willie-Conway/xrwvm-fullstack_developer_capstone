# 👨🏿‍💻 Best Cars Dealership - Create Django Proxy Services Of Backend APIs📍🚗

Welcome to the **Best Cars Dealership - Create Django Proxy Services Of Backend APIs**! This API allows users to interact with a database of car dealerships and customer reviews. It includes various routes for fetching, adding, and filtering reviews and dealerships. 🚗🌟

---

## 📝 Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Routes](#api-routes)
6. [Screenshot](#screenshot)
7. [Contributing](#contributing)
8. [License](#license)

---

## 📌 Overview

This project provides an API for fetching car dealership information and customer reviews. The API is built using **Node.js**, **Express**, and **MongoDB** with **Mongoose** for data modeling. 🚀

- **MongoDB** is used for data storage.
- **Express** handles routing and HTTP requests.
- **Mongoose** provides a convenient way to interact with MongoDB.

---

## 🚀 Features

- **Fetch all dealerships**: Get a list of all car dealerships in the database.
- **Fetch reviews by dealership**: Retrieve reviews based on dealership ID.
- **Add reviews**: Insert new customer reviews into the database.
- **Search dealerships by state**: Filter dealerships by state.
- **Search dealership by ID**: Get a specific dealership using its ID.

---

## 📦 Installation

Follow these steps to install and run the API locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repository-name
   ```

3. Install the necessary dependencies:

   ```bash
   npm install
   ```

4. Start the server:

   ```bash
   npm start
   ```

   The server will be running on `http://localhost:3030`.

---

## ⚙️ Usage

Once the server is running, you can interact with the following API routes:

- **GET `/`**: Welcome message
- **GET `/fetchReviews`**: Fetch all reviews
- **GET `/fetchReviews/dealer/:id`**: Fetch reviews for a specific dealership
- **GET `/fetchDealers`**: Fetch all dealerships
- **GET `/fetchDealers/:state`**: Fetch dealerships by state
- **GET `/fetchDealer/:id`**: Fetch dealership by ID
- **POST `/insert_review`**: Insert a new review

---

## 🧑‍💻 API Routes

### 1. Fetch All Reviews
- **Method**: GET
- **URL**: `/fetchReviews`
- **Description**: Get a list of all reviews from the database.

### 2. Fetch Reviews by Dealer ID
- **Method**: GET
- **URL**: `/fetchReviews/dealer/:id`
- **Description**: Get reviews for a specific dealership by ID.

### 3. Fetch All Dealerships
- **Method**: GET
- **URL**: `/fetchDealers`
- **Description**: Fetch all dealerships.

### 4. Fetch Dealerships by State
- **Method**: GET
- **URL**: `/fetchDealers/:state`
- **Description**: Fetch all dealerships from a specific state.

### 5. Fetch Dealership by ID
- **Method**: GET
- **URL**: `/fetchDealer/:id`
- **Description**: Fetch a dealership by its unique ID.

### 6. Insert a New Review
- **Method**: POST
- **URL**: `/insert_review`
- **Description**: Add a new review for a dealership.

---

## 📸 Screenshot

Here’s a screenshot of the **Sentiment Analyzer** feature that provides sentiment analysis based on the customer reviews:

![Sentiment Analyzer](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/2772982967daa034b30462689f70a618b7c86271/Screenshots/sentiment_analyzer.png)

---

## 🤝 Contributing

We welcome contributions to improve the project! If you have suggestions or fixes, feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your fork
5. Open a pull request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📱 Contact

For questions or suggestions, feel free to contact me:

- **Email**:  hire.willie.conway@gmail.com
- **GitHub**: [@Willie-Conway](https://github.com/Willie-Conway)

---

🚗 Enjoy browsing the Dealerships & Reviews API! 🚗
```

