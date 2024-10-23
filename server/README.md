# NPI Backend

This is the backend for the NPI (Notation Polonaise Inverse) calculator application. It is built using **FastAPI**, **PostgreSQL**, and **Docker**.

## Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

### 1. Clone the Repository

```bash
   git clone https://github.com/wassb92/rpn-calculator.git
   cd server
```

### 2. Set Up Environment Variables

You can either use the default configuration or provide your own in a `.env` file or through environment variables.

- **`DATABASE_URL`**: URL for connecting to the PostgreSQL database.

If `DATABASE_URL` is not set, the application will use the default value: `postgresql+asyncpg://postgres:postgres@localhost:5432/npi_db`.

### 3. Build and Run the Project with Docker

To start the backend using Docker, run:

```bash
docker-compose up --build
```

This will:

- Pull the required Docker images.
- Build the Docker container for the FastAPI backend.
- Set up a PostgreSQL container.
- Start the application on `http://localhost:8000`.

### 4. Stopping the Services

To stop the services, run:

```bash
docker-compose down
```

## API Endpoints

Once the application is running, you can access the API documentation through FastAPI's interactive docs:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Database

The backend uses PostgreSQL to store data. The database is automatically configured when the Docker containers are launched.

If you want to access the database directly:

- **Host**: `localhost`
- **Port**: `5432`
- **User**: `postgres`
- **Password**: `postgres`
- **Database**: `npi_db`

## Development

If you wish to develop or test the application locally without Docker, follow these steps:

### 1. Install Dependencies

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Set Up PostgreSQL

Make sure you have a local instance of PostgreSQL running. Update the `DATABASE_URL` in your environment variables or in the code if needed.

### 3. Start the FastAPI Application

Run the FastAPI app locally:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`.

## Testing

You can run tests (if any) using:

```bash
pytest
```

## Contact

For any inquiries, please contact **Wassini Bouzidi** at [wassini.bouzidi@epitech.eu](mailto:wassini.bouzidi@epitech.eu).
