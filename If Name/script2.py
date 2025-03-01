from script1 import *

def favorite_series(series):
    print(f"My favorite movie is {series}")

def main():
    print("This is script2")
    favorite_movie("The Matrix")
    favorite_series("The Office")
    print("End of script2")

if __name__ == '__main__':
    main()