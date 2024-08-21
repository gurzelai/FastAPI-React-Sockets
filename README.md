# FastAPI and React WebSocket Application

This repository contains a simple web application built with FastAPI for the backend and React for the frontend. The application demonstrates real-time data updates using WebSockets.

## Overview

The application features a FastAPI backend that maintains a list of machines with their respective names and values. Clients can add new machines via a POST request, and all connected WebSocket clients will be notified of these changes in real-time.

## Backend (FastAPI)

### Endpoints

- `POST /machines/`: Adds a new machine to the list.
- `GET /machines/`: Retrieves the current list of machines.
- `WebSocket /ws/machines`: Maintains a WebSocket connection for real-time updates.

### Key Files

- `main.py`: Contains the FastAPI application setup and endpoints.

## Frontend (React)

### Functionality

- Establishes a WebSocket connection to receive real-time updates about machines.
- Displays the list of machines with their names and values in the browser.

### Key Files

- `App.js`: Contains the React component that handles WebSocket communication and displays machine data.

## Setup

### Prerequisites

- Python 3.7+
- Node.js and npm

### Backend Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/gurzelai/fastapi-react-sockets.git
    ```

2. Navigate to the backend directory and install dependencies:
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:
    ```bash
    python main.py
    ```
Do not close this terminal or window.

### Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Run the React application:
    ```bash
    npm start
    ```
Do not close this terminal or window.

## Usage

1. Start the FastAPI server.
2. Start the React application.
3. Open your browser and navigate to [http://localhost:3000](http://localhost:3000) to view the frontend.
4. Use tools like Postman or a similar tool to interact with the API endpoints.

## License

This project is licensed under the MIT License.
