#! /usr/bin/env python

_digits = '0123456789'
_operators = '+-*/'
_allowed_symbol_list = _digits + _operators


def _conv_to_symbol(bin_string):
    assert(len(bin_string) == 4)
    val = int(bin_string, 2)
    if val < len(_allowed_symbol_list):
        return _allowed_symbol_list[val]
    else:
        return ''


def _clean_up(expression):
    ret = []
    number = False
    for e in expression:
        if e in _digits:
            number = True
            ret.append(e)
        elif e in _operators:
            if number == False:
                continue
            else:
                number = False
                ret.append(e)
    if number == False:
        ret = ret[:-1]
    return ''.join(ret)


def conv_to_expression(bin_string):
    num_of_symbols = len(bin_string) / 4
    pieces = [bin_string[i * 4:i * 4 + 4] for i in range(num_of_symbols)]
    expression = _clean_up(''.join(_conv_to_symbol(p) for p in pieces))
    return expression


def _get_4_bit_repr(val):
    return ''.join(str((val & x) / x) for x in [8, 4, 2, 1])


def _conv_symbol_to_bin(symbol):
    assert(len(symbol) == 1)
    assert(symbol in _allowed_symbol_list)
    val = _allowed_symbol_list.index(symbol)
    return _get_4_bit_repr(val)


def conv_to_bin_string(expression):
    return ''.join(_conv_symbol_to_bin(e) for e in expression)


def eval_expr(expression):
    try:
        ret = eval(_clean_up(expression))
    except SyntaxError:
        ret = float('inf')
    except ZeroDivisionError:
        ret = float('inf')
    return ret

def eval_bin_string(bin_string):
    return eval_expr(conv_to_expression(bin_string))

if __name__ == '__main__':
    assert(_clean_up('123+/2') == '123+2')
    assert(_clean_up('123') == '123')
    assert(_clean_up('1') == '1')
    assert(_clean_up('123+2') == '123+2')
    assert(_clean_up('/123+2') == '123+2')
    assert(_clean_up('123+2/') == '123+2')

    assert(_conv_to_symbol('0000') == '0')
    assert(_conv_to_symbol('0010') == '2')
    assert(_conv_to_symbol('1010') == '+')
    assert(_conv_to_symbol('1110') == '')
    assert(conv_to_expression('000111000001') == '1*1')

    assert(_conv_symbol_to_bin('0') == '0000')
    assert(_conv_symbol_to_bin('2') == '0010')
    assert(_conv_symbol_to_bin('+') == '1010')
    assert(_conv_symbol_to_bin('/') == '1101')
    assert(conv_to_bin_string('11*12') == '00010001110000010010')

    assert(eval_expr('2+3') == 5)
    assert(eval_bin_string('00010001110000010010') == 132)

    print 'All tests passed'
