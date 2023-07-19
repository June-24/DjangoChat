# DjangoChat

This repository contains a Django project that demonstrates the usage of Django Channels for building a real-time chat application. Follow the instructions below to get started.

## Prerequisites

Make sure you have the following software installed on your system:

- Python (version 3.7 or higher)
- pip (Python package manager)

## Installation

1. Clone this repository to your local machine or download and extract the ZIP file.

2. Open a terminal or command prompt and navigate to the project's root directory.

3. Create a virtual environment by running the following command:

   ```bash
   python3 -m venv myenv
   ```
4. Activate the Virual environment:
   - on macOS and linux:
   ```bash
   source myenv/bin/activate
   ```
    - on windows:
   ```bash
   myenv\Scripts\activate
   ```
4. Install the project dependencies from the requirements.txt file:
  ```bash
pip install -r requirements.txt
```

## Running the Website
To run the Django website, execute the following command in the project's root directory:
```bash
python manage.py runserver
```
After running the command, the website will be accessible at http://localhost:8000 in your web browser.

# Description
We have used Django Channels for this Project \
A few points about channels in Django and why we have used it
- Usually Django uses HTTP protocol for communication between client and server.
- Channels do not use HTTP, they use protocols like WebSocket.
- Websocket allows bi-directional communication, server can push data to client without waiting for client request.
- This helps when there are multiple clients at once, here in a chat room multiple people can chat at the same time without the need to refresh the page.
- Channels use Django's native async view support, allows us to run HTTP & web socket.
- It also provides integration with Djangos authentication system.

# Images below show the Working of the chat application
## 1. Register Page
![image](https://github.com/June-24/DjangoChat/assets/123622678/c91884d1-15dc-4f3c-9435-009066965247)
![image](https://github.com/June-24/DjangoChat/assets/123622678/c479984a-d052-4473-85d5-182ce00f6790)
## 2. Login Page
![image](https://github.com/June-24/DjangoChat/assets/123622678/1695c8b7-0c6c-4666-af1a-82b81adb8dfd)
## 3. ChatRooms Page
![image](https://github.com/June-24/DjangoChat/assets/123622678/c5917dfa-4505-4156-9762-ed031e722be1)
## 4. A single chatpage
![image](https://github.com/June-24/DjangoChat/assets/123622678/319a926d-1868-4bb8-bee0-29fed15b1961)
## 5.Sending a message
![image](https://github.com/June-24/DjangoChat/assets/123622678/efb0bfa0-1aad-4e55-b2a9-faa46624138d)
![image](https://github.com/June-24/DjangoChat/assets/123622678/080cc8b7-b953-40cf-897c-d4cc3c93d01a)
## 6.Two users sending messages Simultaneously 
![image](https://github.com/June-24/DjangoChat/assets/123622678/0c5ef502-7f27-4415-a6e5-ea7ab498f156)
![image](https://github.com/June-24/DjangoChat/assets/123622678/fde8f031-68b7-4136-aed9-f547c5eb616f)
- as we are using Django Channels, the messages displayed in an instant with no delay or refreshment of pages.
## 7. Logging out
![image](https://github.com/June-24/DjangoChat/assets/123622678/6a6c35cc-29fc-4753-a469-ae155ca3d632)
![image](https://github.com/June-24/DjangoChat/assets/123622678/0ec80105-2c20-4443-ba31-6fbed83e5d3c)

# Database used
- I used the default SQLite database for this project, and all messages and the user details are stored in it.















   


 
