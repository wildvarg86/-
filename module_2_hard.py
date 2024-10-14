from random import randint
random_number = randint(3, 20)
print(random_number)

def password_search():
    password_ = ''
    for i in range(1, 21):
        for j in range(i, 21):
            if (i + j) >= 20:
                continue
            elif i == j:
                continue
            elif random_number % (i + j) == 0:
                password_ += f'{i}{j}'

    return password_

password = password_search()
print(password)
