from flask import Flask, request, jsonify
import csv
    
app = Flask(__name__)

file_name = "database.csv"

@app.route("/")
def hello_world():
    return "Welcome to the Employee Info API! Use /birthdays or /anniversaries with query parameters."

@app.route("/birthdays", methods=["GET"])
def get_birthdays():

    month = request.args.get("month")
    department = request.args.get("department")

    birthday_total = 0
    birthday_names = []

    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                birthday = row['Birthday']
                department_group = row['Department']
                if month.lower() in birthday.lower():
                    if department.lower() in department_group.lower():
                        birthday_total+=1
                        birthday_name = f"{row['Birthday']}, {row['Name']}"
                        birthday_names.append(birthday_name)
    except FileNotFoundError:
        return jsonify({"error": f"File '{file_name}' not found."}), 500  

    if birthday_total == 0:
        return jsonify({"message": "No birthdays found for the given criteria."}), 404
    return jsonify({"total": birthday_total, "names": birthday_names})  

@app.route("/anniversaries", methods=["GET"])
def get_anniversaries():

    month = request.args.get("month")
    department = request.args.get("department")

    anniversary_total = 0
    anniversary_names = []

    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                anniversary = row['Hiring']
                department_group = row['Department']
                if month.lower() in anniversary.lower():
                    if department.lower() in department_group.lower():
                        anniversary_total+=1
                        anniversary_name = f"{row['Hiring']}, {row['Name']}"
                        anniversary_names.append(anniversary_name)
    except FileNotFoundError:
        return jsonify({"error": f"File '{file_name}' not found."}), 500  
    
    if anniversary_total == 0:
        return jsonify({"message": "No anniversaries found for the given criteria."}), 404
    return jsonify({"total": anniversary_total, "names": anniversary_names})


if __name__ == '__main__':
    app.run()