# Python web application using Flask and SQLite database

This is a simple CRUD web application for managing car sales, built using Flask and SQLite.

## Overview

The CarSales web application allows users to:

- **View a list of cars**: Display available cars with details such as ID, Name, Year, and Price.
- **Add a new car**: Provide details to add a new car to the list.
- **Update an existing car**: Modify details of an existing car.
- **Delete a car**: Remove a car from the list.

## Features

- Simple and intuitive interface for managing car sales
- CRUD operations (Create, Read, Update, Delete) for car records
- Persistent storage using SQLite database

## Technologies Used

- **Flask**: A lightweight web framework for Python
- **SQLite**: A lightweight database engine for storing car details


## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/CarSales.git
    cd CarSales
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Initialize the database:**

    The database file (`database.db`) will be created automatically when you run the application for the first time.

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:5000
    ```

## Usage

- **View Cars**: Navigate to the main page to see a list of available cars.
- **Add Car**: Click on the "Add Car" link to add a new car to the list.
- **Update Car**: Click on the "Update" button next to a car to modify its details.
- **Delete Car**: Click on the "Delete" button next to a car to remove it from the list.

## Screenshots

### Home Page

![Home Page](![Uploading Screenshot 2024-08-01 163413.png…]()
)

### Add Car

![Add Car](static/screenshots/add_car.png)

### Update Car

![Update Car](static/screenshots/update_car.png)

### Delete Car

![Update Car](static/screenshots/update_car.png)

---

Feel free to contribute to the project by forking the repository and submitting pull requests. For any issues or feature requests, please open an issue in the repository.

---

Happy Car Sales Management!


