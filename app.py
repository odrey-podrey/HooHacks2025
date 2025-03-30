from flask import Flask, render_template, request, Response
import scraper

app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def home():
    if (request.method == "GET"):
        return render_template("frontEnd.html")
    
    zip_code = request.form.get("user_zipcode")
    rep_name = scraper.rep_from_zip(zip_code)
    print(rep_name)
    party, district = scraper.dist_party_from_zip(zip_code)
    print(party)
    print(district)


    if rep_name != "invalid":
        return render_template("informationTab.html", rep_name=rep_name, party=party, district=district)

    return render_template("frontEnd.html", error="Invalid ZIP code.")


if __name__ == '__main__':
    app.debug = True
    app.run()