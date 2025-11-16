def extract_root(word, pattern):
    root = ''
    try:
        for i in range(len(pattern)):
            if pattern[i] in ['ف', 'ع', 'ل']:
                root += word[i]
    except IndexError:
        print(f"Could not extract root for '{word}' with pattern '{pattern}'")
    return root

with open("الفروع.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("الجذور.txt", "w", encoding="utf-8") as f:
    for line in lines:
        line = line.strip()
        if not line:
            continue

        pattern, word = line.split(" = ")
        root_pattern = extract_root(pattern, pattern)
        root_word = extract_root(word, pattern)
        f.write(f"{root_pattern} = {root_word}\n")
