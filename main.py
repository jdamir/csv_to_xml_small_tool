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




if __name__ == "__main__"
	app.run(debug=True)
