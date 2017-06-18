import math

CONSTANT = 10

def run():
    for i in range(20):
        global CONSTANT
        CONSTANT = CONSTANT + 1

    return CONSTANT

if __name__ == "__main__":
    print(run())
