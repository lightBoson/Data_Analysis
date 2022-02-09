import pandas as pd
import os

def main():   
    file_path, number = welcome()
    df = read_csv(file_path)
    export(number, file_path, df)

#Function welcome in the script
def welcome():
    print('Welcome to the csv converter script\n')
    print('Library used:', pd.__name__,pd.__version__)
    file_path = input('Read the path:\n')
    #check the path
    while not os.path.exists(file_path):
        print('Wrong path, try again')
        file_path = input('Read the path:\n')

    print('Choose the number of your final form:\n1 - JSON \n2 - HTML\n3 - Pickle\n4 - Hdf5\n')
    #check the number
    while True:
        try:
            number = int(input('The number is:\n'))
        except ValueError:
            print("It is not the number, try again")
            continue
        else:
            break
    return file_path,number

#Function read csv   
def read_csv(file_path):
    df = pd.read_csv(file_path, sep= ',')
    return df
#Function ecport csv t json, html, pickle, hdf5
def export(number, file_path, df):
    if number == 1:
        df.to_json(file_path.replace('csv','json'))
    elif number == 2:
        df.to_html(file_path.replace('csv','html'))
    elif number == 3:
        df.to_pickle(file_path.replace('csv','pkl'))
    elif number == 4:
        df.to_hdf(file_path.replace('csv','hdf5'), 'df', format = 'table')
    else: number >= 5

if __name__ == "__main__":
   main()