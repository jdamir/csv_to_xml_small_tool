from flask import Flask
from wtforms import Form, validators, StringField
from wtforms.validators import DataRequired



class DataForm(Form):
	
	Quantity_on_pallet = StringField('Quantity', validators=[validators.required(), validators.Length(min=1, max=4)])
	PalletNumber = StringField('PalletNumber', validators=[validators.required(), validators.Length(min=19, max=19)])
	Purchase_order = StringField('PurchaseOrder', validators=[validators.required(), validators.Length(min=10, max=10)])
	Shipment_id = StringField('ShipmentId', validators=[validators.required(), validators.Length(min=10, max=10)])