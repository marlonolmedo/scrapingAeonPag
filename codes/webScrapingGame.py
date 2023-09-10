from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.gamestop.com/video-games/xbox-one", verify=False)
doc = BeautifulSoup(source.text, "html.parser")

print(doc);

# try:
#     products = doc.find_all("div", class_="o_wsale_product_information_text")
#     # .find("div", class_="row").find("div", class_="as-pro-col")
#     # print(products)
#     for product in products:
        
#         name = product.h6.a.string
#         price = product.find("div", class_="product_price").span.span.string
#         print(name + " ------ " + price)
#         # break
# except Exception as a:
#     print("cambios" + doc)

# print(products)