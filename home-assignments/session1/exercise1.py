import sys
import json
import yaml

args = sys.argv
if len(args) < 2:
    print('Error: missing file name')
    exit(1)

infile = args[1]
fp = open(infile)
j = json.load(fp)
fp.close()

borders = sorted(j['buckets'])
buckets = {border:[] for border in borders}
other = []

print(buckets)

ppl_ages = j['ppl_ages']
for name in ppl_ages:
    age = ppl_ages[name]
    for bucket in buckets:
        if age < bucket:
            buckets[bucket].append(name)
            break
    else:
        other.append(name)

print(buckets)
print(other)

result = {}
prev = 0
for curr in buckets:
    key = '{}-{}'.format(prev, curr)
    value = buckets[curr]
    result[key] = value
    prev = curr

maxage = max(ppl_ages.values())

key = '{}-{}'.format(curr, maxage)
value = other
result[key] = value

splitname = infile.split('.')
splitname[-1] = 'yaml'
outfile = '.'.join(splitname)
fp = open(outfile, 'w')
fp.write(yaml.dump(result))
fp.close()