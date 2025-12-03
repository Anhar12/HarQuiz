from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)
API_KEY = "a2596306e3614ddeaea55855250312"

@app.route("/", methods=["GET", "POST"])
def index():
    forecast_data = None
    city = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            try:
                url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&aqi=no&alerts=no"
                res = requests.get(url).json()

                if "error" in res:
                    error_message = res["error"]["message"]
                else:
                    forecast_data = []
                    for item in res["forecast"]["forecastday"]:
                        date_obj = datetime.strptime(item["date"], "%Y-%m-%d")

                        forecast_data.append({
                            "date": item["date"],
                            "day_name": date_obj.strftime("%A"),
                            "temp_day": item["day"]["maxtemp_c"],
                            "temp_night": item["day"]["mintemp_c"],
                            "condition": item["day"]["condition"]["text"]
                        })

            except Exception as e:
                error_message = "Terjadi kesalahan ketika mengambil data cuaca."

    return render_template(
        "index.html",
        forecast=forecast_data,
        city=city,
        error_message=error_message
    )

@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}

if __name__ == "__main__":
    app.run(debug=True)
