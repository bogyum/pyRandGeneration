'''
#    RAND NUMBER GENERATION
#      - 파라미터로 주어진 값의 범위에서 랜덤 값 생성
'''

import logging, sys, random
from tqdm import tqdm

gens = {}
nums = {}

def getRandNumbers(min, max, choice):
    rand = []
    randNum = random.randint(min, max)

    for i in range(0, choice):
        while randNum in rand:
            randNum = random.randint(min, max)
        rand.append(randNum)
        nums[randNum] += 1

    rand.sort()
    return rand

if __name__ == "__main__" :

    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    if len(sys.argv) != 5:
        logging.error("Argument error")
        logging.error("  Allowed argument :: (Range of rand number) (Number of choices) (Number of attempts) (Minimum freq for output)")
        logging.error("                          (1_46) (6) (10) (10)")
        exit()

    min = int(sys.argv[1].split("_")[0])
    max = int(sys.argv[1].split("_")[1])

    choice = int(sys.argv[2])
    attempts = int(sys.argv[3])
    minFreq = int(sys.argv[4])

    for i in range(0, max+1):
        nums[i] = 0

    for i in tqdm(range(0, attempts)):
        rand = getRandNumbers(min, max, choice)
        strRand = ' '.join([str(x) for x in rand ])

        if gens.__contains__(strRand) :
            gens[strRand] += 1
        else :
            gens[strRand] = 1

    sort_gens = sorted(gens.items(), key=lambda x: x[1], reverse=True)
    sort_nums = sorted(nums.items(), key=lambda x: x[1], reverse=True)

    for i in sort_gens:
        if i[1] < minFreq: break
        print("Generation key : %s - %s freq" % (i[0], i[1]))

    print(sort_nums)