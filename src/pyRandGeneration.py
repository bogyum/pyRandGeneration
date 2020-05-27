'''
    RAND NUMBER GENERATION
      - 파라미터로 주어진 값의 범위에서 랜덤 값 생성
'''

import logging, sys, random

def getRandNumbers(min, max, choice):
    rand = []
    randNum = random.randint(min, max)

    for i in range(0, choice):
        while randNum in rand:
            randNum = random.randint(min, max)
        rand.append(randNum)


    rand.sort()
    return rand

if __name__ == "__main__" :

    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    if len(sys.argv) != 5:
        logging.error("Argument error")
        logging.error("  Allowed argument :: (Range of rand number) (Number of choices) (Number of attempts)")
        logging.error("                          (1_46) (6) (10) ")
        exit()

    min = int(sys.argv[1].split("_")[0])
    max = int(sys.argv[1].split("_")[1])

    choice = int(sys.argv[2])
    attempts = int(sys.argv[3])

    lotto = list(map(int, sys.argv[4].split("_")))
    print("lotto :: %s " % lotto)

    for i in range(0, attempts):
        rand = getRandNumbers(min, max, choice)

        match = 0
        for gen in rand:
            if (lotto.__contains__(gen)):
                match += 1

        if match > 5 :
            print("%s attempt :: %s  - %s 개" % (i, rand, match))

