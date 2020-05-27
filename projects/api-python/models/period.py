import json
import flask
from flask_restful import Resource
from flask_restful import reqparse
from infrastracture.database import Database

class Period(Resource):
    def get(self):
        try:
            database = Database.connect()
            cursor = database.cursor()

            sql = """
                SELECT 
                    id, 
                    period_name, 
                    period_start_date, 
                    period_end_date
                FROM rj_period_tb 
                ORDER BY id DESC
                LIMIT 1
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            data = []
            key = ('id', 'period_name', 'period_start_date', 'period_end_date')
            for system in result:
                item = (system[0], str(system[1]), str(system[2]), str(system[3]))
                data.append(dict(zip(key, item)))
            return flask.jsonify(data)

        except Exception as exception:
            return {'error': str(exception)}