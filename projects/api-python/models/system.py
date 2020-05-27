import json
import flask
from flask_restful import Resource
from flask_restful import reqparse
from infrastracture.database import Database

class System(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('period_id', type=int, help='')
            args = parser.parse_args()
            period_id = args['period_id']

            database = Database.connect()
            cursor = database.cursor()

            sql = """
                SELECT 
                    rj_system_status_tb.id,
                    rj_system_tb.system_name, 
                    COUNT(rj_system_defects_tb.id) as 'defect_count', 
                    rj_system_status_tb.sup
                FROM rj_system_defects_tb
                INNER JOIN rj_system_status_tb ON rj_system_defects_tb.system_status_id = rj_system_status_tb.id
                INNER JOIN rj_system_tb ON rj_system_tb.id = rj_system_status_tb.system_id
                WHERE rj_system_status_tb.period_id = %s
                GROUP BY rj_system_tb.id;
            """
            argument = (period_id, )
            cursor.execute(sql,argument)
            result = cursor.fetchall()
            data = []
            key = ('id', 'system_name', 'defect_count', 'percentage')
            for system in result:
                item = (system[0], str(system[1]), system[2], system[3])
                data.append(dict(zip(key, item)))
            return flask.jsonify(data)
        except Exception as exception:
            return {'error': str(exception)}