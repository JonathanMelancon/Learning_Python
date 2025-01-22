import requests
from bs4 import BeautifulSoup


partnumber = "92949A313"

# From chrome inspector (f12) on element https://www.mcmaster.com/mv1736887241/WebParts/Order/ProductOrderInfo.aspx --> copy curl (bash) --> https://curlconverter.com/ to python

cookies = {
    'bid': '181507263863',
    'clntextrep': '3683196781011957',
    'vstrextrep': '85663328393962',
    'sesnextrep': '90937341633939',
    'intercom-id-c67mkhee': 'a5d974a4-4329-46ea-84dc-57a5ca206196',
    'intercom-device-id-c67mkhee': '540e89ed-0cdb-469f-9cc8-562b2b4787ec',
    'settings': 'CD1',
    'intercom-session-c67mkhee': '',
    'trkrvisit': 'd6721b03666641e483ab6c497510060e',
    'viewporthgt': '911',
    'volver': 'mv1736887241',
    'stbver': 'mvC',
    'cat': '5_1736976827_2c9c158dc6523c7e92bfd8497429c11eXIR3QX6K',
    'cntnrwdth': '628',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'bid=181507263863; clntextrep=3683196781011957; vstrextrep=85663328393962; sesnextrep=90937341633939; intercom-id-c67mkhee=a5d974a4-4329-46ea-84dc-57a5ca206196; intercom-device-id-c67mkhee=540e89ed-0cdb-469f-9cc8-562b2b4787ec; settings=CD1; intercom-session-c67mkhee=; trkrvisit=d6721b03666641e483ab6c497510060e; viewporthgt=911; volver=mv1736887241; stbver=mvC; cat=5_1736976827_2c9c158dc6523c7e92bfd8497429c11eXIR3QX6K; cntnrwdth=628',
    'priority': 'u=1, i',
    'referer': 'https://www.mcmaster.com/92949A313/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-mcm-features': '6dfee20d08b22d52a80698310ccb9821:546,61,391,390,0,11,8,2,12,396,234,5,534,54,55,45,519,555,78,99,91,202,160,50,51,354,355,352,334,520,154,350,509,40,258,239,599,183,600,386,95,613,307,638,368,43,49,370,251,286,84,158,289,277,278,279,281,605,403,282,283,284,588,237,537,617,626,538,203,596,58,523,528,62,618,409,408,407,415,181,180,179,393,625,433,568,566,567,119,616,615,35,372,102,606,38,200,623,457,619,365,117,440,52,441',
    'x-mcm-ps-id': '220585640',
    'x-mcm-t-id': '2274d3fef80c4ff4b0ce720e3892dd70',
    'x-requested-with': 'XMLHttpRequest',
}

requests.get(
    'https://www.mcmaster.com/mv1736887241/tokenauthorization.aspx'
    'https://www.mcmaster.com/mv1736887241/Vldt.aspx'
    
)


requests.post (
    'https://www.mcmaster.com/mv1736887241/tokenauthorization.aspx, True',
    'https://www.mcmaster.com/mv1736887241/Vldt.aspx, True'
   
)

response = requests.get(
    
    'https://www.mcmaster.com/init/ServiceWorkerJS.aspx'
    'https://www.mcmaster.com/mv1736887241/WebParts/Order/ProductOrderInfo.aspx?partNumber=92949A313&clientNavigationEvents=[{%22type%22:%22ORDERINGMASTERPARTNUMBER%22,%22selectionType%22:%22SELECTION%22,%22values%22:{%22entities%22:%2292949A313%22,%22preselectedComponentPartNumber%22:%22%22}}]',
    cookies=cookies,
    headers=headers,
)

print(response.text)

"""
xmlHttpForToken.open("POST", "/mv1736887241/tokenauthorization.aspx", true);
                    xmlHttpForToken.send();

xmlHttp.open("GET", "/mv1736887241/Vldt.aspx", true);
        xmlHttp.send();

if (authToken === "true") {
        SesnMgr.SetStVal(SesnMgr.StValDefs.AuthTokenEnabled.KyTxt(), "true");
                
"""