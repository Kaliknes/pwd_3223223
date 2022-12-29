from random import choice
from random import randint
from itertools import permutations


def ap_random_char(lists):
    return lists.append(choice(char))


def ap_random_char_up(lists):
    return lists.append(choice(char).upper())


def ap_random_num(lists):
    return lists.append(str(randint(0, 9)))


def ap_random_especial_char(lists):
    return lists.append(choice(especial_char))


def password_generator(length):
    if length > 99:
        return "TOO LONG"
    perm_options = [i for i in permutations([b for b in range(1, 5)])]
    password = []

    for xx in range(0, int(length / 2)):
        n = choice(perm_options)
        for ind in range(0, 4):
            if n[ind] == 1:
                ap_random_char(password)
            elif n[ind] == 2:
                ap_random_num(password)
            elif n[ind] == 3:
                ap_random_char_up(password)
            elif n[ind] == 4:
                ap_random_especial_char(password)

    if len(password) == length:
        return "".join(password)
    elif len(password) > length:
        while len(password) > length:
            password.pop()
        return "".join(password)
    elif length == 1:
        ap_random_char(password)
        return "".join(password)
    else:
        return "ERROR"


char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']
especial_char = ['!', '@', '#', '$', '%', '&', '^', '-', '(', ')', '¡', ']', '[', '{', '}', '¿', '?']


def main():
    try:
        print("""
        
    ██████   █████  ███████ ███████ ██     ██  ██████  ██████  ██████  
    ██   ██ ██   ██ ██      ██      ██     ██ ██    ██ ██   ██ ██   ██ 
    ██████  ███████ ███████ ███████ ██  █  ██ ██    ██ ██████  ██   ██ 
    ██      ██   ██      ██      ██ ██ ███ ██ ██    ██ ██   ██ ██   ██ 
    ██      ██   ██ ███████ ███████  ███ ███   ██████  ██   ██ ██████  
                                                                       
    
     ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  
    ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
    ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  
    ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
     ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██ 
                                                                                                                                 
        """)
        ans = int(input("How length you want your password?\n(Tip: < 8 is weak, = 8 is medium, 15 < "
                        "is strong)\n> "))

        pwd = password_generator(ans)
        if pwd == "TOO LONG":
            print("TOO LONG")
        elif pwd != "TO LONG":
            print(f"Your new password is", pwd)
    except ValueError:
        print("ERROR IN VALUE")
    except Exception as g:
        print("ERROR")
        print(g)


if __name__ == '__main__':
    main()
