from flask import Flask, render_template

server = Flask(
    __name__, 
    static_folder='./static', 
    template_folder='./templates'
    )

@server.route('/')
def index():
    return render_template("index.html.j2")

@server.route('/profile')
def profile():
    return render_template("profile.html")

@server.route('/settings')
def settings():
    return render_template("settings.html")

@server.route('/courses')
def courses():
    return render_template("courses.html")

@server.route('/course/<course_id>')
def course(course_id=None):
    return render_template("course.html", COURSE_ID=course_id)

@server.route('/achievements')
def achievements():
    return render_template("achievements.html")








__all__=['server']
