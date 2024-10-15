calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    print((len(string), string.upper(), string.lower()))

def is_contains(string, list_to_search):
    count_calls()
    list_to_search = list(map(str.lower, list_to_search))
    string = string.lower()
    if string in list_to_search:
        print(True)
    else:
        print(False)


string_info('Армагедон')
string_info('Параметр')
string_info('Игра')
is_contains('Армагедон',['армагеДОН', 'ДУРдом', 'Армавир'])
is_contains('Параметр',['армагеДОН', 'ДУРдом', 'Армавир'])
print(calls)
