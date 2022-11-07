
# College Event Portal

This is a web application that is built using Django Framework. Front End is built using HTML & CSS and the database used is MongoDB. This web application can be used to bring all the college fests and events in a single place. There are mainly 3 users in this system, Admin, Coordinator and Student. The admin can track all the user activities and make other user as coordinators. The event coordinators can host events and track participations in their events. The normal users or participants can view and register for events and track the registered events.




## Features

- User authentication(login & signup)
- View, Create and delete fests and events
- Role based users students and coordinators and admin
- Event register and unregister
- Payment Integration
- Providing email remainders to participants before the event is going to happen
- coordinators get a summary about the participation's and participants in the event.
- participants can track registered events


## Installation

first install virtualenv using pip

```bash
  pip install virtualenv
```

create a virtual environment and activate it

```bash
  virtualenv my_name
  cd my_name
  cd Scripts
  activate
```

install all libraries in requirements.txt after activating environment using the command

```bash
  pip install -r requirements.txt
```

go to project folder runserver
```bash
  python manage.py run server
```

## Screenshots

