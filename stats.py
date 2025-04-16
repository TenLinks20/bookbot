def count_words(text:str) -> int:
    text_ls = text.split()
    count = len(text_ls)
    return count

def sort_on(dict):
        return dict["count"]

def count_characters(text:str) -> dict:
    chars = {}
    for char in text:
        lowercase = char.lower()
        if lowercase in chars:
            chars[lowercase] += 1
        else:
            chars[lowercase] = 1
    return chars

def character_info(char_count:dict) -> list:
    char_profile = []
    for char in char_count:
        char_dict = {"character": char, "count": char_count[char]}
        
        char_profile.append(char_dict)
    
    char_profile.sort(reverse=True, key=sort_on)
    return char_profile 