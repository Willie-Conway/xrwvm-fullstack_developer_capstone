
# 🚗 Best Cras Dealership - Containerize your application 🚀

![Containerize your application](https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone/blob/6d5df879364425cd9c34ea574936ad13d6cc496a/Screenshots/Containerize%20your%20application.gif)


Welcome to the **Best Cras Dealership - Containerize your application**! This project involves building and deploying a full-stack application using **Django** for the backend and **React** for the frontend. We've containerized the Django application and deployed it on **Kubernetes** using **IBM Cloud** to adopt a hybrid cloud strategy. This enables the application to be easily scaled and managed in both private and public clouds.

---

## 🛠️ Technologies Used

- **Backend**:
  - 🐍 **Django** (Python Web Framework)
  - **MongoDB** (Database for storing reviews)
  - **Gunicorn** (WSGI HTTP Server)
  
- **Frontend**:
  - ⚛️ **React.js** (Frontend framework)
  - **npm** (Package manager)

- **Containerization**:
  - 🐳 **Docker**
  - **IBM Cloud Container Registry** (ICR)
  
- **Orchestration**:
  - **Kubernetes** (Container orchestration on IBM Cloud)
  
- **Hybrid Cloud**:
  - **IBM Cloud Code Engine** (Serverless deployment for sentiment analysis microservice)

---

## 📂 Project Structure

```bash
├── server/
│   ├── backend/
│   │   ├── manage.py
│   │   ├── requirements.txt
│   │   └── ... (Django app files)
│   ├── frontend/
│   │   ├── src/
│   │   ├── package.json
│   │   └── ... (React app files)
│   ├── Dockerfile
│   ├── entrypoint.sh
│   └── deployment.yaml
├── .gitignore
├── README.md
└── ... (Other project files)
```

---

## 🚀 Getting Started

To get started with this project, follow the steps below:

### 1. Clone the repository:

```bash
git clone https://github.com/Willie-Conway/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

### 2. Backend Setup:

#### 2.1 Install dependencies:
```bash
cd server/backend
pip install -r requirements.txt
```

#### 2.2 Run the Django app locally:
```bash
python manage.py runserver
```

### 3. Frontend Setup:

#### 3.1 Install frontend dependencies:
```bash
cd server/frontend
npm install
```

#### 3.2 Build the frontend:
```bash
npm run build
```

---

## 🐳 Docker Setup

### 1. Create Dockerfile for Backend

In the `server` directory, create a `Dockerfile` for containerizing the Django app:

```Dockerfile
FROM python:3.12.0-slim-bookworm
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1
ENV APP=/app

# Change the workdir.
WORKDIR $APP

# Install the requirements
COPY requirements.txt $APP
RUN pip3 install -r requirements.txt

# Copy the rest of the files
COPY . $APP

EXPOSE 8000
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
```

### 2. Create entrypoint.sh for Migration and Static Files

Create an `entrypoint.sh` file in the `server` directory with the following content:

```bash
#!/bin/sh
# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec "$@"
```

---

## 🏗️ Build and Push Docker Image to IBM Cloud Registry

### 1. Export your SN Labs Namespace:

```bash
MY_NAMESPACE=$(ibmcloud cr namespaces | grep sn-labs-)
echo $MY_NAMESPACE
```

### 2. Build the Docker image:

```bash
docker build -t us.icr.io/$MY_NAMESPACE/dealership .
```

### 3. Push the Docker image to the IBM Cloud Image Registry (ICR):

```bash
docker push us.icr.io/$MY_NAMESPACE/dealership
```

---

## 📝 Kubernetes Deployment

### 1. Create the `deployment.yaml` file

In the `server` directory, create a `deployment.yaml` file to define the Kubernetes deployment and service. Replace `<your-name-space>` with your SN Labs namespace:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: dealership
  name: dealership
spec:
  replicas: 1
  selector:
    matchLabels:
      run: dealership
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      labels:
        run: dealership
    spec:
      containers:
      - image: us.icr.io/$MY_NAMESPACE/dealership:latest
        imagePullPolicy: Always
        name: dealership
        ports:
        - containerPort: 8000
          protocol: TCP
      restartPolicy: Always
```

### 2. Apply the Kubernetes deployment:

```bash
kubectl apply -f deployment.yaml
```

### 3. Port-forward to access the application:

```bash
kubectl port-forward deployment.apps/dealership 8000:8000
```

Visit the application at [http://localhost:8000](http://localhost:8000) to interact with the dealership platform.

---

## 📝 Features

- **Dealer Listings**: Browse through different dealerships and view their details.
- **Review System**: Post reviews for dealerships and read others' reviews.
- **Sentiment Analysis**: Reviews are analyzed for sentiment using a microservice deployed on IBM Cloud Code Engine.

---

## 👥 Contributors

- **Willie Conway** - Developer
- **Your Team Members** - Collaborators

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎉 Acknowledgments

- Thanks to [IBM Cloud](https://www.ibm.com/cloud) for providing the infrastructure for the deployment.
- Special thanks to [Skills Network](https://skillsnetwork.com/) for providing this awesome learning platform!

