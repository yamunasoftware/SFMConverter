empty_collection = {
    "id": None,
    "description": None,
    "count": None,
    "tweet_ids": [],
    "collection_terms": [],
    "wikipedia": None,
    "create_time": None,
    "metrics": {
        "retweet_count": None,
        "like_count": None,
        "reply_count": None,
        "quote_count": None
    }
}

empty_user = {
    "contributors_enabled": None,
    "created_at": None,
    "default_profile": None,
    "default_profile_image": None,
    "description": None,
    "follow_request_sent": None,
    "geo_enabled": None,
    "id": None,
    "metrics": {
        "favorites_count": None,
        "followers_count": None,
        "friends_count": None,
        "statuses_count": None,
        "listed_count": None,
    },
    "has_extended_profile": None,
    "is_translation_enabled": None,
    "is_translator": None,
    "lang": None,
    "location": None,
    "real_name": None,
    "notifications": None,
    "screen_name": None,
    "time_zone": None,
    "translator_type": None,
    "url": None,
    "utc_offset": None,
    "verified": None,
    "withheld_in_countries": []
}

empty_output = {
    "contributors": None,
    "created_at": None,
    "entities": {
        "hashtags": [],
        "media": [],
        "urls": [],
        "user_mentions": [],
    },
    "geo": {
        "country": None,
        "type": None,
        "latitude": None,
        "longitude": None
    },
    "id": None,
    "in_reply_to_screen_name": None,
    "in_reply_to_user_id": None,
    "in_reply_to_status_id": None,
    "is_quote_status": None,
    "lang": None,
    "lang_iso_code": None,
    "metrics": {
        "favorite_count": None,
        "retweet_count": None
    },
    "source": None,
    "result_type": None,
    "text": None,
    "user": empty_user.copy()
}
