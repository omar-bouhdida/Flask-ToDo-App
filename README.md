# To-Do App

A simple yet powerful To-Do application that allows users to manage their tasks efficiently. This project is built using Flask for the backend and HTML/CSS for the frontend, providing a clean and responsive user interface.

## Features

- **Add new tasks**: Quickly add tasks to your to-do list.
- **Mark tasks as completed**: Track progress by marking tasks as done.
- **Edit tasks**: Update task details anytime.
- **Delete tasks**: Remove tasks that are no longer needed.
- **Responsive UI**: A user-friendly interface that works seamlessly on all devices.

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)

## Installation

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Git

### Setup

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd todo-app
    ```

2. **Create and activate a virtual environment**:

    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

5. **Open your browser and navigate to**:
    ```
    http://127.0.0.1:5000/
    ```

## API Endpoints (if applicable)

- **GET** `/tasks`: Retrieve all tasks
- **POST** `/tasks`: Create a new task
- **PUT** `/tasks/:id`: Update a specific task
- **DELETE** `/tasks/:id`: Delete a specific task

## Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bugfix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Commit your changes**:
    ```bash
    git commit -m "Add your meaningful commit message here"
    ```
4. **Push your branch**:
    ```bash
    git push origin feature/your-feature-name
    ```
5. **Open a pull request** with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions, feedback, or collaboration opportunities, feel free to reach out:

- **Name**: Omar BOUHDIDA
- **Email**: omarbouhdiida@gmail.com
