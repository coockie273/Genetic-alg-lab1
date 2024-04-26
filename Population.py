import random


class ExtremumFinder:

    def __init__(self, power, iteration, p_kross, p_mut, function):
        self.population = []
        self.power = power
        self.iteration = iteration
        self.p_kross = p_kross
        self.p_mut = p_mut
        self.func = function

        for i in range(0, power):
            chromosome = ""
            for j in range(0, 14):
                gen = random.randint(0, 1)
                chromosome += str(gen)
            self.population.append(chromosome)

    def value(self, chromosome):
        decimal_value = int(chromosome, 2)
        return self.func(0.5 + (decimal_value * 10.5) / (2 ** 14 - 1))

    def reproduction(self, sum):
        probabilities = []


        for individual in self.population:
            probabilities.append((self.value(individual) + 1) / sum)

        new_population = random.choices(self.population, probabilities, k=self.power)

        self.population = new_population

    def krossingover(self, p):
        random_number = random.random()
        if random_number < p:
            individual1 = random.choice(self.population)
            self.population.remove(individual1)

            individual2 = random.choice(self.population)
            self.population.remove(individual2)

            k = random.randint(0, 13)

            for i in range(0, 14):
                if i < k:
                    char_list = list(individual1)
                    char_list[i] = individual2[i]
                    individual1 = "".join(char_list)
                else:
                    char_list = list(individual2)
                    char_list[i] = individual1[i]
                    individual2 = "".join(char_list)

            self.population.append(individual1)
            self.population.append(individual2)

    def mutation(self, p):
        for chromosome in self.population:
            random_number = random.random()
            if random_number < p:
                self.population.remove(chromosome)
                k = random.randint(0, 13)
                if chromosome[k] == "0":
                    char_list = list(chromosome)
                    char_list[k] = "1"
                    chromosome = "".join(char_list)
                else:
                    char_list = list(chromosome)
                    char_list[k] = "0"
                    chromosome = "".join(char_list)
                self.population.append(chromosome)

    def start(self):
        for i in range(0, self.iteration):
            sum = 0

            for individual in self.population:
                sum += (1 + self.value(individual))

            avg = sum / len(self.population)

            self.reproduction(sum)
            self.krossingover(self.p_kross)
            self.mutation(self.p_mut)

        return max(map(self.value, self.population))
