#! /usr/bin/env python


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
    return ''.join(_conv_to_symbol(p) for p in pieces)


if __name__ == '__main__':
    assert(_conv_to_symbol('0000') == '0')
    assert(_conv_to_symbol('0010') == '2')
    assert(_conv_to_symbol('1010') == '+')
    assert(_conv_to_symbol('1110') == '')
    assert(conv_to_expression('000111000001') == '1*1')

    print 'All tests passed'
