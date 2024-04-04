# Summarizes an SFM collection by producing and printing a single JSON object summarizing the SFM tweets
# in the input file, according to the collection level schema

import copy
import ujson
import sys
from empty import empty_collection


if len(sys.argv) != 3:
    raise ValueError("Supply two command-line argument specifying the JSON filepath and JSON output file a")

collection_obj = copy.deepcopy(empty_collection)

count = 0
tweet_ids = []
collection_terms = set()
retweet_count = 0
like_count = 0

with open(sys.argv[2], 'w', encoding='utf-8') as outputFile:
    with open(sys.argv[1]) as f:
        for line in f:
            datum = ujson.loads(line)
            count += 1
            if "id_str" in datum and datum["id_str"] is not None:
                tweet_ids.append(datum["id_str"])
            if "entities" in datum and datum["entities"] is not None and "hashtags" in datum["entities"] and datum["entities"]["hashtags"] is not None:
                collection_terms |= set([hashtag["text"] for hashtag in datum["entities"]["hashtags"] if hashtag is not None and "text" in hashtag])
            retweet_count += datum["retweet_count"] if "retweet_count" in datum and datum["retweet_count"] is not None else 0
            like_count += datum["favorite_count"] if "favorite_count" in datum and datum["favorite_count"] is not None else 0

    collection_obj["count"] = count
    collection_obj["tweet_ids"] = tweet_ids
    collection_obj["collection_terms"] = list(collection_terms)
    collection_obj["metrics"]["retweet_count"] = retweet_count
    collection_obj["metrics"]["like_count"] = like_count

    outputFile.write((ujson.dumps(collection_obj, ensure_ascii=False, escape_forward_slashes=False)) + '\n')


