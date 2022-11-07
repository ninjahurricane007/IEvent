
# College Event Portal

This is a web application that is built using Django Framework. Front End is built using HTML & CSS and the database used is MongoDB. This web application can be used to bring all the college fests and events into a single place. There are mainly 3 users in this system, Admin, Coordinator and Student. The admin can track all the user activities and make other user as coordinators. The event coordinators can host events and track participations in their events. The normal users or participants can view and register for events and track the registered events.





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

Home Page

![Home Page](https://user-images.githubusercontent.com/67139570/200377203-43fa1681-a64f-46be-a441-03c4bb2f4a9b.jpg)

Sign Up Page

![Sign Up](https://user-images.githubusercontent.com/67139570/200377407-93204630-7aaf-4766-9ece-0e658972bcec.jpg)

Sign In Page

![Sign In](https://user-images.githubusercontent.com/67139570/200377463-2903ea07-65c6-45df-a06e-e4c9b892e0b1.jpg)

Fest Creation Page

![Fest Creation](https://user-images.githubusercontent.com/67139570/200377589-60918539-4088-4e82-b1bf-0d2b078fc518.jpg)

Fest Page

![Fests](https://user-images.githubusercontent.com/67139570/200377659-08e3db24-124d-4f09-a685-70542e775675.jpg)

Event Creation Page

![Event Creation](https://user-images.githubusercontent.com/67139570/200377694-8dd0a89c-e68d-451a-87b8-b0b6d2ff4029.jpg)

Event Page

![Events](https://user-images.githubusercontent.com/67139570/200377752-f676de5c-0ada-494a-9577-0fd9b0169237.jpg)

Event Details Page

![Details](https://user-images.githubusercontent.com/67139570/200377790-72d104bb-ab4a-4be5-b674-43a2db0172f5.jpg)

Event Checkout Page

![Checkout](https://user-images.githubusercontent.com/67139570/200377844-a0d42b49-29e3-40ce-bcf0-9911aa4ef532.jpg)

Payment Gateway

![Payment Gateway](https://user-images.githubusercontent.com/67139570/200377886-415d78af-1723-48fc-adfc-11bf899188d1.jpg)

Registered Events Page

![Registered](https://user-images.githubusercontent.com/67139570/200377968-02d4f9db-c0ff-4773-8d5d-e3d94eeaad74.jpg)

Coordinator Panel

![Coordinator](https://user-images.githubusercontent.com/67139570/200378006-08cd0994-dbe5-44e6-b162-0d2bdc4ec0a4.jpg)

Profile Page

![Profile](https://user-images.githubusercontent.com/67139570/200378080-ccaba1ff-6f5d-409f-a300-697bc0c636a6.jpg)

Admin Panel

![Admin](https://user-images.githubusercontent.com/67139570/200378123-e6b5a9a5-9da2-476a-84d2-317ab284ac40.jpg)






