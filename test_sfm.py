import unittest
import copy
from sfm_converter import output_data
from empty import empty_user, empty_output


class TestSFMConvert(unittest.TestCase):
    def test_empty(self):
        in_datum = {}
        out_datum = copy.deepcopy(empty_output)
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_nones_1(self):
        in_datum = {
            "created_at": None,
            "entites": None,
            "id": None,
            "geo": {
                "country": None,
                "longitude": None,
            },
            "lang": None
        }
        out_datum = copy.deepcopy(empty_output)
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_nones_2(self):
        in_datum = {
            "geo": None,
            "metrics": None,
            "in_reply_to_user_id": None,
            "lang_iso_code": None,
            "text": None,
            "user": None,
            "source": None,
            "place": None,
        }
        out_datum = copy.deepcopy(empty_output)
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_nones_3(self):
        in_datum = {
            "entities": {
                "media": None,
                "urls": None
            },
            "user": {
                "name": None,
                "screen_name": None,
            }
        }
        out_datum = copy.deepcopy(empty_output)
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_nones_4(self):
        in_datum = {
            "entities": {
                "media": [None],
            },
            "place": {
                "country": None,
            }
        }
        out_datum = copy.deepcopy(empty_output)
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_nones_5(self):
        in_datum = {
            "entities": {
                "media": [],
                "user_mentions": [],
            },
            "place": {
                "country": None,
            },
            "metadata": {
                "iso_language_code": None,
                "result_type": None,
            },
            "is_quote_status": None,
            "user": None,
            "full_text": None
        }
        out_datum = copy.deepcopy(empty_output)
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_nones_6(self):
        in_datum = {
            "entities": {
                "media": [],
                "user_mentions": [],
            },
            "place": {
                "country": None,
            },
            "metadata": {
                "iso_language_code": None,
                "result_type": None,
            },
            "is_quote_status": None,
            "user": copy.deepcopy(empty_user),
            "full_text": None,
        }
        out_datum = copy.deepcopy(empty_output)
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_nones_7(self):
        in_datum = {
            "entities": {
                "media": [],
                "user_mentions": [],
            },
            "place": {
                "country": None,
            },
            "metadata": {
                "iso_language_code": None,
                "result_type": None,
            },
            "is_quote_status": None,
            "user": {
                "contributors_enabled": None,
                "created_at": None,
                "verified": None,
            },
            "full_text": None
        }
        out_datum = copy.deepcopy(empty_output)
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_misspelled(self):
        in_datum = {
            "entaties": {
                "media": [None],
            },
            "place": {
                "cuntry": None,
            }
        }
        out_datum = copy.deepcopy(empty_output)
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_sample_1(self):
        in_datum = {
            "created_at": "Fri Sep 04 13:53:36 +0000 2020",
            "id": 1301881098507628544,
            "id_str": "1301881098507628544",
            "full_text": "RT @stLogesh: Sir my name is Logeshwaran and I'm passed out BE student in anna university.Due to covid19 problem  many students in tamilnad\u2026",
            "truncated": False,
            "entities": {
                "hashtags": [],
                "symbols": [],
                "user_mentions": [{
                    "screen_name": "stLogesh",
                    "name": "L\u00f8g\u00e9sh",
                    "id": 737309631253479424,
                    "id_str": "737309631253479424",
                    "indices": [3, 12]
                }],
                "urls": []
            },
            "metadata": {
                "iso_language_code": "en",
                "result_type": "recent"
            },
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user": {
                "id": 1315833661,
                "id_str": "1315833661",
                "name": "\u0bb5\u0bbf\u0bb7\u0bcd\u0ba3\u0bc1 \u0baa\u0bbf\u0bb0\u0b95\u0bbe\u0bb7\u0bcd \u0bb0\u0bc6\u0b95\u0bc1\u0ba8\u0bbe\u0ba4\u0ba9\u0bcd",
                "screen_name": "reguvishnu",
                "location": "\u0baa\u0b9f\u0bcd\u0b9f\u0bc1\u0b95\u0bcd\u0b95\u0bcb\u0b9f\u0bcd\u0b9f\u0bc8,\u0ba4\u0bae\u0bbf\u0bb4\u0bcd \u0ba8\u0bbe\u0b9f\u0bc1",
                "description": "#\u0ba4\u0bbf\u0bae\u0bc1\u0b95"
            },
            "geo": None,
            "coordinates": None,
            "place": None,
            "contributors": None
        }

        out_user_mention = copy.deepcopy(empty_user)
        out_user_mention["screen_name"] = "stLogesh"
        out_user_mention["real_name"] = "L\u00f8g\u00e9sh"
        out_user_mention["id"] = "737309631253479424"

        out_datum = copy.deepcopy(empty_output)
        out_datum["created_at"] = "Fri Sep 04 13:53:36 +0000 2020"
        out_datum["id"] = "1301881098507628544"
        out_datum["text"] = "RT @stLogesh: Sir my name is Logeshwaran and I'm passed out BE student in anna university.Due to covid19 problem  many students in tamilnad\u2026"
        out_datum["entities"]["user_mentions"] = [out_user_mention.copy()]
        out_datum["lang_iso_code"] = "en"
        out_datum["result_type"] = "recent"
        out_datum["source"] = "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>"
        out_datum["user"]["id"] = "1315833661"
        out_datum["user"]["real_name"] = "\u0bb5\u0bbf\u0bb7\u0bcd\u0ba3\u0bc1 \u0baa\u0bbf\u0bb0\u0b95\u0bbe\u0bb7\u0bcd \u0bb0\u0bc6\u0b95\u0bc1\u0ba8\u0bbe\u0ba4\u0ba9\u0bcd"
        out_datum["user"]["screen_name"] = "reguvishnu"
        out_datum["user"]["description"] = "#\u0ba4\u0bbf\u0bae\u0bc1\u0b95"
        out_datum["user"]["location"] = "\u0baa\u0b9f\u0bcd\u0b9f\u0bc1\u0b95\u0bcd\u0b95\u0bcb\u0b9f\u0bcd\u0b9f\u0bc8,\u0ba4\u0bae\u0bbf\u0bb4\u0bcd \u0ba8\u0bbe\u0b9f\u0bc1"
        
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_sample_2(self):
        in_datum = {
            "full_text": "RT @stLogesh: Sir my name is Logeshwaran and I'm passed out BE student in anna university.Due to covid19 problem  many students in tamilnad\u2026",
            "entities": {
                "hashtags": [],
                "symbols": [],
                "urls": [],
                "media": [
                    {
                        "id_str": "This is a random id in string form",
                        "url": "https://www.somewhere.com",
                        "indices": [1000, 1000, 1000],
                    },
                    {},
                ],
            },
            "metadata": {
                "iso_language_code": "en",
                "result_type": "recent"
            },
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user": {
                "id": 1315833661,
                "id_str": "1315833661",
                "name": "\u0bb5\u0bbf\u0bb7\u0bcd\u0ba3\u0bc1 \u0baa\u0bbf\u0bb0\u0b95\u0bbe\u0bb7\u0bcd \u0bb0\u0bc6\u0b95\u0bc1\u0ba8\u0bbe\u0ba4\u0ba9\u0bcd",
                "screen_name": "reguvishnu",
                "location": "\u0baa\u0b9f\u0bcd\u0b9f\u0bc1\u0b95\u0bcd\u0b95\u0bcb\u0b9f\u0bcd\u0b9f\u0bc8,\u0ba4\u0bae\u0bbf\u0bb4\u0bcd \u0ba8\u0bbe\u0b9f\u0bc1",
                "description": "#\u0ba4\u0bbf\u0bae\u0bc1\u0b95"
            },
            "geo": {
                "coordinates": [90.0, -100.0],
                "type": "the type",
            },
            "place": {
                "country": "Australia",
            },
            "contributors": None
        }

        out_user = copy.deepcopy(empty_user)
        out_user["id"] = "1315833661"
        out_user["real_name"] = "\u0bb5\u0bbf\u0bb7\u0bcd\u0ba3\u0bc1 \u0baa\u0bbf\u0bb0\u0b95\u0bbe\u0bb7\u0bcd \u0bb0\u0bc6\u0b95\u0bc1\u0ba8\u0bbe\u0ba4\u0ba9\u0bcd"
        out_user["screen_name"] = "reguvishnu"
        out_user["description"] = "#\u0ba4\u0bbf\u0bae\u0bc1\u0b95"
        out_user["location"] = "\u0baa\u0b9f\u0bcd\u0b9f\u0bc1\u0b95\u0bcd\u0b95\u0bcb\u0b9f\u0bcd\u0b9f\u0bc8,\u0ba4\u0bae\u0bbf\u0bb4\u0bcd \u0ba8\u0bbe\u0b9f\u0bc1"

        out_datum = copy.deepcopy(empty_output)
        out_datum["text"] = "RT @stLogesh: Sir my name is Logeshwaran and I'm passed out BE student in anna university.Due to covid19 problem  many students in tamilnad\u2026"
        out_datum["entities"]["media"] = [
            {
                "id": "This is a random id in string form",
                "url": "https://www.somewhere.com",
            },
            {
                "id": None,
                "url": None,
            }
        ]
        out_datum["lang_iso_code"] = "en"
        out_datum["source"] = "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>"
        out_datum["user"] = out_user.copy()
        out_datum["result_type"] = "recent"
        out_datum["geo"] = {
            'country': "Australia",
            'latitude': 90.0,
            'longitude': -100.0,
            "type": "the type",
        }
        out_datum['metrics'] = {
            'favorite_count': None,
            'retweet_count': None
        }
        myOut = output_data(in_datum).__dict__
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_sample_3(self):
        in_datum = {
            "full_text": "RT @stLogesh: Sir my name is Logeshwaran and I'm passed out BE student in anna university.Due to covid19 problem  many students in tamilnad\u2026",
            "lang": "English",
            "favorite_count": 10000,
            "retweet_count": -1,
            "metadata": {
                "iso_language_code": "en",
                "result_type": "recent"
            },
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
        }
        out_datum = copy.deepcopy(empty_output)
        out_datum["text"] = "RT @stLogesh: Sir my name is Logeshwaran and I'm passed out BE student in anna university.Due to covid19 problem  many students in tamilnad\u2026"
        out_datum["lang"] = "English"
        out_datum["lang_iso_code"] = "en"
        out_datum["source"] = "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>"
        out_datum["result_type"] = "recent"
        out_datum["metrics"] = {
            "favorite_count": 10000,
            "retweet_count": -1
        }
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_sample_4(self):
        in_datum = {
            "full_text": "RT @stLogesh: Sir my name is Logeshwaran and I'm passed out BE student in anna university.Due to covid19 problem  many students in tamilnad\u2026",
            "display_text_range": [10, 20],
            "lang": "English",
            "favorite_count": 10000,
            "retweet_count": -1,
            "entities": {
                "user_mentions": [
                    {
                        "contributors_enabled": True,
                        "geo_enabled": False,
                        "id_str": "some random string",
                        "name": "the name",
                    }
                ]
            },
            "geo": {
                "type": "some type of geo",
            },
            "metadata": {
                "iso_language_code": "en",
                "result_type": "recent"
            },
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "user": {
                "favorites_count": 100,
                "listed_count": -100,
                "screen_name": "my name",
                "is_translator": False,
            },
        }

        out_user_mention = copy.deepcopy(empty_user)
        out_user_mention["contributors_enabled"] = True
        out_user_mention["geo_enabled"] = False
        out_user_mention["id"] = "some random string"
        out_user_mention["real_name"] = "the name"

        out_user = copy.deepcopy(empty_user)
        out_user["metrics"]["favorites_count"] = 100
        out_user["metrics"]["listed_count"] = -100
        out_user["screen_name"] = "my name"
        out_user["is_translator"] = False

        out_datum = copy.deepcopy(empty_output)
        out_datum["text"] = "RT @stLogesh: Sir my name is Logeshwaran and I'm passed out BE student in anna university.Due to covid19 problem  many students in tamilnad\u2026"
        out_datum["lang"] = "English"
        out_datum["lang_iso_code"] = "en"
        out_datum["result_type"] = "recent"
        out_datum["source"] = "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>"
        out_datum["entities"]["user_mentions"] = [out_user_mention]
        out_datum["geo"]["type"] = "some type of geo"
        out_datum["metrics"] = {
            "favorite_count": 10000,
            "retweet_count": -1
        }
        out_datum["user"] = out_user
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_sample_5(self):
        in_datum = {
            "in_reply_to_screen_name": "my screen name",
            "in_reply_to_user_id_str": "user id string",
            "in_reply_to_status_id_str": "status id string",
            "is_quote_status": False,
        }
        out_datum = copy.deepcopy(empty_output)
        out_datum["in_reply_to_screen_name"] = "my screen name"
        out_datum["in_reply_to_user_id"] = "user id string"
        out_datum["in_reply_to_status_id"] = "status id string"
        out_datum["is_quote_status"] = False
        self.assertEqual(out_datum, output_data(in_datum).__dict__)

    def test_sample_6(self):
        in_datum = {
            "user": {
                "contributors_enabled": True,
                "created_at": "created now!",
                "default_profile": False,
                "default_profile_image": True,
                "description": "my description",
                "follow_request_sent": False,
                "geo_enabled": True,
                "favorites_count": 600,
                "friends_count": 200,
                "followers_count": 1000,
                "statuses_count": -1000,
                "listed_count": 900,
                "id_str": "my id",
                "has_extended_profile": True,
                "is_translation_enabled": False,
                "is_translator": True,
                "lang": "English",
                "location": "my location",
                "name": "my name",
                "notifications": False,
                "screen_name": "my screen name",
                "time_zone": "my time zone",
                "translator_type": "translator_type",
                "url": "https://myurl.com",
                "utc_offset": "my utc offset",
                "verified": True,
                "withheld_in_countries": ["Australia", "New Zealand"],
            }
        }
        out_user = copy.deepcopy(empty_user)
        out_user["contributors_enabled"] = True
        out_user["created_at"] = "created now!"
        out_user["default_profile"] = False
        out_user["default_profile_image"] = True
        out_user["description"] = "my description"
        out_user["follow_request_sent"] = False
        out_user["geo_enabled"] = True
        out_user["metrics"]["favorites_count"] = 600
        out_user["metrics"]["friends_count"] = 200
        out_user["metrics"]["followers_count"] = 1000
        out_user["metrics"]["statuses_count"] = -1000
        out_user["metrics"]["listed_count"] = 900
        out_user["id"] = "my id"
        out_user["has_extended_profile"] = True
        out_user["is_translation_enabled"] = False
        out_user["is_translator"] = True
        out_user["lang"] = "English"
        out_user["location"] = "my location"
        out_user["real_name"] = "my name"
        out_user["notifications"] = False
        out_user["screen_name"] = "my screen name"
        out_user["time_zone"] = "my time zone"
        out_user["translator_type"] = "translator_type"
        out_user["url"] = "https://myurl.com"
        out_user["utc_offset"] = "my utc offset"
        out_user["verified"] = True
        out_user["withheld_in_countries"] = ["Australia", "New Zealand"]

        out_datum = copy.deepcopy(empty_output)
        out_datum["user"] = out_user
        self.maxDiff = None
        self.assertEqual(out_datum, output_data(in_datum).__dict__)


if __name__ == "__main__":
    #sys.stdout.reconfigure(encoding="utf-8")
    unittest.main()
