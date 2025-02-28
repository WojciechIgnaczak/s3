import pandas as pd
import random
file="data_01.dat"

columns_names=['timestamp','identyfikator','dane czasowe 1','dane czasowe 2','dane dyskretne','napisy(nazwiska)','wart. ciagle z wart odstajacymi1','wart. ciagle z wart odstajacymi2','odstające na plus','odstające na minus','przestrzenne X','przestrzenne Y','przestrzenne Z']
df=pd.read_csv(file,header=None,names=columns_names)
print(df.sort_values(by='timestamp'))





# zliczanie dyskretnych
dyskretne_dane=df['dane dyskretne'].value_counts().sort_values()




# czy identyfikator działa
#pattern=r'(1|...|9)(0{0-10})(Rand(100-10000))(($1+$3)%2)'


matches = df['identyfikator'].apply(str).str.extract(r'([1-9])(0{0,10})(\d+)')
matches[2]=matches[2].astype(str).str[:-1]
pierwsza_liczba = matches[0].astype(int)
druga_liczba=matches[2].astype(int)
check_number=(pierwsza_liczba+druga_liczba)%2

real_check_number = df["identyfikator"].astype(str).str[-1].astype(int)


checking_check_number = pd.DataFrame({
    'identyfikator': df['identyfikator'],
    'real_check_number': real_check_number,
    'my_check_number': check_number,

})

checking_check_number['bool']= checking_check_number['real_check_number'] == checking_check_number['my_check_number']



# duplikaty identyfikatorów
duplikaty=df['identyfikator'].drop_duplicates()
