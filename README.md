# TELEGRAM MESSAGE SENDER
Pack of tests for testing Ajax mobile app

## Prerequisites
- Python 3.7 or higher
- Appium
- Appium-Python-Client
- Pytest

## Setup
1. Clone the repository:

    ```bash
    git clone 
    ```
2. Create virtual environment:
   ```
    python -m venv venv
   ```
   and activate it 
   <br>
   <br>
    - on windows:
    ```
    venv\Scripts\activate
    ```   
    - on Mac:
    ```
    source venv/bin/activate
   ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a .env file in the root directory of the project and add the following:
    ```
    VALID_PASSWORD=password for your valid login
    ```

## Usage
Run the script by executing the following command:

```bash
pytest
```

