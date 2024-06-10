from src.DiamondPricePrediction.pipelines.prediction_pipeline import CustomData
from src.DiamondPricePrediction.pipelines.prediction_pipeline import PredictPipeline
from src.DiamondPricePrediction.logger import logging
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        carat = float(request.form.get('carat'))
        depth = float(request.form.get('depth'))
        table = float(request.form.get('table'))
        x = float(request.form.get('x'))
        y = float(request.form.get('y'))
        z = float(request.form.get('z'))
        cut = request.form.get('cut')
        color = request.form.get('color')
        clarity = request.form.get('clarity')

        logging.info("Received the data from the form")
        logging.debug(f"carat: {carat}, depth: {depth}, table: {table}, x: {x}" \
                      f"y: {y} z: {z}, color: {color}, clarity: {clarity}, cut: {cut}")

        custom_data_obj = CustomData(carat, depth, table, x, y, z, cut, color, clarity)
        single_test_data = custom_data_obj.get_data_as_dataframe()

        single_predict_pipeline_obj = PredictPipeline()
        predicted_price = single_predict_pipeline_obj.predict(single_test_data)
        predicted_price = round(predicted_price[0], 2)

        return render_template("result.html", final_result=predicted_price)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)