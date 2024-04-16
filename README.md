# SM_System

<h2>Service Management System</h2>
In this repositories is my first Django project. It is a web based "Computer Service Management System".

<h2>Users of the system</h2>
<ul>
<li>Administrator - superuser</li>
<li>Recipient - Authorized user. Has the right to:</li>
	<ul>
	<li>Fills in the customer data.</li>
	<li>Creates, edits, deletes and includes service cards.</li>
	<li>Edits service data and prices.</li>
	<li>Registered new employees</li>
	</ul>
<li>Technician - Authorized user. Has the right to:</li>
	<ul>
	<li>Repair started</li>
	<li>Finishing repair</li>
	</ul>
<li>Manager - Authorized user - superuser</li>
<li>Client - Not an authorized user. Has the right to:</li>
	<ul><li>To check if his message is ready</li></ul>
</ul>

<h2>DB Models / Tables</h2>
<ul>
    <li>Users - ID, email, password, first_name, last_name, phone_nimber, user_type, profile_picture</li>
    <li>Customers - id, email, first name, last name, phone number</li>
    <li>Service order - id, so_id, accept_date, close_date, client, technician, device_type, device_data, issue_description, status</li>
    <li>Job card – id, order, technician, start_date, end_date, resolution_description, price , completed</li>
</ul>
<h2>Sranitsi</h2>
<ul>
     <li>Home page with information about workshops, services offered and prices</li>
     <li>Working page for the receiver</li>
     <li>Work page for technicians</li>
     <li>Worksheet for manager - not complete</li>
     <li>Order check station</li>
</ul>

<h2>Technologies</h2>

<ul>
<li>Python 3.11</li>	
<li>Django(5.0.3)</li>
<li>Djangorestframework(3.15.0)</li>
<li>HTML, CSS</li>
<li>JavaScript</li>
<li>Postgresql</li>
</ul>

<h2>Installation</h2>

<ol>
<li>Clone repository:<br>
git clone https://github.com/angelovang/SM_System
</li>

<li>Install dependencies:<br>
pip install -r requirements.txt 
</li>

<li>
Set up environment variables
</li>

<li>Apply database migrations: <br>
python manage.py makemigrations <br>
python manage.py migrate
</li>

<li>
Run the server <br>
python manage.py runserver
</li>
</ol>
	
