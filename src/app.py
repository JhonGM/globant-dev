from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from transform_data import read_files

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:password@localhost/flaskmysql"
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

#Create / Insert Tables

@app.route("/create", methods=["POST"])
def create_task():

    file = request.json["filename"]
    table = request.json["table"]

    if table == "departments":
        json_data = read_files(file)
        for n in range(len(json_data)):
            id = json_data[n]["id"]
            department = json_data[n]["department"]
            new_task = departments(id, department)
            db.session.add(new_task)
            db.session.commit()

        return department_schema.jsonify(new_task)

    if table == "jobs":

        json_data = read_files(file)
        for n in range(len(json_data)):
            id = json_data[n]["id"]
            job = json_data[n]["job"]
            new_task = jobs(id, job)
            db.session.add(new_task)
            db.session.commit()

        return department_schema.jsonify(new_task)
    
    if table == "hired_employees":

        json_data = read_files(file)
        for n in range(len(json_data)):
            id = json_data[n]["id"]
            name = json_data[n]["name"]
            datetime = json_data[n]["datetime"]
            department_id = json_data[n]["department_id"]
            job_id = json_data[n]["job_id"]
            new_task = hired_employees(id, name, datetime, department_id, job_id)
            db.session.add(new_task)
            db.session.commit()

        return department_schema.jsonify(new_task)
    
    else:
        
        return f'table {table} not exist'


@app.route("/departments", methods=["GET"])
def get_tasks():
    all_task = departments.query.all()
    result = departments_schema.dump(all_task)

    return jsonify(result)


@app.route("/departments/<id>", methods=["GET"])
def get_task(id):
    task = departments.query.get(id)
    return department_schema.jsonify(task)


if __name__ == "__main__":
    app.run(debug=True)
