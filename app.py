from flask import Flask, render_template, request, redirect
import sqlite3 as s

carsales = Flask(__name__)

def getconnect():
    conn = s.connect('Database.db')
    return conn

@carsales.route("/")
def main():
    cars = []
    conn = getconnect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TblCars")
    for row in cursor.fetchall():
        cars.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
    conn.close()
    return render_template("carlist.html", cars=cars)

@carsales.route("/addcar", methods=['GET', 'POST'])
def addcar():
    if request.method == 'GET':
        return render_template("addcar.html", car={})
    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form["name"]
        year = int(request.form["year"])
        price = float(request.form["price"])
        conn = getconnect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TblCars VALUES (?, ?, ?, ?)", [id, name, year, price])
        conn.commit()
        conn.close()
        return redirect('/')

@carsales.route('/updatecar/<int:id>', methods=['GET', 'POST'])
def updatecar(id):
    cr = []
    conn = getconnect()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM TblCars WHERE id = ?", [id])
        row = cursor.fetchone()
        cr.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
        conn.close()
        return render_template("addcar.html", car=cr[0])
    if request.method == 'POST':
        name = request.form["name"]
        year = int(request.form["year"])
        price = float(request.form["price"])
        cursor.execute("UPDATE TblCars SET name = ?, year = ?, price = ? WHERE id = ?", [name, year, price, id])
        conn.commit()
        conn.close()
        return redirect('/')

@carsales.route('/deletecar/<int:id>')
def deletecar(id):
    conn = getconnect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TblCars WHERE id = ?", [id])
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == "__main__":
    carsales.run(debug=True)
