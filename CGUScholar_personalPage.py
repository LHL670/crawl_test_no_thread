import time
import threading
import queue
from getIDList import getIDList
import manageFirebase
import getPersonalPage
import getIDList
# Worker 類別，負責處理資料


def CGUCrawlWorker_noThread(label):
    workCount = 0
    IDList = getIDList.getIDList(label)
    while workCount < 5:
        personalData = getPersonalPage.getPersonalPage(IDList[workCount])
        workCount = workCount + 1
        manageFirebase.updatePersonalData(personalData)

    print("Done.")


# 累積到一定得筆數upload firebase
if __name__ == '__main__':
    print('start')
    label = 'causal_inference'
    CGUCrawlWorker_noThread(label)
