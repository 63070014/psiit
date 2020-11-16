from flask import Flask, render_template #backend ระบบจัดการ database
app = Flask(__name__)

@app.route("/") #url
def hello():
    age = "bubee"
    return render_template("index.html", data=age) #in web

if __name__ == "__main__":
    app.run(debug=True)

