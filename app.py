from flask import Flask, render_template, request
from analysis import process

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    sinewave_resolution = int(request.form['sinewave_resolution'])
    sinewave_frequency = float(request.form['sinewave_frequency'])
    sinewave_amplitude = float(request.form['sinewave_amplitude'])
    sinewave_dc_offset = float(request.form['sinewave_dc_offset'])
    quant_resolution = int(request.form['quant_resolution'])
    sample_catcher_frequency = int(request.form['sample_catcher_frequency'])

    plot_filename, levels, delta = process(sinewave_resolution, 
                                      sinewave_frequency,
                                      sinewave_amplitude,
                                      sinewave_dc_offset,
                                      quant_resolution,
                                      sample_catcher_frequency)

    return render_template('result.html', plot_filename=plot_filename, levels=levels, delta=delta)

if __name__ == '__main__':
    app.run(debug=True)