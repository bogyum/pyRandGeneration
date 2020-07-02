import logging, sys
import pyUtilsClass

utils = pyUtilsClass.Utils()

if __name__=="__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    if len(sys.argv) < 2:
        logging.error("Argument error")
        logging.error("    Allowed argument :: [Lotto wins numbers file]")
        exit()

    totalCount = 0
    lottoWinsCount = [0] * 45

    with open(utils.getLocalPath() + "/../resource/" + sys.argv[1], 'r') as wins:

        while(True):
            line = wins.readline().strip()
            if not line: break
            if line[0] == '#': continue

            win = " ".join(line.split()).split(" ")

            totalCount += 7
            for element in win:
                lottoWinsCount[int(element)-1] += 1

        wins.close()

    with open(utils.getLocalPath() + "/../resource/" + sys.argv[1].replace(".wins", ".json"), 'w') as result:
        result.write('{ "totalCount": %s, "winsCount": %s }' % (totalCount, lottoWinsCount))
        result.close()
