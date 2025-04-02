# 👨🏿‍💻 Best Cars Dealership - Implement API endpoints using Express-Mongo 📍🚗

Welcome to the Best Cars Dealership - Implement API endpoints using Express-Mongo Project! In this project, we built a web application using **React**, **Node.js**, and **MongoDB**. The application provides various API endpoints using **Express** and **Mongoose** to interact with a MongoDB database. This file explains how to run the application and interact with the API endpoints.

## 🧑‍💻 Project Setup

### Clone the Project

If you haven't already cloned the repository, start by cloning it from GitHub:

```bash
git clone https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

### Install Dependencies

Before running the app, make sure all dependencies are installed:

```bash
cd server/database
npm install
```

### Docker Setup

The application is containerized using Docker. To build and run the app:

1. Build the Docker image:

```bash
docker build . -t nodeapp
```

2. Start the Docker containers:

```bash
docker-compose up
```

The app will run in two containers:
- **Node.js app** on port `3030`
- **MongoDB** on port `27017`

Once you see the server start successfully, you can begin testing the API endpoints.

## 📝 API Endpoints

### 1. Fetch All Reviews
- **URL:** `/fetchReviews`
- **Method:** `GET`
- **Description:** Fetches all reviews from the database.

### 2. Fetch Reviews for a Specific Dealer
- **URL:** `/fetchReviews/dealer/:id`
- **Method:** `GET`
- **Description:** Fetches reviews for a specific dealer by their ID.

### 3. Fetch All Dealerships
- **URL:** `/fetchDealers`
- **Method:** `GET`
- **Description:** Fetches all dealerships.

### 4. Fetch Dealerships by State
- **URL:** `/fetchDealers/:state`
- **Method:** `GET`
- **Description:** Fetches dealerships from a specific state.

### 5. Fetch a Specific Dealer by ID
- **URL:** `/fetchDealer/:id`
- **Method:** `GET`
- **Description:** Fetches details of a specific dealer by their ID.

### 6. Insert a Review
- **URL:** `/insert_review`
- **Method:** `POST`
- **Description:** Allows the insertion of new reviews. You'll need to send the review data in the body of the request.

---

### Testing Endpoints

#### Example URLs to test in Postman:

1. **Get reviews for a specific dealer:**
   ```
   GET /fetchReviews/dealer/29
   ```
   ![dealer_review.png](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/6cd9ee5b4541702119e3eca79d915f1df15c7c1d/Screenshots/dealer_review.png)

2. **Get all dealerships:**
   ```
   GET /fetchDealers
   ```
   ![dealerships.png](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/6cd9ee5b4541702119e3eca79d915f1df15c7c1d/Screenshots/dealerships.png)

3. **Get details for a specific dealer:**
   ```
   GET /fetchDealer/3
   ```
   ![dealer_details.png](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/6cd9ee5b4541702119e3eca79d915f1df15c7c1d/Screenshots/dealer_details.png)

4. **Get dealerships from a specific state (e.g., Kansas):**
   ```
   GET /fetchDealers/Kansas
   ```
   ![kansasDealers.png](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/6cd9ee5b4541702119e3eca79d915f1df15c7c1d/Screenshots/kansasDealers.png)

---

## 🔧 Development

If you need to make any changes to the API or fix bugs, follow these steps:

1. Open the `app.js` file in the `server/database` directory.
2. Implement missing endpoints (`fetchDealers`, `fetchDealers/:state`, `fetchDealer/:id`).
3. Run the following commands to rebuild and restart the Docker containers:

```bash
docker build . -t nodeapp
docker-compose up
```

### Important Files

- **Schemas:** `server/database/models/dealership.js` and `server/database/models/review.js`
- **API Routes:** `server/database/app.js`
- **JSON Data Files:** `server/database/data/dealerships.json` and `server/database/data/reviews.json`

---

## 📂 Project Structure

Here's a breakdown of the project directory structure:

```
/xrwvm-fullstack_developer_capstone
    ├── server/
    │   ├── database/
    │   │   ├── app.js
    │   │   ├── models/
    │   │   │   ├── dealership.js
    │   │   │   ├── review.js
    │   │   ├── data/
    │   │   │   ├── dealerships.json
    │   │   │   ├── reviews.json
    │   │   ├── docker-compose.yml
    │   │   ├── Dockerfile
    ├── client/  (React application files)
    ├── README.md
```

---

## 📚 Dependencies

- **Node.js**
- **Express**
- **Mongoose**
- **MongoDB** (running in a Docker container)
- **Docker** (for containerization)
- **Postman** (for testing APIs)

---

## 🏁 Deployment

1. Build and start the containers (as described earlier).
2. Access the API endpoints through `http://localhost:3030`.

---

## 👨‍💻 Author

**Willie Conway**  
GitHub: [@Willie-Conway](https://github.com/Willie-Conway)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


