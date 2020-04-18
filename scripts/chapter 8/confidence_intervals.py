from point_estimates  import (
                            breaks as population, # population
                            np,
                            stats,
                                )

population_mean = np.mean(population)

confidence = 0.95
sample_size = 100

cases_num = 100



number_of_correct_guesses = 0

for i in range(cases_num):

    sample = np.random.choice(population, sample_size)

    lower_bound, upper_bound = stats.t.interval(
        alpha=confidence,   # confidence level
        df=sample_size-1,   # degree of freedom
        loc=np.mean(sample),
        scale=(np.std(sample) / np.sqrt(sample_size)) # estimate of population std (?)
        # scale=stats.sem(sample)   # vs standard error of the mean (?)
    )
    if lower_bound <= population_mean <= upper_bound:
        number_of_correct_guesses += 1

    # print(f'Actual Mean: {population_mean}')
    # print(f'{confidence:.0%} Confidence interval boundaries are {lower_bound} - {upper_bound}')

print(f'From {cases_num} cases correct prediction'
      f' was made {number_of_correct_guesses} times ({number_of_correct_guesses/cases_num*100}%)')