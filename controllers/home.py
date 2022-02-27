from flask import Blueprint, render_template
from services.donations import Donations

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def getindex():
    donations = Donations()
    total = donations.get_total_value_in_usd()
    return render_template('home/index.html', total_donated=total)
