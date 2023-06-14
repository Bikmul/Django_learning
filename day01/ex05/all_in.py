import sys

def run(str):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    arr = [elem.strip() for elem in str.split(',') if elem.strip()]
    i=0
    while i < len(arr):
        c=0
        for k,v  in capital_cities.items():
            if v.lower() == arr[i].lower():
                for key, val in states.items():
                    if k == val:
                        print(f'{v} is the capital of {key}')
                        c=c+1
        for k,v  in states.items():
            if k.lower() == arr[i].lower():
                for key, val in capital_cities.items():
                    if v == key:
                        print(f'{val} is the capital of {k}')
                        c=c+1
        if c == 0:
            print(f'{arr[i]} is neither a capital city nor a state')
        i = i+1



if __name__ == '__main__':
    if( len(sys.argv) == 2):
        run(sys.argv[1])