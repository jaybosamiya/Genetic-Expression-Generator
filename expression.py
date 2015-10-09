#! /usr/bin/env python

_allowed_symbol_list = '0123456789+-*/'


def _conv_to_symbol(bin_string):
    assert(len(bin_string) == 4)
    val = int(bin_string, 2)
    if val < 10:
        return str(val)
    elif val < 14:
        return '+-*/'[val - 10]
    else:
        return ''


def conv_to_expression(bin_string):
    num_of_symbols = len(bin_string) / 4
    pieces = [bin_string[i * 4:i * 4 + 4] for i in range(num_of_symbols)]
    # TODO : Make sure that it is a valid expression
    return ''.join(_conv_to_symbol(p) for p in pieces)


def _get_4_bit_repr(val):
    return ''.join(str((val & x) / x) for x in [8, 4, 2, 1])


def _conv_symbol_to_bin(symbol):
    assert(len(symbol) == 1)
    assert(symbol in _allowed_symbol_list)
    val = _allowed_symbol_list.index(symbol)
    return _get_4_bit_repr(val)


def conv_to_bin_string(expression):
    return ''.join(_conv_symbol_to_bin(e) for e in expression)


if __name__ == '__main__':
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

    print 'All tests passed'
