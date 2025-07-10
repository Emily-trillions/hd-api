from flask import Flask, request, jsonify
from datetime import datetime
import hades_hd as hd

app = Flask(__name__)

@app.route("/get-chart", methods=["POST"])
def get_chart():
    data = request.json

    try:
        birth_date = data["birth_date"]  # format: DD-MM-YYYY
        birth_time = data["birth_time"]  # format: HH:MM (24h)
        birth_location = data["birth_location"]  # e.g. "Plymouth, Ohio, USA"

        # Combine into datetime
        birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%d-%m-%Y %H:%M")

        # Generate HD chart (placeholder – customize with hades-hd)
        chart = hd.Chart(
            birth_datetime=birth_datetime,
            city=birth_location
        )

        result = {
            "type": chart.hd_type,
            "authority": chart.authority,
            "profile": chart.profile,
            "defined_centers": chart.defined_centers,
            "channels": chart.channels,
            "gates": chart.gates,
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
