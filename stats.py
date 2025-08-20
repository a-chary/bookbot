def get_num_words(text):
    num = len(text.split())
    return num

def char_count(text):
    char_dic = {}
    for char in text:
        if char.lower() in char_dic:
            char_dic[char.lower()] += 1
        else:
            char_dic[char.lower()] = 1
    return char_dic

def sort_on(items):
    return items["num"]

def sorted_dic_list(char_dic):
    dic_list = [{"char":k, "num":v} for k,v in char_dic.items()]
    dic_list.sort(reverse=True, key=sort_on)
    return dic_list
