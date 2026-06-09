# Cloud-Based Data Analytics Pipeline

## Overview

A cloud-native ETL and analytics platform built using Python, FastAPI, AWS S3, PostgreSQL (Supabase), SQLAlchemy, Docker, and Pandas.

The project demonstrates the complete lifecycle of a modern data engineering pipeline, including data ingestion, validation, transformation, storage, analytics generation, and API-based data access.

Designed to simulate real-world data engineering and backend development workflows, the platform processes 50,000+ transactional records and exposes business insights through RESTful APIs.

---

## Features

### Data Ingestion Layer

- Generate synthetic business datasets
- Store raw datasets in AWS S3
- Cloud-native raw data lake architecture

### Data Validation Layer

- Missing value detection
- Duplicate record removal
- Invalid data filtering
- Data quality checks

### Data Transformation Layer

- Feature engineering
- Revenue categorization
- Monthly and yearly aggregations
- Analytics-ready datasets

### Database Layer

- PostgreSQL (Supabase)
- SQLAlchemy ORM
- Structured relational schema
- Optimized analytics queries

### Analytics Layer

- Total Revenue Analysis
- Monthly Revenue Trends
- Top Customers
- Top Products
- Revenue Category Insights

### API Layer

- FastAPI REST APIs
- Swagger Documentation
- JSON Responses
- Analytics Endpoints

### DevOps

- Dockerized Deployment
- GitHub Actions CI/CD
- Environment Variable Management

---

## Architecture

CSV Generator
↓
AWS S3 Raw Layer
↓
Validation Layer
↓
Transformation Layer
↓
Supabase PostgreSQL
↓
Analytics Engine
↓
FastAPI REST APIs
↓
Swagger UI

---

## Tech Stack

### Backend

- Python
- FastAPI

### Data Processing

- Pandas
- NumPy
- Faker

### Database

- PostgreSQL
- Supabase
- SQLAlchemy

### Cloud

- AWS S3
- AWS IAM

### DevOps

- Docker
- Docker Compose
- GitHub Actions

### API Testing

- Swagger UI
- Postman

---

## Project Structure

cloud-data-analytics-pipeline/

├── app/
│ ├── analytics/
│ ├── api/
│ ├── database/
│
├── scripts/
│ ├── generate_data.py
│ ├── ingest.py
│ ├── validate.py
│ ├── transform.py
│ ├── load.py
│
├── data/
│ ├── raw/
│ ├── processed/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md

---

## API Endpoints

### Revenue Analytics

GET /revenue

Returns total revenue generated.

---

### Monthly Revenue

GET /monthly-revenue

Returns month-wise revenue aggregation.

---

### Top Products

GET /top-products

Returns highest-performing products.

---

### Top Customers

GET /top-customers

Returns highest-value customers.

---

### Dashboard Metrics

GET /dashboard

Returns aggregated business KPIs.

---

## Local Setup

Clone Repository

git clone <repository-url>

cd cloud-data-analytics-pipeline

Create Virtual Environment

python -m venv venv

Activate Virtual Environment

Windows

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run Application

python -m uvicorn app.main:app --reload

Open Swagger UI

http://127.0.0.1:8000/docs

---

## Business Impact

- Automated ETL pipeline processing 50,000+ records
- Cloud-native data lake architecture using AWS S3
- Reduced manual data preparation through automated validation and transformation
- Exposed analytics through production-style REST APIs
- Demonstrated end-to-end data engineering workflow

---

## Future Enhancements

- Apache Airflow Workflow Orchestration
- Real-Time Streaming Pipelines
- Kafka Integration
- Kubernetes Deployment
- Automated Monitoring with CloudWatch
- Data Warehouse Integration

---

## Author

A Vinay Kumar

Computer Science and Business Systems

Software Engineering | Data Engineering | Cloud Analytics
