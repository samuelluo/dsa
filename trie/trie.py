
# ---------------------------------------------------------
def make_trie(words):
    root = dict()
    for w in words:
        current_dict = root
        for l in w:
            if l not in current_dict.keys():
                current_dict[l] = {}
            current_dict = current_dict[l]
        current_dict['*'] = None
    return root

def word_in_trie(word, root):
    while len(word) != 0:
        c = word[0]
        word = word[1:]
        if c not in root.keys():
            return False
        else:
            root = root[c]
    return True

def words_with_prefix(prefix, root):
    # Find the prefix
    words = []
    for c in prefix:
        if c not in root.keys():
            return words
        else:
            root = root[c]

    # Find children
    queue = [(root, prefix)]
    while len(queue) != 0:
        node, curr_prefix = queue.pop(0)
        for c in node.keys():
            if c == '*':
                words.append(curr_prefix)
            else:
                queue.append((node[c], curr_prefix + c))
    return words

# ---------------------------------------------------------
# Build trie
words = ['to', 'tea', 'ted', 'ten', 'A', 'in', 'inn', 'inning']
trie = make_trie(words)
print(trie)

# Check if words in trie
print(word_in_trie('tea', trie))
print(word_in_trie('te', trie))

# Return words in trie with prefix
words = words_with_prefix('te', trie)
print(words)
words = words_with_prefix('i', trie)
print(words)
words = words_with_prefix('inning', trie)
print(words)