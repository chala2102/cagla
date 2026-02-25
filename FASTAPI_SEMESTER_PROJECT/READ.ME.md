

## Project Description

For this final project, I built a small Task Manager API using FastAPI. The idea was to create a system where tasks can be added, viewed, updated, and deleted through API endpoints.

Instead of using a database, I used a simple `tasks.txt` file to store the data in JSON Lines format. Each task is saved on its own line, which makes it easy to read and keeps the data even if the server is stopped and started again.

This project helped me understand how backend systems work behind the scenes, especially how APIs handle requests and how data can be stored and managed without a database. It was also good practice for working with FastAPI and organizing a small backend project from scratch.




Features

The API includes the following functionality:

Create a new task

View all tasks

View a single task by ID

Update a task

Delete a task

Delete all tasks

Filter tasks by completion status

Search tasks by keyword

View task statistics (total, completed, pending, percentage)



Additional small features I added:

Task priority (low, medium, high)

Notes field

Created and updated timestamps



/////How to Run the Project//////

Open terminal in the project folder

Create virtual environment

python -m venv venv

Activate virtual environment

venv\Scripts\activate

Install dependencies

pip install fastapi uvicorn

Run the server

python -m uvicorn main:app --reload

Open in browser

http://127.0.0.1:8000/docs


MAKER = CAGLA NUR CELIK :)