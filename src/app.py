from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from transform_data import read_files
from pymysql import IntegrityError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:password@localhost/gl-test"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


# departments table
class departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(255), unique=True)

    def __init__(self, id, department):
        self.title = id
        self.department = department


with app.app_context() as ctx:
    db.create_all()


class departmentsSchema(ma.Schema):
    class Meta:
        fields = ("id", "department")


department_schema = departmentsSchema()
departments_schema = departmentsSchema(many=True)


# jobs table
class jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(255), unique=True)

    def __init__(self, id, job):
        self.title = id
        self.job = job


with app.app_context() as ctx:
    db.create_all()


class jobsSchema(ma.Schema):
    class Meta:
        fields = ("id", "department")


job_schema = jobsSchema()
job_schema = jobsSchema(many=True)


# hired table
class hired_employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    datetime = db.Column(db.String(255))
    department_id = db.Column(db.Integer)
    job_id = db.Column(db.Integer)

    def __init__(self, id, name, datetime, department_id, job_id):
        self.title = id
        self.name = name
        self.datetime = datetime
        self.department_id = department_id
        self.job_id = job_id


with app.app_context() as ctx:
    db.create_all()


class hired_employeesSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "datetime", "department_id", "job_id")


job_schema = hired_employeesSchema()
job_schema = hired_employeesSchema(many=True)

# Create / Insert Tables


@app.route("/create", methods=["POST"])
def create_task():

    file = request.json["filename"]
    table = request.json["table"]

    data = read_files(file)

    if table == "departments":
        for n in range(len(data)):
            id = data[n]["id"]
            department = data[n]["department"]
            try:
                new_task = departments(id, department)
                db.session.add(new_task)
                db.session.commit()
                return f"writing {len(data)} records on {table} table"
            except IntegrityError:
                return f"duplicate data for {table} table"

    if table == "jobs":

        for n in range(len(data)):
            id = data[n]["id"]
            job = data[n]["job"]
            try:
                new_task = jobs(id, job)
                db.session.add(new_task)
                db.session.commit()
                return f"writing {len(data)} records on {table} table"
            except IntegrityError:
                return f"duplicate data for {table} table"

    if table == "hired_employees":

        for n in range(len(data)):
            id = data[n]["id"]
            name = data[n]["name"]
            datetime = data[n]["datetime"]
            department_id = data[n]["department_id"]
            job_id = data[n]["job_id"]
            new_task = hired_employees(id, name, datetime, department_id, job_id)
            db.session.add(new_task)
            db.session.commit()

        return f"writing {len(data)} records on {table} table"

    else:

        return f"table {table} does not exist"


if __name__ == "__main__":
    app.run(debug=True)
