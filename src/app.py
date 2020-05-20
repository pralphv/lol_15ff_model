from flask import Flask, jsonify, make_response, request
import pandas as pd

try:
    from .models import load_15_model, load_20_model
    from .standard_score import load_standard_score_15, load_standard_score_20
except ImportError:
    from models import load_15_model, load_20_model
    from standard_score import load_standard_score_15, load_standard_score_20

app = Flask(__name__)


def create_resp(status, msg):
    return jsonify({'status': status, 'msg': msg})


@app.route('/')
def landing_page():
    return make_response(create_resp('ok', 'online'), 200)


features = [
    'kda_diff',
    'cs_diff',
    'turrets_diff',
    'inhibitors_diff',
    'level_diff',
    'monsters_diff'
]


def process_data(parameters, minute: int):
    team_100 = parameters['100']
    team_200 = parameters['200']

    team_100['kda'] = team_100['kills'] + team_100['assists']
    team_100['monsters'] = team_100['dragon'] + team_100['herald']
    team_200['kda'] = team_200['kills'] + team_200['assists']
    team_200['monsters'] = team_200['dragon'] + team_200['herald']
    team_200['kda'] = team_200['kills'] + team_200['assists']

    df_100 = pd.DataFrame([team_100])
    df_200 = pd.DataFrame([team_200])
    df_diff = df_100 - df_200

    df_diff.columns = map(lambda col_name: f'{col_name}_diff', df_diff.columns.values)
    df_diff = df_diff[features]

    if minute == 15:
        stats = load_standard_score_15()
    elif minute == 20:
        stats = load_standard_score_20()

    for col_name, stat in stats.items():
        df_diff[col_name] = (df_diff[col_name] - stat['mean']) / stat['std']
    return df_diff


@app.route('/api/15', methods=['POST'])
def predict_15_min():
    parameters = request.json
    df_diff = process_data(parameters, 15)
    clf = load_15_model()
    winning_team = clf.predict(df_diff)[0]
    return make_response(create_resp('ok', {'winningTeam': winning_team}), 200)


@app.route('/api/20', methods=['POST'])
def predict_20_min():
    parameters = request.json
    df_diff = process_data(parameters, 20)
    clf = load_20_model()
    winning_team = clf.predict(df_diff)[0]
    return make_response(create_resp('ok', {'winningTeam': winning_team}), 200)


@app.route('/api/required-format')
def return_required_format():
    required_format = {
        "100": {
            "turrets": "int",
            "herald": "int",
            "baron": "int",
            "dragon": "int",
            "inhib": "int",
            "level": "int",
            "kills": "int",
            "deaths": "int",
            "assists": "int",
            "cs": "int"
        },
        "200": {
            "turrets": "int",
            "herald": "int",
            "baron": "int",
            "dragon": "int",
            "inhib": "int",
            "level": "int",
            "kills": "int",
            "deaths": "int",
            "assists": "int",
            "cs": "int"
        }
    }
    return make_response(create_resp('ok', required_format), 200)


if __name__ == '__main__':
    app.run(debug=True)
