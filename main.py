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

if __name__ == "__main__"
	app.run(debug=True)
