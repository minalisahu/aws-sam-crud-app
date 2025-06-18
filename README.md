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

Make sure the following tools are installed on your system:

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- [Docker](https://www.docker.com/products/docker-desktop/)

---

## 🛠️ Setup and Run Locally

### 1. Install dependencies (if any)

This project currently uses only built-in libraries. If you add any external dependencies, include them in a `requirements.txt` file.

### 2. Build the project

```bash
sam build
---

```


