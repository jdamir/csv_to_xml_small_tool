from flask import Flask, render_templates, request
from wtforms import Form, validators, StringField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'type_your_secret_key_here'

class DataForm(Form):

	Quantity_on_pallet = StringField('Quantity', validators=[validators.required(), validators.Length(min=1, max=4)])
	PalletNumber = StringField('PalletNumber', validators=[validators.required(), validators.Length(min=19, max=19)])
	Purchase_order = StringField('PurchaseOrder', validators=[validators.required(), validators.Length(min=10, max=10)])
	Shipment_id = StringField('ShipmentId', validators=[validators.required(), validators.Length(min=10, max=10)])


@app.route("/", methods=["POST"])
def data():
	form = DataForm(request.form)

	global Quantity_on_pallet
	global StartPalletNumber
	global Purchase_order
	global ShipmentId

	if request.method == 'POST':
		Quantity_on_pallet=request.form['Quantity_on_pallet']
		StartPalletNumber=request.form['PalletNumber']
		Purchase_order=request.form['Purchase_order']
		Shipment_id=request.form['Shipment_id']
		Quantity_on_pallet = int(Quantity_on_pallet)
		StartPalletNumber = int(StartPalletNumber)


	return render_templates("data.html", form=form)


@app.route("/index", methods=["POST"])
def index():
	if request.method == 'POST':
		f = request.files['file'].read()
		data_csv = str(f.decode("utf-8")).split('\r\n')
		data_csv.pop()
		data.sort()

		def iter(grp, q):
			return [grp[i:i + q] for i in range(0, len(grp), q)]

		keys = []
		groups = []
		for k, g in itertools.groupby(data_csv, key = lambda x: x[2:26]):
			keys.append(k)
			groups.append(list(g))

		for i in range(len(keys)):
			groups[i]=(iter(groups[i], Quantity_on_pallet))

		cases_a = [item for sublist in groups for item in sublist]


		StopPalletNumber = StartPalletNumber - len(cases_a)

		Pallets = list(range(StartPalletNumber, StopPalletNumber, -1))
		Pallets = [str(item) for item in Pallets]
		quantity = str(len(Pallets))




if __name__ == "__main__"
	app.run(debug=True)
