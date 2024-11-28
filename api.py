import uuid # generate unique user ID's
from flask import request,jsonify

# In memeory data storage for users
data_storage={"users":{}}

# Define the RegisterUser API
def regisrter_user():
    try:
        # Extract data from the request body
        body=request.get_json()
        name=body['name']
        age=body['age']

        # generate a unique ID for the user
        user_id=str(uuid.uuid4())

        # add user to the data storage
        data_storage['users'][user_id]={
            "id": user_id,
            "name":name,
            "age":age
        }

        # Return the created user object
        return jsonify(data_storage['users'][user_id]),200
    except KeyError:
        # If required fields are missing, return a 400 error
        return "Missing required fields", 400

#GetUser API
def get_user(user_id):
    # check if the user exists in the data store
    user=data_storage["users"].get(user_id)
    if user:
        #return the user data if found
#        print("User found:", user)  # Debug log
        return jsonify(user),200
    # return 404 if the user is not found
  #  print("User not found!")  # Debug log
    return "User not found",404

# RemoveUser API
def remove_user(user_id):
    # Check if the user exists in the data store
    if user_id in data_storage['users']:
        # Remove the user
        del data_storage['users'][user_id]
        return "User removed successfully", 200
    # Return 404 if the user is not found
    return "User not found", 404

# ListUsers API
def list_users():
    # Retrive all users from the data storage
    users=list(data_storage['users'].values()) # convert disctionary to a list of objects
    return jsonify({"users":users}),200

# AddWorkout API
def add_workout(user_id):
    try:
        # extract data from the request body
        body=request.get_json()
        date=body['date']
        time=body['time']
        distance=body['distance']

        # chech if the user exists
        user=data_storage['users'].get(user_id)
        if not user:
            return "User not found", 404
        # add workout to the user workout list profile
        workout={
            "date":date,
            "time":time,
            "distance":distance
        }
        user.setdefault('workouts',[]).append(workout)

        # Return the workout details
        return jsonify(workout),200
    except KeyError:
        # if the fields are missing, return a 400 error
        return "Missing required fields",400
    
# Listworkouts API
def list_workouts(user_id):
    # check if the user exists
    user=data_storage['users'].get(user_id)
    if not user:
        return "User not found",404
    workouts=user.get('workouts',[])
    return jsonify({"workouts":workouts}),200

#--------------------------------------------- extra credit ---------------------------------------

# FollowFriend API
def follow_friend(user_id):
    try:
        # extract the data from the request body
        body=request.get_json()
        follow_id=body['follow_id']

        # checking if both users exist
        if user_id not in data_storage['users'] or follow_friend not in data_storage['users']:
            return "Oops U cant follow your user/friend because user not found" ,404
        
        # add follow_id to the suers following list
        user_follows=data_storage.setdefault('follows',{})
        user_follows.setdefault(user_id,set()).add(follow_id)

        # return the updated following list
        return jsonify({"following": list(user_follows[user_id])}),200
    except KeyError:
        return "Missing the required fileds" ,400