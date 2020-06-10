'''
#    RAND NUMBER GENERATION
#      - 파라미터로 주어진 값의 범위에서 랜덤 값 생성
'''

import logging, sys, numpy
from tqdm import tqdm

if __name__ == "__main__" :

    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    if len(sys.argv) != 4:
        logging.error("Argument error")
        logging.error("  Allowed argument :: (Number of attempts) (Number of rand iteration) (Number of generation")
        exit()

    attempts = int(sys.argv[1])
    randIteration = int(sys.argv[2])
    genIteration = int(sys.argv[3])

    numbers = range(1, 46)
    lottoCandidate = set()

    for i in range(0, attempts):

        gens = {}
        for j in tqdm(range(0, randIteration)):
            randGeneration = numpy.random.choice(numbers, 6, False)

            for k in randGeneration:
                if gens.__contains__(k):
                    gens[k] += 1
                else:
                    gens[k] = 1

        sort_gens = sorted(gens.items(), key=lambda x: x[1], reverse=True)
        for j in range(0, 6):
            lottoCandidate.add(sort_gens[j][0])

    for i in range(0, genIteration):
        print("Lotto Candidate %s :: %s " % (i, numpy.random.choice(list(lottoCandidate), 6, False)))
