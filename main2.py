import requests
import json
import sys

class Tiki_API:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0',
            'TE': 'Trailers'
        }
        self.string_id = "tikivn://products/"
        self.detail_url = "https://tiki.vn/api/v2/products/{}?platform=web&spid={}&include=tag,images,gallery,promotions,badges,stock_item,variants,product_links,discount_tag,ranks,breadcrumbs,top_features,cta_desktop"
        self.category_url = "https://tiki.vn/api/v2/products?category={}&page={}&limit={}"

    def get_id(self, url):
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data=payload)
        html = response.text

        poss = html.find(self.string_id)
        for i in range(poss, poss + 200):
            if (html[i] == '"'):
                pose = i
                break

        pdid = html[poss + len(self.string_id):pose]
        if (response.status_code == 200):
            return {'status': True, 'product_id': pdid}
        else:
            return {'status': False}

    def get_product(self, id_product, sub_id=-1):
        if (sub_id == -1):
            sub_id = id_product
        url = self.detail_url.format(id_product, sub_id)
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data=payload)

        if (response.status_code == 200):
            data = json.loads(response.text)
            return {'status': True, 'data': data}
        else:
            return {'status': False}

    def get_category(self, id_c, page=1, limit=300):

        url = self.category_url.format(id_c, page, limit)

        payload = {}
        response = requests.request("GET", url, headers=self.headers, data=payload)

        if (response.status_code == 200):
            data = json.loads(response.text)
            if (len(data['data']) == 0):
                return {'status': False}
            return {'status': True, 'data': data['data'], 'paging': data['paging']}
        else:
            return {'status': False}

tiki = Tiki_API()
i=i=int(sys.argv[1]) +11000000
data=[]
while(i<(int(sys.argv[2])+11000000)):
    product_details = tiki.get_product(str(i))
    data.append(product_details)
    i+=1
