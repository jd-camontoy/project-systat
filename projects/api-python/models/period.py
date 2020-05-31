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
            result = cursor.fetchone()
            if result is None:
                return {
                    'success' : False,
                    'error' : 'No record on periods'
                }

            data = {}
            data['id'], data['period_name'], data['period_start_date'], data['period_end_date'] = result
            return flask.jsonify(data)

        except Exception as exception:
            return {'error': str(exception)}