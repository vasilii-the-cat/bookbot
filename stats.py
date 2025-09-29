def get_num_words(content):
    words = content.split()
    return len(words)

def get_character_count(content):
    character_count = {}
    for character in content:
        lower_case_character = character.lower()
        if lower_case_character in character_count:
            character_count[lower_case_character] += 1
        else:
            character_count[lower_case_character] = 1
    return character_count

def sort_on(items):
    return items["num"]

def get_sorted_character_data(unsortet_character_count):
    character_count_list = []

    for k, v in unsortet_character_count.items():
        character_count_list.append({
            "char": k,
            "num": v
        })
    
    character_count_list.sort(reverse=True, key=sort_on)
    return character_count_list