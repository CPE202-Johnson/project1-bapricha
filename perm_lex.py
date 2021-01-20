# str -> list
#
def perm_gen_lex(a):
    perm_list = []
    perm_gen_lex_helper(a, perm_list)
    perm_list.sort()
    return perm_list


def perm_gen_lex_helper(str, perm_list):
    if len(str) == 1 or len(str) == 0:
        perm_list.append(str)
        return perm_list
    else:
        for char in str:
            new_str = str.replace(char, '', 1)
            new_list = perm_gen_lex_helper(new_str, [])
            for i in range(len(new_list)):
                new_list[i] = char + new_list[i]
            perm_list += new_list
        return perm_list
