

def longest_common_permutation(a, b):
    a_set = set(a)
    b_set = set(b)
    common_chars = []

    for ch in a:
        if ch in b_set:
            b_set.remove(ch)
            common_chars.append(ch)

    common_chars = sorted(common_chars)
    return ''.join(common_chars)

while True:
    try:
        a = input().strip()
        b = input().strip()
        lcs = longest_common_permutation(a, b)
        print(lcs)
    except EOFError:
        break
