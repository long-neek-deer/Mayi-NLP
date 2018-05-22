import pandas as pd
from pandas import DataFrame
from config import isCase
path = './feature/'


def distinct_terms(lst1, lst2):
    lst1 = lst1.split(" ")
    lst2 = lst2.split(" ")
    common = set(lst1).intersection(set(lst2))
    new_lst1 = ' '.join([w for w in lst1 if w not in common])
    new_lst2 = ' '.join([w for w in lst2 if w not in common])
    
    return (new_lst1,new_lst2)

def prepare_distinct(path,out):
    data_input = pd.read_csv(path)
    data_ouput = DataFrame(columns=['sen1_distinct_unigram','sen2_distinct_unigram'])
    for index,row in data_input.iterrows():
        s1 = str(row['sen1_unigram'])
        s2 = str(row['sen2_unigram'])
        coo_terms = distinct_terms(s1,s2)
        data_ouput.loc[index] = [coo_terms[0],coo_terms[1]]
    data_ouput.to_csv(out,index=False)


if isCase == False:
    prepare_distinct(path+'train_unigram.csv',path+'train_distinct_unigram.csv')
    prepare_distinct(path+'test_unigram.csv',path+'test_distinct_unigram.csv')
else:
    prepare_distinct(path+'case_unigram.csv',path+'case_distinct_unigram.csv')