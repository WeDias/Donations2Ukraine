from flask import Blueprint, render_template
from services.donations import Donations


donations = Donations()
home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def get_index():
    return render_template('home/index.html')


@home.route('/api/v1/donated', methods=['GET'])
def get_donated():
    return {'donated_usd': donations.get_total_value_in_usd()}
