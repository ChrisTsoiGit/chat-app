 # serialize and convert Bson to Json:

def userEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),  # ObjectId -> str
        "username": db_item["user_name"],
        "email": db_item["user_email"],
        "pw": db_item["user_pw"],
        "avatar": db_item["user_avatar_url"]
    }

def listOfUserEntity(db_item_list) -> list:  # list of dictionaries
    list_user_entity = []
    for item in db_item_list:
        list_user_entity.append(userEntity(item))
    return  list_user_entity
