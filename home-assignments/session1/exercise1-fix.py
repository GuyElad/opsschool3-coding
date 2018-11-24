import json
from sys import argv
import yaml


def my_dict_json(json_file):
    try:
        with open(json_file) as input_file:
            my_dict = json.load(input_file)
            return my_dict
    except FileNotFoundError:
            print("Error: missing file name", argv[1])
    exit(1)


def split_to_buckets(ppl_ages, buckets, other):
    for name in ppl_ages:
        age = ppl_ages[name]
        for bucket in buckets:
            if age < int(bucket.split('-', 1)[1]):
                buckets[bucket].append(name)
                break
        else:
            other.append(name)
    return buckets


def border_order(json_file):
    borders = sorted(json_file['buckets'])
    buckets: dict = {border: [] for border in borders}
    other = []
    result: dict = {}
    prev = 0
    ppl_ages = json_file['ppl_ages']
    maxage = max(ppl_ages.values())
    for curr in buckets:
        key = '{}-{}'.format(prev, curr)
        value = buckets[curr]
        result[key] = value
        prev = curr
    key = '{}-{}'.format(prev, maxage)
    value = other
    result[key] = value
    return buckets, other, result


def output_file(all_ppl_clustered):
    with open('my_dict.yaml', 'w') as results_file:
        try:
            yaml.dump(all_ppl_clustered, results_file, default_flow_style=False, allow_unicode=True)
        except ValueError:
            print("Error: can't export to .yaml file")


def main():
    json_file = my_dict_json('my_dict.json')
    buckets, other, result = border_order(json_file)
    ppl = json_file['ppl_ages']
    all_ppl_clustered = split_to_buckets(ppl, result, other)
    output_file(all_ppl_clustered)


if __name__ == '__main__':
    main()


