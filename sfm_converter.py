# Converts the JSON data in an SFM file to the schema and prints the results. Redirect output to store in a file.

import ujson
import sys
from empty import empty_user

class output_data():

    ''' 
        Handles the use of a user JSON object within the tweet JSON
        Creates a dictionary of the proper user object and returns it
        general structure to set fields is the following:
        <field>: user[<field>] if <field> in user else None
        This uses a ternary operation to avoid a KeyError exception if a field is not present 
    '''
    def convert_user(self, user):
        return {
            "contributors_enabled": user["contributors_enabled"] if "contributors_enabled" in user else None,
            "created_at": user["created_at"] if "created_at" in user else None,
            "default_profile": user["default_profile"] if "default_profile" in user else None,
            "default_profile_image": user["default_profile_image"] if "default_profile" in user else None,
            "description": user["description"] if "description" in user else None,
            "follow_request_sent": user["follow_request_sent"] if "follow_request_sent" in user else None,
            "geo_enabled": user["geo_enabled"] if "geo_enabled"  in user else None,
            "id": user["id_str"] if "id_str" in user else None,
            # metrics follows a similar structure to everything else in a nested dictionary
            "metrics": {
                "favorites_count": user["favorites_count"] if "favorites_count" in user else None,
                "followers_count": user["followers_count"] if "followers_count" in user else None,
                "friends_count": user["friends_count"] if "friends_count" in user else None,
                "statuses_count": user["statuses_count"] if "statuses_count" in user else None,
                "listed_count": user["listed_count"] if "listed_count" in user else None,
            },
            "has_extended_profile": user["has_extended_profile"] if "has_extended_profile" in user else None,
            "is_translation_enabled": user["is_translation_enabled"] if "is_translation_enabled" in user else None,
            "is_translator": user["is_translator"] if "is_translator" in user else None,
            "lang": user["lang"] if "lang" in user else None,
            "location": user["location"] if "location" in user else None,
            "notifications": user["notifications"] if "notifications" in user else None,
            "real_name": user["name"] if "name" in user else None,
            "screen_name": user["screen_name"] if "screen_name" in user else None,
            "time_zone": user["time_zone"] if "time_zone" in user else None,
            "translator_type": user["translator_type"] if "translator_type" in user else None,
            "url": user["url"] if "url" in user else None,
            "utc_offset": user["utc_offset"] if "utc_offset" in user else None,
            "verified": user["verified"] if "verified" in user else None,
            "withheld_in_countries": user["withheld_in_countries"] if "withheld_in_countries" in user and bool(user["withheld_in_countries"]) else [],
        }

    '''
        Initializer for the output_data python object
        Takes in the input dictonary and fills in the appropriate output fields in a python object
        The general format is:
        self.<field> = in_datum[<field>] if "field" in in_datum else None
        This uses a ternary operation to avoid a KeyError exception if a field is not present 
    '''
    def __init__(self, in_datum):
        self.contributors = in_datum["contributors"] if "contributors" in in_datum else None
        self.created_at = in_datum["created_at"] if "created_at" in in_datum else None
        
        '''
            Entities is the most complex structure within the JSON object.
            It contains media which is a list of media which we parse individually in a for loop using list comprehension
            We then need to check if each field exists and is the correct data type with ternary statements
        '''
        self.entities = {
            "media": [{
                "url": medium["url"] if "url" in medium else None,
                "id": medium["id_str"] if "id_str" in medium else None,
            } for medium in in_datum["entities"]["media"] if type(medium) is dict] if "media" in in_datum["entities"] and type(in_datum["entities"]["media"]) is list else [],
            "hashtags": in_datum["entities"]["hashtags"] if "hashtags" in in_datum["entities"] and bool(in_datum["entities"]["hashtags"]) else [],
            "user_mentions": [self.convert_user(user_mention) for user_mention in in_datum["entities"]["user_mentions"]] if "user_mentions" in in_datum["entities"] else [],
            "urls": in_datum["entities"]["urls"] if "urls" in in_datum["entities"] and bool(in_datum["entities"]["urls"]) else []
        } if "entities" in in_datum and type(in_datum["entities"]) is dict else {"hashtags": [], "media": [], "user_mentions": [], "urls": []}    
        
        '''
            Geo is a nested dictionary that is structured similarly to the individual fields, 
            we just need to check that each layer actually exists within the input_data dictionary
        '''
        self.geo = {
            "country": in_datum["place"]["country"] if "place" in in_datum and type(in_datum["place"]) is dict and "country" in in_datum["place"] else None,
            "latitude": in_datum["geo"]["coordinates"][0] if "geo" in in_datum and type(in_datum["geo"]) is dict and "coordinates" in in_datum["geo"] else None,
            "longitude": in_datum["geo"]["coordinates"][1] if "geo" in in_datum and type(in_datum["geo"]) is dict and "coordinates" in in_datum["geo"] else None,
            "type": in_datum["geo"]["type"] if "geo" in in_datum and type(in_datum["geo"]) is dict and "type" in in_datum["geo"] else None,
        }
        
        self.id = in_datum["id_str"] if "id_str" in in_datum else None
        self.in_reply_to_screen_name = in_datum["in_reply_to_screen_name"] if "in_reply_to_screen_name" in in_datum else None
        self.in_reply_to_user_id = in_datum["in_reply_to_user_id_str"] if "in_reply_to_user_id_str" in in_datum else None
        self.in_reply_to_status_id = in_datum["in_reply_to_status_id_str"] if "in_reply_to_status_id_str" in in_datum else None
        self.is_quote_status = in_datum["is_quote_status"] if "is_quote_status" in in_datum else None
        self.lang = in_datum["lang"] if "lang" in in_datum else None
        self.lang_iso_code = in_datum["metadata"]["iso_language_code"] if "metadata" in in_datum and type(in_datum["metadata"]) is dict and "iso_language_code" in in_datum["metadata"] else None
        self.result_type = in_datum["metadata"]["result_type"] if "metadata" in in_datum and type(in_datum["metadata"]) is dict and "result_type" in in_datum["metadata"] else None
        
        '''
            Metrics is a nested dictionary that is structured similarly to the individual fields, 
            However we only need to check surface level of in_datum for the field existing
        '''
        self.metrics = {
            "favorite_count": in_datum["favorite_count"] if "favorite_count" in in_datum else None,
            "retweet_count": in_datum["retweet_count"] if "retweet_count" in in_datum else None
        }
        
        self.source = in_datum["source"] if "source" in in_datum else None
        self.text = in_datum["full_text"] if "full_text" in in_datum else None
        
        # Create a user object (if it exists) with the convert_user() helper function
        self.user = self.convert_user(in_datum["user"]) if "user" in in_datum and type(in_datum["user"]) is dict else empty_user
    
'''
    Main function for the converter
    Iterates through the file given line by line 
    Creates a output_data json object
    Prints the dictionary representation to the terminal (to be rerouted to an output file)
'''
if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ValueError("Supply two command-line argument specifying the JSON filepath and the JSON output")
    with open(sys.argv[2], 'w', encoding="utf-8") as outputFile:

        with open(sys.argv[1]) as f:
            for line in f:
                #print(ujson.dumps(output_data(ujson.loads(line)).__dict__, ensure_ascii=False, escape_forward_slashes=False))     
                outputFile.write(ujson.dumps(output_data(ujson.loads(line)).__dict__, ensure_ascii=False, escape_forward_slashes=False) + '\n')