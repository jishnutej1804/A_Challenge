from collections import deque


def word_ladder(begin_word, end_word, word_list):
    word_set = set(word_list)

    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        word, length = queue.popleft()

        if word == end_word:
            return length

        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + char + word[i + 1:]

                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, length + 1))

    return 0


print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(word_ladder("hit", "hot", ["hot"]))
print(word_ladder("a", "c", ["a", "b", "c"]))