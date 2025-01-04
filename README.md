# Django Project Setup and Run Instructions

## Project Overview
This project provides basic functionality for user authentication and company management, including login, logout, user detail viewing/editing, and company detail viewing.

## Prerequisites
- Python (3.8 or later)
- pip (Python package manager)
- Git
- A virtual environment manager (e.g., `venv`)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   ./run.sh
   ```

## Single Run Command
To make it easier to set up and run the project, a `run.sh` file is provided. It performs the following tasks:
- Installs dependencies
- Applies migrations
- Starts the Django development server

### Usage
Ensure the script has executable permissions:
```bash
chmod +x run.sh
```
Then execute the script:
```bash
./run.sh
```

## Project Structure
- `manage.py`: Django's management script.
- `app_name/`: The application directory containing models, views, templates, and forms.
- `requirements.txt`: Lists Python dependencies for the project.
- `run.sh`: A script to set up and run the project.
- `.gitignore`: Specifies files and directories to exclude from Git tracking.

## Notes
- Update the `<repository-url>` in the commands above with your GitHub repository URL.
- Modify the `run.sh` script as needed for custom configurations.

---
