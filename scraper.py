from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
# import re

req = Request("https://www.mcmaster.com/mv1736685562/WebParts/Order/ProductOrderInfo.aspx?partNumber=91251A777&clientNavigationEvents=[{%22type%22:%22ORDERINGMASTERPARTNUMBER%22,%22selectionType%22:%22SELECTION%22,%22values%22:{%22entities%22:%2291251A777%22,%22preselectedComponentPartNumber%22:%22%22}}]" , headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.360'})

webpage = urlopen(req).read()

content = BeautifulSoup(webpage, "html.parser")

# part_number:str = str(content.find("H1"))

# print(content.prettify)

#BeautifulSoup(requests.get("https://www.mcmaster.com/98296A877/").text, "html.parser").contents



# curl 'https://www.mcmaster.com/mv1736685562/WebParts/Order/ProductOrderInfo.aspx?partNumber=91251A777&clientNavigationEvents=\[\{%22type%22:%22ORDERINGMASTERPARTNUMBER%22,%22selectionType%22:%22SELECTION%22,%22values%22:\{%22entities%22:%2291251A777%22,%22preselectedComponentPartNumber%22:%22%22\}\}\]' \
#   -H 'accept: */*' \
#   -H 'accept-language: en-US,en;q=0.9' \
#   -H 'cookie: bid=181507263863; clntextrep=3683196781011957; vstrextrep=85663328393962; sesnextrep=90937341633939; intercom-id-c67mkhee=a5d974a4-4329-46ea-84dc-57a5ca206196; intercom-device-id-c67mkhee=540e89ed-0cdb-469f-9cc8-562b2b4787ec; settings=CD1; intercom-session-c67mkhee=; trkrvisit=ffe00eceb5f746a9afced2ebb6aeb138; volver=mv1736685562; stbver=mvD; viewporthgt=1271; cat=5_1736891748_4e4483e20eda9dda261a75a8e673bba66Z1IJRJO; cntnrwdth=790' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.mcmaster.com/91251A777/' \
#   -H 'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
#   -H 'x-mcm-features: 6dfee20d08b22d52a80698310ccb9821:546,61,391,390,0,11,8,2,12,396,234,5,534,54,55,45,519,555,78,99,91,202,160,50,51,354,355,352,334,520,154,350,509,40,258,239,599,183,600,386,95,613,307,638,368,43,49,370,251,286,84,158,289,277,278,279,281,605,403,282,283,284,588,237,537,617,626,538,203,596,58,523,528,62,618,409,408,407,415,181,180,179,393,625,433,568,566,567,119,616,615,35,372,102,606,38,200,623,457,619,365,117,440,52,441' \
#   -H 'x-mcm-ps-id: 412951030' \
#   -H 'x-mcm-t-id: 414947ccfda0452f9e88f1b2db36bffe' \
#   -H 'x-requested-with: XMLHttpRequest'