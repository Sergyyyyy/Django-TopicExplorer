from symtable import Class

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def testing(request):
#     return HttpResponse("<h1>Hello World!</h1>")

class Model:
    def __init__(self, TopicName, Description):
        self.TopicName = TopicName
        self.Description = Description

topics = {"Models" : "Handles your database structure and data.",
        "Views" : "The logic that processes requests and returns responses.",
        "Templates" : "The HTML files that display data to the user.",
        "URLs" : "The address book that routes requests to views.",
        "Admin" : "A built-in interface to manage your data easily.",
        "MVT" : "Stands for Model-View-Template architecture.",
        "ORM" : "Allows you to talk to a database using Python code.",
        "Migrations" : "Propagates changes you make to models to the database.",
        "Forms" : "Handles user input and validation safely.",
        "Middleware" : "Hooks into Django's request/response processing."}



def Home1(request):
    pass




"""
Models - Handles your database structure and data.
Views - The logic that processes requests and returns responses.
Templates - The HTML files that display data to the user.
URLs - The address book that routes requests to views.
Admin - A built-in interface to manage your data easily.
MVT - Stands for Model-View-Template architecture.
ORM - Allows you to talk to a database using Python code.
Migrations - Propagates changes you make to models to the database.
Forms - Handles user input and validation safely.
Middleware - Hooks into Django's request/response processing.
"""


"""
    def home(request):
    c1 = Course("Django Web Development", 14)
    c2 = Course("Python Basics", 4)
    c3 = Course("Database Management", 😎
    course_list = [c1, c2, c3]

    # We look at the URL for a 'letter'. If not found, we use 'a'.
    search_char = request.GET.get('letter', 'a')

    display_data = []
    for c in course_list:
        count_result = c.count_letter(search_char)
        display_data.append({'course': c, 'count': count_result})

    return render(request, 'index.html', {
        'data_list': display_data,
        'total': len(course_list),
        'search_letter': search_char
    })
"""

"""
<body>
    <h1>Our Academic Schedule</h1>

    <p><em>To search for a different letter, add <strong>?letter=your_letter</strong> to the end of the URL.</em></p>
    <p>Currently searching for: <strong>{{ search_letter }}</strong></p>

    <ul>
        {% for item in data_list %}
            <li>
                <strong>{{ item.course.title }}</strong>: {{ item.course.duration }} weeks
                <br>
                <small>The letter "{{ search_letter }}" appears
                {{ item.count }} times in this title.</small>
            </li>
        {% endfor %}
    </ul>

    <hr>
    <p>Total Courses Enrolled: {{ total }}</p>
</body>
"""