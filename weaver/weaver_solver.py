# manually adding invalid words since text file does not
# completely align with Weaver's accepted words

excluded = {"sven", "oren", "saam", "dack", "derk", "herk"}

with open("downloads/weaver/english.txt", "r") as f:
    text = f.readlines()
    possible_words = {}
    priority = 0
    # lower priority = higher frequency in English
    for line in text:
        line = line.split()
        w = line[1]
        if len(w) == 4 and w not in excluded:
            possible_words[w] = priority
            priority += 1

# manually adding words to dictionary, giving them the highest possible priority
add = ["plat"]

for new_w in add:
    possible_words[new_w] = 0


def get_neighbors(word):
    """
    Given a starting word, returns a list of all possible neighbors

    Args:
        word: string of length 4, representing a valid English word
    Returns:
        list of all possible neighbors (len 4 English words), ordered
        in decreasing frequency
        (a neighbor is a valid word changed by 1 letter)
    """
    # want neighbors to be ordered from
    all_neighbors = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # for every place, try changing every letter
    for place, i_let in enumerate(word):
        for letter in alphabet:
            if i_let != letter:
                new_word = word[:place] + letter + word[place + 1 :]
                if new_word in possible_words:
                    # if new_word is a valid word add to all neighbors list
                    all_neighbors.append((new_word, possible_words[new_word]))

    # sort by decreasing frequency
    all_neighbors = sorted(all_neighbors, key=lambda x: x[1])
    all_neighbors = [x[0] for x in all_neighbors]

    # return sorted neighbors list
    return all_neighbors


def weaver_solver(start, goal):
    """
    Given a start state (word of length four), find shortest path until goal is met

    Args:
        start: English word of length 4
        goal: same
    Returns:
        list of path from start to goal
        string 'No paths were found' if not possible
    """
    # checks valid start and goal parameters
    if len(start) != 4 or len(goal) != 4:
        return "Words must be length 4!"
    if start not in possible_words:
        return "Starting word is invalid!"
    if goal not in possible_words:
        return "Target word is invalid!"

    queue = [[start]]

    while queue:
        current_path = queue.pop(0)
        # last is the most recently traversed word in path
        last = current_path[-1]
        # iterate through possible neighbors (in decreasing freq)
        # and create new paths for each neighbor
        for neighbor in get_neighbors(last):
            # words cannot be repeated in a given path
            if neighbor not in current_path:
                new_path = current_path + [neighbor]
                # termination, target found
                if neighbor == goal:
                    return new_path[1:]
                # append whole path to queue
                queue.append(new_path)
    # if queue is empty, no paths were found => failure
    return "No paths were found!"


def find_changes(start, path):
    """
    Helper function for weaver_hints
    Finds the single letter changes between words in a path

    Args:
        start: 4 letter word (str)
        path: list of 4 letter words (strs) connected by one letter
    Returns:
        List of ordinal numbers where letters get changed (i.e 1st, 2nd, etc.)
    """
    changes = []
    mapping = {0: "first", 1: "second", 2: "third", 3: "fourth"}
    complete_path = [start] + path
    for word1, word2 in zip(complete_path[:-1], path):
        for i in range(4):
            if word1[i] != word2[i]:
                changes.append(mapping[i])
                break
    return changes


def weaver_hints(start, goal):
    """
    Receives player input to receive progressive hints

    Args:
        start: 4 letter starting word (str)
        goal: 4 letter target word (str)
    Prints:
        Hints if player continually accepts hints
        Terminating message if the opposite
    """
    solved = weaver_solver(start, goal)
    # using the find_changes helper function,
    # finds the letters changed between sequential pairs of words
    mapped = find_changes(start, solved)

    order = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
    ]

    # No path
    if isinstance(solved, str):
        return "No paths were found"

    # reveal length of word
    hint1 = input("Would you like to receive the first hint? (Y/N)")
    if hint1 == "Y":
        print(f"The optimal solution is length {len(solved)}")
    elif hint1 == "N":
        return "No worries! Call this function again if you change your mind."

    # reveal changes in letters
    for num, change in enumerate(mapped, 1):
        inp = input(f"Would you like to receive the {order[num]} hint? (Y/N)")
        if inp == "Y":
            print(f"Change the {change} letter for the {order[num-1]} word.")
        elif inp == "N":
            return "No worries! Call this function again if you change your mind."

    # reveal complete path
    reveal = input("Would you like to reveal the path? (Y/N)")
    if reveal == "Y":
        return solved
    return "No worries! Call this function again if you change your mind."


if __name__ == "__main__":
    pass
