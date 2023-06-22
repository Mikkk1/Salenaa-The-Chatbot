# Chatbot Project

The Chatbot Project is a web application that allows users to interact with a chatbot and perform various tasks. This project is built using Flask, a lightweight web framework for Python, and incorporates features like user registration, authentication, password reset, and natural language processing.

## Features

- User Registration:
  - Users can create new accounts by providing their email, name, and password.
  - Input validation ensures the entered data meets the required criteria.
  - User IP addresses are recorded and stored in the database.

- User Login:
  - Registered users can log in using their email and password.
  - Passwords are securely hashed and stored in the database.
  - The user's IP address is checked and updated if it has changed since the last login.

- User Logout:
  - Logged-in users can log out from their accounts.

- Password Reset:
  - Users who forget their passwords can request a password reset.
  - An email is sent to the user's registered email address containing a one-time password (OTP).
  - The user verifies their identity by entering the OTP and can then reset their password.

- AIML-Based Chatbot:
  - The chatbot utilizes the AIML (Artificial Intelligence Markup Language) library.
  - AIML allows for the creation of patterns and templates to generate responses.
  - AIML files in the "MyBot" directory are used for learning and generating responses.

- Web Scraping:
  - The application includes a web scraping feature to fetch information from websites.
  - Web scraping is triggered when user queries contain specific keywords.
  - BeautifulSoup library is used for parsing HTML and extracting data from websites.

- Sentiment Analysis:
  - The application employs sentiment analysis using the VADER tool from the NLTK library.
  - Sentiment analysis is used to understand the user's mood and generate appropriate responses.

- User Data Storage:
  - User data, including email, name, password, IP address, and chat history, is stored in a database.
  - The database enables personalized interactions and maintains user-specific information.

- Chatbot Interface:
  - Authenticated users can engage in conversations with the chatbot.
  - Natural language processing techniques are used to understand and respond to user queries.
  - The chatbot's responses are generated based on predefined rules or machine learning algorithms.

- Social Network Analysis:
  - The chatbot includes a social network analysis feature that allows users to establish relationships with other users.
  - Users can specify their relationships (e.g., father, mother, friend), and the chatbot stores and maintains this relationship data.
  - The social network analysis feature enables the chatbot to provide information about user relationships and perform actions based on defined relationships.

## Installation

1. Clone the repository:
   ```
    https://github.com/Mikkk1/Salena-The-Chatbot/
   ```

2. Navigate to the project directory:
   ```
   cd chatbot-project
   ```

3. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Create a database (e.g., Neo4j) and note down the connection details.
   - Configure the database connection settings in the `config.py` file.

5. Configure email settings:
   - Specify the SMTP server details in the `auth.py` file for sending password reset emails.
   - Provide a valid email address and credentials for the SMTP server.

6. Run the application:
   ```
   python main.py
   ```

7. Access the application:
   - Open a web browser and visit `http://localhost:5000` to access the chatbot application.

## Usage

1. Registration:
   - Click on the "Register" link

 on the login page.
   - Fill in the required details (email, name, password) and submit the form.
   - If successful, you will be redirected to the login page.

2. Login:
   - Enter your registered email and password on the login page.
   - Click the "Login" button to log in.
   - If the credentials are valid, you will be redirected to the home page.

3. Password Reset:
   - If you forget your password, click on the "Forgot Password" link on the login page.
   - Enter your registered email address and submit the form.
   - An email containing an OTP (one-time password) will be sent to your email address.
   - Enter the OTP on the verification page to proceed.
   - Once verified, you can enter a new password and confirm it to reset your password.

## File Structure

The project has the following file structure:

- `app.py`: The main Flask application file that defines routes and initializes the application.
- `auth.py`: A Flask Blueprint that handles user authentication and related functionality.
- `config.py`: Configuration file that stores various settings for the application, such as database connection details and email server settings.
- `database.py`: Contains functions for interacting with the database, including user-related operations.
- `userData.py`: A module for storing user-specific data throughout the session.
- `templates/`: Directory containing HTML templates for different pages/views.
- `static/`: Directory for static files such as CSS stylesheets and JavaScript files.
- `requirements.txt`: A file listing all the required Python packages and their versions.

## Dependencies

The project relies on the following Python packages (specified in `requirements.txt`):

- Flask: A web framework for building the application.
- Flask-Login: Handles user session management and authentication.
- Werkzeug: Provides password hashing and verification functionality.
- Requests: Allows making HTTP requests to retrieve the user's IP address.
- Email: Provides functionality for sending emails.
- SMTPlib: A library for sending emails using the Simple Mail Transfer Protocol (SMTP).
- Random: Generates random strings for OTP generation.
- String: Provides string manipulation functions.

## Conclusion

The Chatbot Project is a web application that enables users to register, log in, reset passwords, and interact with a chatbot. It incorporates user authentication, database operations, email functionality, natural language processing, web scraping, sentiment analysis, and social network analysis. The documentation provides an overview of the project, installation instructions, usage guidelines, and information about the file structure and dependencies.

Enjoy using the Chatbot application! If you have any further questions or need assistance, please refer to the project's documentation or reach out at:

sarimzahid991@gmail.com
