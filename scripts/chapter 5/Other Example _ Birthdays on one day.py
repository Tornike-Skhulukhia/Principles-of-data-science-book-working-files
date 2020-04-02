'''
    Write a function which gets number of people
    (in a room) and returns the probability that at 
    least two of them have birtday on the same day  
'''

def get_probability_percentage(num_of_people):
    # probability that no one has a birthday on same date
    no_one_on_same_date_prob = 1

    for i in range(1, num_of_people):
        no_one_on_same_date_prob *= (365 - i)/365

    return (1 - no_one_on_same_date_prob) * 100


# graph
import matplotlib.pyplot as plt
plt.style.use('dark_background')

people_num = list(range(2, 100))
probabilities = [get_probability_percentage(i) for i in people_num]

plt.bar(people_num, probabilities)
plt.title('Number of people & probability that at least 2 of them have birthday on the same day')
plt.xlabel('Number of people')
plt.ylabel('Probability(%)')
plt.show()
