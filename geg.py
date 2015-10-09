#! /usr/bin/env python


def fitness_function(bin_string):
    from expression import eval_bin_string
    val = eval_bin_string(bin_string)
    if val == required_int:
        ret = float("inf")
    else:
        ret = 1 / abs(float(val) - float(required_int))
    return ret

if __name__ == '__main__':
    import genetic
    from expression import eval_bin_string, conv_to_expression
    global required_int
    required_int = int(raw_input('Input integer: '))
    genetic.initialize(50, 4, 100, fitness_function, 0.7, 0.001)
    while True:
        fittest = genetic.get_fittest(5)
        for v in fittest:
            print eval_bin_string(v),
        print
        if eval_bin_string(fittest[0]) == required_int:
            break
        genetic.next_generation()
    print "Found expression: %s" % conv_to_expression(genetic.get_fittest(1)[0])
