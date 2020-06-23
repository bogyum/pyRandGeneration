'''
#    RAND NUMBER GENERATION
#      - 파라미터로 주어진 값의 범위에서 랜덤 값 생성
'''

import logging, sys, numpy
import pyUtilsClass
from tqdm import tqdm

utils = pyUtilsClass.Utils()

if __name__ == "__main__" :

    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    if len(sys.argv) != 3:
        logging.error("Argument error")
        logging.error("  Allowed argument :: (Lotto Wins Count Json) (Number of attempts)")
        exit()

    attempts = int(sys.argv[2])
    winsCount = utils.readJsonFile(utils.getLocalPath() + "/../resource/" + sys.argv[1])

    probSum = 0.0
    prob = [0.0] * 45
    for i in range(0, 45):
        prob[i] = winsCount["winsCount"][i] / winsCount["totalCount"] * 100
        probSum += prob[i]

    for i in tqdm(range(0, attempts)):
        rand = numpy.random.choice(range(0,45), 6, replace=False, p=prob)
        sort_rand = sorted(rand)
        print("Expected lotto wins[%s] :: %s" % (i, sort_rand))
