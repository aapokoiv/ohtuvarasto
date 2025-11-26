from flask import Flask, render_template, request, redirect, url_for
from varasto_service import VarastoService

app = Flask(__name__)
varasto_service = VarastoService()


@app.route('/')
def index():
    varastot = varasto_service.hae_kaikki_varastot()
    return render_template('index.html', varastot=varastot)


@app.route('/luo', methods=['GET', 'POST'])
def luo_varasto():
    if request.method == 'POST':
        try:
            nimi = request.form.get('nimi', '')
            tilavuus = float(request.form.get('tilavuus', 0))
            alku_saldo = float(request.form.get('alku_saldo', 0))
            varasto_service.luo_varasto(nimi, tilavuus, alku_saldo)
        except ValueError:
            pass
        return redirect(url_for('index'))
    return render_template('luo_varasto.html')


@app.route('/varasto/<int:varasto_id>')
def nayta_varasto(varasto_id):
    varasto_data = varasto_service.hae_varasto(varasto_id)
    if not varasto_data:
        return redirect(url_for('index'))
    return render_template('varasto.html',
                           varasto_id=varasto_id,
                           varasto_data=varasto_data)


@app.route('/varasto/<int:varasto_id>/lisaa', methods=['POST'])
def lisaa_varastoon(varasto_id):
    try:
        maara = float(request.form.get('maara', 0))
        varasto_service.lisaa_varastoon(varasto_id, maara)
    except ValueError:
        pass
    return redirect(url_for('nayta_varasto', varasto_id=varasto_id))


@app.route('/varasto/<int:varasto_id>/ota', methods=['POST'])
def ota_varastosta(varasto_id):
    try:
        maara = float(request.form.get('maara', 0))
        varasto_service.ota_varastosta(varasto_id, maara)
    except ValueError:
        pass
    return redirect(url_for('nayta_varasto', varasto_id=varasto_id))


if __name__ == '__main__':
    app.run()
