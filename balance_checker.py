from stack import Stack


def check_balance(somestring):
    s = Stack()
    symbols = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    open_symbol = symbols.values()
    close_symbol = symbols.keys()

    for symbol in somestring:
        if symbol in open_symbol:
            s.push(symbol)
        elif symbol in close_symbol:
            if not s.isEmpty:
                peek = s.peek
                if symbols[symbol] == peek:
                    s.pop
                else:
                    return False
            else:
                return False
    return s.isEmpty


if __name__ == '__main__':
    somestring = str(input('Enter string for check balance: ')).strip()
    if check_balance(somestring):
        print('Balance')
    else:
        print('Not Balance')