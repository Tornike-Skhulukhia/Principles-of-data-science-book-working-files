import pandas as pd

df = pd.read_csv(
        'https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_15/master/data/titanic.csv')

# df = df[['Sex', 'Survived', 'Pclass']]
df.rename({'Sex': 'sex',
           'Survived': 'survived',
           'Pclass': 'ticket_class'},
           axis=1, inplace=True)


# calculate that any given person survived
# not taking into account any other factor
p_survived = (df['survived'] == 1).sum() / df.shape[0]
p_not_survived = 1 - p_survived  # because these are complementary events

# probability that passanger is male/female
p_male = (df['sex'] == 'male').sum() / df.shape[0]
p_female = 1 - p_male

### Gender
# Question: Did having a certain gender affect the survival rate?
# estimate: chance that someone survived, given that they were female
'''
    P(Survived | Female) = P(Survived and Female) / p(Female)
'''
# P(Survived and Female) = P(Survived) * P(Female | Survived)
p_survived_and_female = ((df['survived'] == 1) & (df['sex'] == 'female')).sum() / df.shape[0]
p_survived_given_female = p_survived_and_female / p_female

p_survived_and_male = ((df['survived'] == 1) & (df['sex'] == 'male')).sum() / df.shape[0]
p_survived_given_male = p_survived_and_male / p_male


print(f"{'Chances of survival':^50}\n{'='*50}")
print(f"Without knowing anything about you: {p_survived:.2%}".center(50))
print("=" * 50)
print(f"{'If you were Female':<40} : {p_survived_given_female:.2%}")
print(f"{'If you were male':<40} : {p_survived_given_male:.2%}")

### Ticket Class
# P(Survived | Ticket_Class_1)
p_survived_given_ticket_class_1 = ((df['ticket_class'] == 1) & (df['survived'] == 1)).sum() / (df['ticket_class'] == 1).sum()

# P(Survived | Ticket_Class_2)
p_survived_given_ticket_class_2 = ((df['ticket_class'] == 2) & (df['survived'] == 1)).sum() / (df['ticket_class'] == 2).sum()

# P(Survived | Ticket_Class_3)
p_survived_given_ticket_class_3 = ((df['ticket_class'] == 3) & (df['survived'] == 1)).sum() / (df['ticket_class'] == 3).sum()

print("-" * 50)
print(f"{'If you had ticket class 1':<40} : {p_survived_given_ticket_class_1:.2%}")
print(f"{'If you had ticket class 2':<40} : {p_survived_given_ticket_class_2:.2%}")
print(f"{'If you had ticket class 3':<40} : {p_survived_given_ticket_class_3:.2%}")

print("\n" * 10)
print("But wait, we are programers, right?")
print("\n" * 2)
print("=" * 50)

# few changes
df.rename({'Embarked': 'embarked',
            'SibSp': 'siblings_spouses_num_onboard',
            'Parch': 'parent_children_num_onboard',
            },
            axis=1, inplace=True)

df['embarked'] = df['embarked'].replace({'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'})
df['embarked'].fillna('Not Available', inplace=True)

# generate simple previous counts from these
cols = ['embarked',
        'ticket_class',
        'sex',
        'siblings_spouses_num_onboard',
        'parent_children_num_onboard']

print(f"{'Chances of survival by specific characteristics':^80}\n{'='*80}")
print("=" * 80)
# & just print the results
for col_name in cols:
    for col_value in sorted(df[col_name].unique()):
        # breakpoint()
        p_survived_with_this_characteristic = ((df['survived'] == 1) & (df[col_name] == col_value)).sum() / (df[col_name] == col_value).sum()
        print(f"Chance if {col_name} = {col_value}".ljust(60), f'{p_survived_with_this_characteristic:.2%}')
    print('-' * 80)
