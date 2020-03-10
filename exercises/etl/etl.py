def transform(old):
    new_data = {}
    for i, (point, letters) in enumerate(old.items()):
        for letter in letters:
            new_data[letter.lower()] = point

    return new_data

