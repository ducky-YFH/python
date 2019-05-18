import requests
import re
import os
from bs4 import BeautifulSoup
import traceback
import threading
import time

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3766.2 Safari/537.36"}

url = "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1=CN&FIELD1=ASCO&co1=AND&TERM2=&FIELD2=&d=PTXT"


#取得所有url
def GetAllUrl(url,header):
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("table")[1]
    # print(table)
    pat = "/netacgi/nph-Parser"
    aTagLs = table.find_all(href=re.compile(pat))
    pat2 = 'href="(.*?)">'
    ls = []
    for aTag in aTagLs:
        aTag = str(aTag)
        link = "http://patft.uspto.gov" + re.compile(pat2).findall(aTag)[0].replace("amp;", "")
        ls.append(link)

    # 去掉重复的a链接
    last_ls = []
    for a in ls:
        if a not in last_ls:
            last_ls.append(a)
    return last_ls


'''
#取得所要的数据
invertor 
applicant 
'''

def GetData(urlLs):
    for url in urlLs:
        th = threading.Thread(target=threadingGo, args=(url,))
        th.start()

def threadingGo(url):
    try:
        url = "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=39&f=G&l=50&co1=AND&d=PTXT&s1=CN.ASCO.&OS=ACN/CN&RS=ACN/CN"
        dict = {"Inventors": [], "Applicant": [], "Assignee": [], "FamilyId": [], "ApplNo": [], "PublicationDate": []}
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, 'html.parser')
        # 找到主要的table
        mainTable = soup.find_all("table")[3]

        # -----发明者(Inventors)-----
        inventor = str(mainTable.find_all("tr")[0]) \
            .replace(
            '<tr> <th align="left" scope="row" valign="top" width="10%">Inventors:</th> <td align="left" width="90%">',
            "") \
            .replace('<b>', "").replace("</b>", "").replace("</td> </tr>", "").replace("\n", "")
        # print(inventor)
        # -----申请人(Applicant)-----
        '''
        applicant = str(mainTable.find_all("tr")[1].find_all("table")[0].find_all("tr")[1])\
                    .replace("\n","").replace("<tr>","").replace("<br/>","").replace("<td>","").replace("</td>","").replace("</tr>","") \
                    .replace("<b>", "").replace("</b>", "").replace('<td align="center">',"")
        '''
        applicantName = ""
        applicantCity = ""
        applicantState = ""
        applicantCountry = ""
        applicantType = ""
        # -----代理人(Assignee)-----
        AssigneeName = ""
        AssigneeCity = ""
        AssigneeState = ""
        AssigneeCountry = ""
        # string=re.compile("sisters")

        # -----PatentFamilyID(有些网页可能没有)-----
        FamilyID = ""
        # -----IssueDate------
        IssueDate = ""
        # -----Title------
        Title = ""
        # -----Abstract-----
        
    except Exception as e:
        print('traceback.print_exc():', traceback.print_exc())


def main():
    # start_time = time.time()
    # urlLs = GetAllUrl(url, headers)
    # GetData(urlLs)
    # end_time = time.time()
    # total_time = end_time - start_time
    # print("所有任务结束，总耗时为：{}".format(total_time))
    threadingGo(url)


if __name__ == "__main__":
    main()