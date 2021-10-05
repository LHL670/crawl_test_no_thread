import time
import threading
import queue
from getIDList import getIDList
import manageFirebase
import getPersonalPage
import getIDList
# Worker 類別，負責處理資料


def CGUCrawlWorker_noThread(label):
    IDList = getIDList.getIDList(label)
    for id in IDList:
        personalData = getPersonalPage.getPersonalPage(id)
        manageFirebase.updatePersonalData(personalData)

    print("Done.")


# 累積到一定得筆數upload firebase
if __name__ == '__main__':
    print('start')
    label = 'causal_inference'
    CGUCrawlWorker_noThread(label)
