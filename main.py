import pandas as pd 
from src.graphs import *
from src.pdf import *
from src.table import *
from src.mail import *
from src.parser import *

def main():
    
    #Read CSV
    df = pd.read_csv('./output/mining.csv', encoding='latin-1')
    df=df.drop('Unnamed: 0',axis=1)

    #Make Graphs
    make_graphs(df,pars.args.p1,pars.args.p2)

    #Generate Table
    generate_big_table(df,pars.args.p1)
    generate_big_table(df,pars.args.p2)

    #Make Report
    generate_report(df,pars.args.p1,pars.args.p2)

    #Send mail 
    generate_mail(pars.args.p3, pars.args.p1, pars.args.p2)

if __name__ == "__main__":
    pars = ParserKey()
    main()

