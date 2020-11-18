from models.Profile import Profile                                     # Importing the Profile Model
from models.Account import Account                                     # Importing the Account Model
from schemas.ProfileSchema import profile_schema, profiles_schema      # Importing the Profile Schema
from main import db                                                    # This is the db instance created by SQLAlchemy
from main import bcrypt                                                # Import the hasing package from main
from services.auth_service import verify_account 
from sqlalchemy.orm import joinedload                                  # 
from flask_jwt_extended import jwt_required, get_jwt_identity          # Packages for authorization via JWTs
from flask import Blueprint, request, jsonify, abort                   # Import flask and various sub packages

profiles = Blueprint("profiles", __name__, url_prefix="/profile")      # Creating the profile blueprint 

@profiles.route("/", methods=["GET"])                                  # Route for the profile index
def profile_index():                                                   # This function will run when the route is matched
    profiles = Profile.query.options(joinedload("account")).all()      # Retrieving all profiles from the db
    return jsonify(profiles_schema.dump(profiles))                     # Returning all the profiles in json

@profiles.route("/", methods=["POST"])                                 # Route for the profile create
@jwt_required
@verify_account
def profile_create(account):                                           # This function will run when the route is matched
    profile_fields = profile_schema.load(request.json)

    profile = Profile.query.filter_by(username=profile_fields["username"]).first() # Query the account table with the email and return the first account

    if account.profile != None:
        return abort(400, description="User already has profile")             # Return the error "Email already in use"

    
    if profile:                                                              # If a account is returned 
        return abort(400, description="username already in use")             # Return the error "Email already in use"

    new_profile = Profile()
    new_profile.username = profile_fields["username"]
    new_profile.firstname = profile_fields["firstname"]
    new_profile.lastname = profile_fields["lastname"]
    new_profile.account_id = account.id
    account.profile.append(new_profile)
    db.session.commit() 
      
    return jsonify(profile_schema.dump(new_profile))