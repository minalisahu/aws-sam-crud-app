# 🛠️ Serverless CRUD API with Python and AWS SAM

This project is a simple serverless CRUD application built using **Python**, **AWS Lambda**, **DynamoDB**, and the **AWS SAM CLI**. It exposes RESTful API endpoints via API Gateway and performs basic operations (Create, Read, Update, Delete) on a DynamoDB table.

## 🚀 Features

- Serverless architecture using AWS Lambda
- CRUD operations via API Gateway
- DynamoDB as the backend data store
- Local development and testing with SAM CLI

---

## 📦 Tech Stack

- Python 3.12
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS SAM CLI
- Docker

---

## 📁 Project Structure

crud-app-new/
├── hello_world/
│ └── app.py # Lambda function handler
├── template.yaml # AWS SAM template
├── env.json # Environment variables for local testing
└── README.md




---

## 🔧 Prerequisites

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- [Docker](https://www.docker.com/products/docker-desktop/)

---

## 🛠️ Setup and Run Locally

### 1. Install dependencies (if any)
This app currently uses only built-in libraries. If you add dependencies, use a `requirements.txt`.

### 2. Build the project

```bash
sam build

---

## 🛠️ Setup and Run Locally

### 1. Install dependencies (if any)
This app currently uses only built-in libraries. If you add dependencies, use a `requirements.txt`.

### 2. Build the project

```bash
sam build


### 3. 🧪 Run Locally

Start the local API using SAM:

```bash
sam local start-api


📫 Sample cURL Commands
✅ Create an item (POST)

curl -X POST http://localhost:3000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Notebook", "description": "A ruled notebook with 100 pages"}'
📋 Get all items (GET)

curl http://localhost:3000/items
🔁 Update an item (PUT)

curl -X PUT http://localhost:3000/items/{id} \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Name", "description": "Updated Description"}'
❌ Delete an item (DELETE)

curl -X DELETE http://localhost:3000/items/{id}
📤 Deployment to AWS
To deploy the application to your AWS account:

sam deploy --guided

