from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# GETメソッド、POSTメソッドの追記
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("top.html")

@app.route("/result", methods=["POST"])
def result():
    title = request.form["option"]

    if title == "お椀":
        photo1 = "static/images/お椀photo1.jpg"
        photo2 = "static/images/お椀photo2.jpg"
        photo3 = "static/images/お椀photo3.jpg"
        photo4 = "static/images/お椀photo4.jpg"
    elif title == "盛皿":
        photo1 = "static/images/盛皿photo1.jpg"
        photo2 = "static/images/盛皿photo2.jpg"
        photo3 = "static/images/盛皿photo3.jpg"
        photo4 = "static/images/盛皿photo4.jpg"
    elif title == "お盆":
        photo1 = "static/images/お盆photo1.jpg"
        photo2 = "static/images/お盆photo2.jpg"
        photo3 = "static/images/お盆photo3.jpg"
        photo4 = "static/images/お盆photo4.jpg"
    elif title == "酒器":
        photo1 = "static/images/酒器photo1.jpg"
        photo2 = "static/images/酒器photo2.jpg"
        photo3 = "static/images/酒器photo3.jpg"
        photo4 = "static/images/酒器photo4.jpg"
    elif title == "箱物":
        photo1 = "static/images/箱物photo1.jpg"
        photo2 = "static/images/箱物photo2.jpg"
        photo3 = "static/images/箱物photo3.jpg"
        photo4 = "static/images/箱物photo4.jpg"
    elif title == "うるし塗り体験":
        photo1 = "static/images/うるし塗り体験photo1.jpg"
        photo2 = "static/images/うるし塗り体験photo2.jpg"
        photo3 = "static/images/うるし塗り体験photo3.jpg"
        photo4 = "static/images/うるし塗り体験photo4.jpg"

    return render_template(
        "second.html", title=title, photo1=photo1, photo2=photo2, photo3=photo3, photo4=photo4
    )


@app.route('/second')
def second():
    return render_template('top.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True, host='0.0.0.0')
