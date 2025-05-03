# Daycare Management System

A **Daycare Management System** built with Python and FastAPI to manage teachers and their data using CSV-based persistence.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete teacher, Students, Classrooms and Class records.
- **CSV Persistence**: Data is stored and retrieved from CSV files.
- **FastAPI Integration**: RESTful API endpoints for managing teacher data.
- **Error Handling**: Handles duplicate entries, missing records, and invalid requests.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ezequielsan/daycareManagementSystem.git
   cd daycareManagementSystem
   ```
2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install fastapi uvicorn pydantic
    ```

## Usage

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```


2. Access the API documentation:
    Open your browser and go to http://127.0.0.1:8000/docs for the Swagger UI.

3. Use the following endpoints:
    ```
    GET /teachers: Retrieve all teachers.
    GET /teachers/{teacher_id}: Retrieve a specific teacher by ID.
    POST /teachers: Add a new teacher.
    PUT /teachers/{teacher_id}: Update an existing teacher.
    DELETE /teachers/{teacher_id}: Delete a teacher by ID.
    ```
