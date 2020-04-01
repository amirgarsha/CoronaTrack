import requests
import pandas as pd

## get information about countries listed below
Countries = ['iran','italy','spain','germany','france','united-kingdom','switzerland','belgium','us','china']
allCountry=[]
for Country in Countries:
    url = "https://api.covid19api.com/country/%s/status/confirmed" % Country

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

#print(response.text.encode('utf8')) //use this for checking
    jsonRes = response.json()

#us and china are different in getting information. it is needed to get inf in different way
    if Country == 'us' or Country == 'china':
        dateTemp = 0
        caseTemp = 0
        for i in range(0,len(jsonRes)):
#           print(i)
#            print(len(jsonRes))
            dateI = jsonRes[i]['Date'][0:10]
            if dateI == dateTemp:
                Case = int(jsonRes[i]['Cases']) + caseTemp
            else:
                Case = int(jsonRes[i]['Cases'])
#                print(dateTemp,caseTemp,sep=",")  //just for temporary checking
                allCountry.append((Country,dateTemp,caseTemp))
            dateTemp = dateI
            caseTemp = Case

    else:
        dateTemp = 0
        caseTemp = 0
        for i in range(0,len(jsonRes)):
            dateI = jsonRes[i]['Date'][0:10]
            if dateI == dateTemp:
                Case = max(int(jsonRes[i]['Cases']),caseTemp)
            else:
                Case = int(jsonRes[i]['Cases'])
#                print(dateTemp,caseTemp,sep=",") //temporary checking
                allCountry.append((Country, dateTemp, caseTemp))
            dateTemp = dateI
            caseTemp = Case

## split information based on country on different lists
iran = [allCountry[x][1:3] for x in range(0,len(allCountry)) if allCountry[x][0] == 'iran']
spain = [allCountry[x][1:3] for x in range(0,len(allCountry)) if allCountry[x][0] == 'spain']
italy = [allCountry[x][1:3] for x in range(0,len(allCountry)) if allCountry[x][0] == 'italy']
united_kingdom = [allCountry[x][1:3] for x in range(0,len(allCountry)) if allCountry[x][0] == 'united-kingdom']
germany = [allCountry[x][1:3] for x in range(0,len(allCountry)) if allCountry[x][0] == 'germany']
belgium = [allCountry[x][1:3] for x in range(0,len(allCountry)) if allCountry[x][0] == 'belgium']
switzerland = [allCountry[x][1:3] for x in range(0,len(allCountry)) if allCountry[x][0] == 'switzerland']
france = [allCountry[x][1:3] for x in range(0,len(allCountry)) if allCountry[x][0] == 'france']
us = [allCountry[x][1:3] for x in range(0,len(allCountry)) if allCountry[x][0] == 'us']
china = [allCountry[x][1:3] for x in range(0,len(allCountry)) if allCountry[x][0] == 'china']

## make dataframe based on each country
df_iran = pd.DataFrame(iran,columns=['Date','Total'])
df_spain = pd.DataFrame(spain,columns=['Date','Total'])
df_italy = pd.DataFrame(italy,columns=['Date','Total'])
df_uk = pd.DataFrame(united_kingdom,columns=['Date','Total'])
df_germany = pd.DataFrame(germany,columns=['Date','Total'])
df_belgium = pd.DataFrame(belgium,columns=['Date','Total'])
df_switzerland = pd.DataFrame(switzerland,columns=['Date','Total'])
df_france = pd.DataFrame(france,columns=['Date','Total'])
df_us = pd.DataFrame(us,columns=['Date','Total'])
df_china = pd.DataFrame(china,columns=['Date','Total'])
#for x in range(1,len(china)):      //for checking that information is correct
#    print(china[x][0], china[x][1],sep=",")

## save it to excel file
with pd.ExcelWriter('CoronaStat.xlsx') as writer:
    df_iran.to_excel(writer,sheet_name="Iran")
    df_belgium.to_excel(writer,sheet_name="Belgium")
    df_china.to_excel(writer,sheet_name="China")
    df_france.to_excel(writer,sheet_name="France")
    df_germany.to_excel(writer,sheet_name="Germany")
    df_italy.to_excel(writer,sheet_name="Italy")
    df_spain.to_excel(writer,sheet_name="Spain")
    df_switzerland.to_excel(writer,sheet_name="Switzerland")
    df_uk.to_excel(writer,sheet_name="UK")
    df_us.to_excel(writer,sheet_name="USA")