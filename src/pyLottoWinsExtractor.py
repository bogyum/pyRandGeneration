
import logging, sys
import pyUtilsClass

utils = pyUtilsClass.Utils()

if __name__=="__main__":

    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    if len(sys.argv) < 2:
        logging.error("Argument error")
        logging.error("    Allowed argument :: [Lotto wins origin file]")
        exit()


    lottoWins = []
    with open(utils.getLocalPath() + "/../resource/" + sys.argv[1], 'r') as wins:

        while(True):
            line = wins.readline()
            if not line: break

            line = line.strip()
            numbers = " ".join(line.split()).split(" ")
            if len(numbers) > 10:
                lottoWins.append(numbers[-7:])
        wins.close()

    with open(utils.getLocalPath() + "/../resource/" + sys.argv[1].replace(".txt", ".wins"), "w") as result:

        for lottoWin in lottoWins:
            for win in lottoWin:
                result.write("%s " % win)
            result.write("\n")
        result.close()







