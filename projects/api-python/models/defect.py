import json
import flask
from flask_restful import Resource
from flask_restful import reqparse
from infrastracture.database import Database

class Defect(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('system_status_id', type=int, help='')
            args = parser.parse_args()
            system_status_id = args['system_status_id']

            database = Database.connect()
            cursor = database.cursor()

            sql = """
                SELECT 
                    `id`, 
                    `defect_description`, 
                    `date_reported`, 
                    `date_fixed_released` 
                FROM `rj_system_defects_tb`
                WHERE `system_status_id` = %s
            """
            arg = (system_status_id, )
            cursor.execute(sql,arg)
            result = cursor.fetchall()
            data = []
            key = ('id', 'defect_description', 'date_reported', 'date_fixed_released')
            for system in result:
                item = (system[0], str(system[1]), str(system[2]), str(system[3]))
                data.append(dict(zip(key, item)))
            return flask.jsonify(data)

        except Exception as exception:
            return {'error': str(exception)}

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('params', type=str, help='')
            args = parser.parse_args()
            params = json.loads(args['params'])

            system_status_id = params['system_status_id'] if 'system_status_id' in params else None
            defect_description = params['defect_description'] if 'defect_description' in params else None
            date_reported = params['date_reported'] if 'date_reported' in params else None
            date_fixed_released = params['date_fixed_released'] if 'date_fixed_released' in params else None

            if (
                system_status_id == None or 
                defect_description == None or 
                date_reported == None or 
                date_fixed_released == None
            ):
                return {
                    'success' : False,
                    'message' : 'Incomplete parameters'
                }
                
            database = Database.connect()
            cursor = database.cursor()
            sql = """
                INSERT INTO `rj_system_defects_tb` 
                (`system_status_id`, `defect_description`, `date_reported`, `date_fixed_released`)
                VALUES (%s, %s, %s, %s)
            """
            arg = (system_status_id, defect_description, date_reported, date_fixed_released)
            cursor.execute(sql, arg)

            if cursor.lastrowid:
                database.commit()
                database.close()
                return {
                    'success' : True,
                    'last_insert_id' : cursor.lastrowid,
                }

            return {
                'success' : False,
                'message' : 'Defect record not inserted'
            }
        
        except Exception as exception:
            return {'error': str(exception)}