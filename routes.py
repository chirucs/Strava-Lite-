from api import *

def register_routes(app):
    # Route for RegisterUser API
    app.add_url_rule('/user','register_user',regisrter_user,methods=['POST'])

    # Route for GetUser API
    app.add_url_rule('/user/<user_id>','get_user',get_user,methods=['GET'])
    
    # Route for RemoveUser API
    app.add_url_rule('/user/<user_id>', 'remove_user', remove_user, methods=['DELETE'])

    # Route for ListUsers API
    app.add_url_rule('/users','list_users',list_users,methods=['GET'])

    # Route for Workout API
    app.add_url_rule('/workouts/<user_id>','add_workout',add_workout,methods=['PUT'])

    # Route for Listworkouts API
    app.add_url_rule('/workouts/<user_id>','list_workouts',list_workouts,methods=['GET'])



#--------------------------------------------- extra credit ---------------------------------------

    app.add_url_rule('/followers/<user_id>','follow_friend',follow_friend,methods=['PUT'])