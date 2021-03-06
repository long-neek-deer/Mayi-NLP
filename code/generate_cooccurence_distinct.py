import pandas as pd
from pandas import DataFrame
from config import isCase
path = './feature/'


def cooccurrence_terms(lst1, lst2, join_str="__"):
    lst1 = lst1.split(" ")
    lst2 = lst2.split(" ")
    terms = [""] * len(lst1) * len(lst2)
    cnt =  0
    for item1 in lst1:
        for item2 in lst2:
            terms[cnt] = item1 + join_str + item2
            cnt += 1
    res = " ".join(terms)
    # res: 'apple_eat sleep_well'
    return res

def prepare_cooccurrence(path,out):

    data_input = pd.read_csv(path)
    data_ouput = DataFrame(columns=['sen1_sen2_distinct_unigram'])
    for index,row in data_input.iterrows():
        s1 = str(row['sen1_distinct_unigram'])
        s2 = str(row['sen2_distinct_unigram'])
        coo_terms = cooccurrence_terms(s1,s2)
        data_ouput.loc[index] = [coo_terms]
    data_ouput.to_csv(out,index=False)

if isCase == False:
    prepare_cooccurrence(path+'train_distinct_unigram.csv',path+'train_cooccurrence_distinct.csv')
    prepare_cooccurrence(path+'test_distinct_unigram.csv',path+'test_cooccurrence_distinct.csv')
else:
    prepare_cooccurrence(path+'case_distinct_unigram.csv',path+'case_cooccurrence_distinct.csv')

