# python3
hashes = []

def _hash_func(s):
        return sum([ord(s[i]) for i in range(len(s))])

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def precomputeHashes(text, pattern):
	global hashes
	hashes.append(_hash_func(text[:len(pattern)]))

	for i in range(1, len(text) - len(pattern) + 1):
		old_hash = hashes[i - 1]
		left_hash = ord(text[i-1])
		right_hash = ord(text[i + len(pattern) - 1])
		hashes.append(old_hash - left_hash + right_hash)

def get_occurrences(pattern, text):
    precomputeHashes(text, pattern)
    occurences = []
    plen = len(pattern)
    tlen = len(text)
    phash = _hash_func(pattern)
    for i in range(tlen - plen + 1):
    	if phash != hashes[i]:
    		continue
    	if pattern == text[i:i + plen]:
    		occurences.append(i)
    return occurences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
