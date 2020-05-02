import json
import flask
from flask_restful import Resource
from flask_restful import reqparse
from infrastracture.storage import Storage

class System(Resource):
    def get(self):
        try:
            system_collection = Storage.get_collection('systems')
            results = system_collection.find({})
            data = []
            key = ('id', 'name', 'percentage')
            for system in results:
                item = (str(system['_id']), system['name'], system['percentage'])
                data.append(dict(zip(key, item)))
            return flask.jsonify(data)

        except Exception as exception:
            return {'error': str(exception)}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('params', type=str, help='')
        args = parser.parse_args()
        params = json.loads(args['params'])

        system_name = params['name'] if 'name' in params else None
        system_percentage = params['percentage'] if 'percentage' in params else None

        if (system_name == None or system_percentage == None):
            return {
                'success' : False,
                'message' : 'Incomplete parameters'
            }

        try:
            data = {'name': system_name, 'percentage': system_percentage}
            system = Storage.get_collection('systems')
            document_id = system.insert_one(data)

            if document_id:
                return {
                    'success': True,
                    'message': 'A new system has been added'
                }

            return {
                'success': False,
                'message': 'The system has not been added'
            }
        
        except Exception as exception:
            return {'error': str(exception)}
    