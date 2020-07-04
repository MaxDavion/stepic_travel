import random
from flask import Flask, render_template
import data


app = Flask(__name__)


@app.route('/')
def main():
    _tours_list = list(data.tours.items())
    random.shuffle(_tours_list)
    return render_template(
        "index.html",
        title=data.title,
        departures=data.departures,
        tours=dict(_tours_list[:6]),
        description=data.description,
        subtitle=data.subtitle
    )


@app.route('/departures/<departure>/')
def departures(departure):
    return render_template(
        "departure.html",
        departures=data.departures,
        departure=data.departures[departure],
        title=data.title,
        tours={k:v for k,v in data.tours.items() if v['departure'] == departure}
    )


@app.route('/tours/<int:id>/')
def tours(id):
    return render_template(
        "tour.html",
        departures=data.departures,
        title=data.title,
        tour_id=id,
        tour=data.tours.get(id)
    )


@app.template_filter('as_currency')
def as_currency(price):
    """ Вернуть переданную цену с разделением пробелом между тысячами
    Пример:
        '52000' -> '52 000'
    """
    return '{:,.0f}'.format(price).replace(",", " ")


@app.template_filter('as_stars')
def as_stars(count_stars):
    """ Вернуть строку, содержащую переданное кол-во ★
    Пример:
        '5' -> '★★★★★'
    """
    return int(count_stars) * '★'


if __name__ == '__main__':
    app.run()
