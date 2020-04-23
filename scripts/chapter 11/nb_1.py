import pandas as pd
import matplotlib.pyplot as plt
import sklearn

df = pd.read_table('https://raw.githubusercontent.com/sinanuozdemir/sfdat22/master/data/sms.tsv',
                   sep='\t', header=None, names=['label', 'msg'])
df.msg = df.msg.str.lower()

if __name__ == '__main__':
    p_ham, p_spam = df.label.value_counts(normalize=True)

    spams_df = df[df['label'] == 'spam']
    hams_df = df[df['label'] == 'ham']

    # df.label.value_counts().plot(kind='bar')

    # as it is classification problem, we choose most common one
    # null_accuracy = df.label.value_counts(normalize=True).max()


    # plt.show()
    p_spam_given_scn = p_ham_given_scn = 0 # find max of these

    # p(spam | scn) = 
    '''
                p(spam) * p( scn | spam)
                ------------------------
                        p(scn)               - no need to calculate as we compare numbers which are all divided to this
    '''
    p_scn_given_spam = 1

    for word in ['send', 'cash', 'now']:
        p_word_given_spam = spams_df.msg.str.contains(word).sum() / spams_df.shape[0]

        p_scn_given_spam *= p_word_given_spam
        print(word, p_word_given_spam)

    print('p( scn | spam) = ', p_scn_given_spam)


    # p(ham | scn) = 
    '''
                p(ham) * p( scn | ham)
                ------------------------
                        p(scn)               - no need to calculate as we compare numbers which are all divided to this
    '''
    p_scn_given_ham = 1

    for word in ['send', 'cash', 'now']:
        p_word_given_ham = hams_df.msg.str.contains(word).sum() / hams_df.shape[0]

        p_scn_given_ham *= p_word_given_ham
        print(word, p_word_given_ham)

    print('p( scn | ham) = ', p_scn_given_ham)


    spam_probability = p_spam * p_scn_given_spam     # / p(scn) 
    ham_probability = p_ham * p_scn_given_ham        # / p(scn)

    print('Probability that it is spam/it is ham = ', spam_probability/ham_probability)
