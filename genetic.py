#! /usr/bin/env python

initialized = False


def gen_random_candidate():
    from random import randint
    size = randint(low_size, high_size)
    return ''.join(str(randint(0, 1)) for _ in range(size))


def initialize(pop, l_size, h_size, fitness_function, crossover, mutation):
    global generation_population, low_size, high_size, initialized, candidates
    global fitness, crossover_rate, mutation_rate
    generation_population, low_size, high_size, initialized = pop, l_size, h_size, True
    candidates = [gen_random_candidate() for _ in range(generation_population)]
    fitness, crossover_rate, mutation_rate = fitness_function, crossover, mutation


def _get_fitnesses():
    fitness_val = dict()
    net_fitness = 0
    for v in candidates:
        fitness_val[v] = fitness(v)
        net_fitness += fitness_val[v]
    return fitness_val, net_fitness


def next_generation():
    from random import uniform, randint
    fitness_val, net_fitness = get_fitnesses()
    new_pop = []

    def pick_parent():
        val = uniform(0, net_fitness)
        for v in candidates:
            val -= fitness_val[v]
            if val <= 0:
                return v

    def do_crossover(p1, p2):
        c1, c2 = randint(0, len(m)), randint(0, len(n))
        return p1[:c1] + p2[c2 + 1:], p2[:c2] + p1[c1 + 1:]

    def mutate(o):
        ret = []
        for b in o:
            if uniform(0, 1) < mutation_rate:
                ret.append(str(1 - int(b)))
            else:
                ret.append(b)
        return ''.join(ret)

    while len(new_pop) < generation_population:
        org1, org2 = pick_parent(), pick_parent()
        if uniform(0, 1) < crossover_rate:
            org1, org2 = do_crossover(org1, org2)
        org1 = mutate(org1)
        org2 = mutate(org2)
        new_pop.append(org1)
        new_pop.append(org2)

    candidates = new_pop


def get_fittest(n):
    fitness_val, _ = _get_fitnesses()
    rev_sorted_pop = sorted(candidates, key=lambda p: fitness_val[p])
    sorted_pop = rev_sorted_pop[::-1]
    return sorted_pop[:n]
