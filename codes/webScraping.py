from bs4 import BeautifulSoup
import requests, openpyxl
import json

# source = requests.get("https://es.aliexpress.com/category/204006047/cellphones.html?category_redirect=1&spm=a2g0o.home.103.2.65d870e5559DNX")
# source = requests.get("https://www.amazon.com/s?k=graphics+card")
# source = requests.get("https://www.gamestop.com/video-games/xbox-one")

# print(doc);
excel = openpyxl.Workbook()
# pages = {}
costantColums = ["Name Product", "Price", "Page"]
def specificPages(OtherUrl, pageNamed):
    # source = requests.get("https://aeon.com.sv/shop/category/componentes-tarjetas-de-video-431", verify=False)
    source = requests.get("https://aeon.com.sv" + OtherUrl, verify=False)
    doc = BeautifulSoup(source.text, "html.parser")
    try:
        products = doc.find_all("div", class_="o_wsale_product_information_text")
        # .find("div", class_="row").find("div", class_="as-pro-col")
        # print(products)
        excel.create_sheet(pageNamed)
        excel[pageNamed].append(costantColums)
        for product in products:
            name = product.h6.a.string
            url = product.h6.a['href']
            price = product.find("div", class_="product_price").span.span.string
            excel[pageNamed].append([name,price, ("https://aeon.com.sv" + url)])
            # break
    except Exception as a:
        print(a)

def getAllPages():
    baseUrl = "https://aeon.com.sv"
    source = requests.get(baseUrl, verify=False)
    doc = BeautifulSoup(source.text, "html.parser")
    # print(doc)
    try:
        selects = doc.find_all("div", class_="o_mega_menu")[1].contents
        # .find("div", class_="row").find("div", class_="as-pro-col")
        # print(products)
        productosurl = []
        # print(selects)
        for select in selects:
            # print(select)
            # urlProducts = select.find_all("a")
            if(select.name == 'section'):
                aTags = select.find_all("a")
                # print(aTags)
                for aTag in aTags:
                    url = aTag['href']
                    nameCategorie = aTag.string
                    print("categoria")
                    specificPages(url, nameCategorie)
                    # print(url);
            # print(select.name)
            # price = product.find("div", class_="product_price").span.span.string
            # print(name + " ------ " + price)
            # break
        excel.save('aeonProducts.xlsx')
    except Exception as a:
        print(a)

# specificPages()
getAllPages()
# print(products)