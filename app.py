from flask import Flask, render_template, request, redirect, url_for
from database import get_connection

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        patient_name = request.form["patient_name"]
        age = request.form["age"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        disease = request.form["disease"]
        doctor = request.form["doctor"]
        admission_date = request.form["admission_date"]

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO patients
        (patient_name, age, gender, phone, disease, doctor, admission_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            patient_name,
            age,
            gender,
            phone,
            disease,
            doctor,
            admission_date
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("hospital"))

    return render_template("index.html")


@app.route("/hospital")
def hospital():
    return render_template("hospital.html")


if __name__ == "__main__":
    app.run(debug=True)