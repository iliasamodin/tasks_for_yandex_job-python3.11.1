import json


# Using the stability property of python's standard sort - Timsort 
#   to sequentially sort nested dictionaries by multiple values
def sort_nested_dictionaries(feeds_of_store):
    feeds_of_store.sort(key=lambda feed: feed["offer_id"])
    feeds_of_store.sort(key=lambda feed: feed["price"])

    return feeds_of_store


if __name__ == "__main__":
    with open("input.txt") as input_file:
        _ = input_file.readline()

        feeds_of_store = []
        for line in input_file:
            offers = json.loads(line.strip())
            feeds_of_store.extend(offers["offers"])

    sort_nested_dictionaries(feeds_of_store)
    converted_json_for_feeds = json.dumps({"offers": feeds_of_store})

    with open("output.txt", "w") as output_file:
        print(converted_json_for_feeds, file=output_file)