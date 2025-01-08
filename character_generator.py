import urandom

def generate_random_character():
    # Generate a random number between 0 and 61 (for letters a-z, digits 0-9, and special characters)
    # ASCII range for special characters: 33-47, 58-64, 91-96, 123-126
    ranges = [(ord('a'), ord('z')), (ord('0'), ord('9')), (33, 47), (58, 64), (91, 96), (123, 126)]
    
    def get_random_from_ranges():
        range_index = urandom.getrandbits(3) % len(ranges)
        start, end = ranges[range_index]
        return urandom.randint(start, end)

    random_character = chr(get_random_from_ranges())
    return random_character
