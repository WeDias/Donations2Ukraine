from cachetools import TTLCache
from flask import Blueprint, render_template
from services.donations_all import DonationsAll


donations = DonationsAll()
cache = TTLCache(maxsize=1, ttl=60)
home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def get_index():
    return render_template('home/index.html')


@home.route('/api/v1/donated', methods=['GET'])
def get_donated():
    if 'donations_all' not in cache:
        cache['donations_all'] = donations.get_value_in_dollars()
    return {'donated_usd': cache['donations_all']}
