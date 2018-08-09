from flask import Flask, render_templates, request, redirect, url_for
from wtforms import Form, validators, StringField
from wtforms.validators import DataRequired
import itertools, datetime
import xml.etree.ElementTree as ET

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
		return redirect(url_for('index'))

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

		dt=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

		asn = ET.Element("asn")
		asn.set("xsi:noNamespaceSchemaLocation", "S:/SchemaRepository/XMLSchemas/External/asn.xsd")
		asn.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")

		sender_location = ET.SubElement(asn, "sender_location") 
		sender_location.text=" "

		receiver_location = ET.SubElement(asn, "receiver_location")
		receiver_location.text=" "

		shipment_id = ET.SubElement(asn, "shipment_id")
		shipment_id.text = Shipment_id

		shipment_date = ET.SubElement(asn, "shipment_date")
		shipment_date.text = dt

		vehicle_id = ET.SubElement(asn, "vehicle_id")
		vehicle_id.text=" "

		purchase_order = ET.SubElement(asn, "purchase_order")
		purchase_order.text = Purchase_order

		number_of_pallets = ET.SubElement(asn, "number_of_pallets")
		number_of_pallets.text = quantity


		count=0
		for n in Pallets:
			pallet = ET.SubElement(asn, "pallet")
			sscc = ET.SubElement(pallet, "sscc")
			sscc.text = n
			number_of_cases = ET.SubElement(pallet, "number_of_cases")
			number_of_cases.text = str(len(cases_a[y]))
			for i in cases_a[y]:
				case = ET.SubElement(pallet, "case")
				label = ET.SubElement(case, "label")
				label.text = i
			count+=1



if __name__ == "__main__"
	app.run(debug=True)
