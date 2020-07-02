'''
#    RAND NUMBER GENERATION
#      - 파라미터로 주어진 값의 범위에서 랜덤 값 생성
'''

import logging, sys, numpy
import pyUtilsClass
from tqdm import tqdm

utils = pyUtilsClass.Utils()

def getMatchedCount(comp, compIndex, wins):
    count = 0
    for index in range(0, len(wins)):
        if index == compIndex: continue
        for num in comp:
            if str(num) in wins[index]:
                count += 1
    return count

if __name__ == "__main__" :

    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    if len(sys.argv) != 3:
        logging.error("Argument error")
        logging.error("  Allowed argument :: (Lotto Wins Count Json) (Number of attempts)")
        exit()

    attempts = int(sys.argv[2])
    winsCount = utils.readJsonFile(utils.getLocalPath() + "/../resource/" + sys.argv[1])

    # 각 번호별 출현 확률
    probSum = 0.0
    prob = [0.0] * 45
    for i in range(0, 45):
        prob[i] = winsCount["winsCount"][i] / winsCount["totalCount"]
        probSum += prob[i]

    # 각 회차별 당첨번호 읽어오기
    wins = []
    with open(utils.getLocalPath() + "/../resource/lotto.wins", "r") as winList:
        while(True):
            line = winList.readline().strip()
            if not line: break
            if '#' in line: continue
            wins.append(line.split(" ")[:6])

    avgCount = 0.0
    for winIndex in range(0, len(wins)):
        avgCount += getMatchedCount(wins[winIndex], winIndex, wins) / (len(wins)-1)
    totalAvgCount = avgCount / len(wins)

    # 랜덤 초이스
    minIndex = 0
    minAvg = 100
    minRand = []
    for i in tqdm(range(0, attempts)):

        rand = numpy.random.choice(range(1,46), 6, replace=False, p=prob)
        matchedAvg = getMatchedCount(rand, len(wins)+1, wins) / len(wins)

        diff = abs(totalAvgCount - matchedAvg)

        if minAvg > diff:
            minAvg = diff
            minRand = rand
            minIndex = i

    print("\nExpected lotto wins[%s] :: %s, %s" % (minIndex, sorted(minRand), minAvg))
