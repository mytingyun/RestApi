import sys,time
import requests
import json



class Process_method:
    def __init__(self,host,org,app,headers):
        self.host = host
        self.org = org
        self.app = app
        self.headers = headers


    def process_get(self,url):
        try:
            allurl = "%s/%s/%s/%s" % (self.host,self.org,self.app,url)
            print('url:',allurl)
            self.r = requests.get(allurl, headers=self.headers)
            if self.r.status_code == 200:
                data = self.r.json()
                if data:
                    result = json.dumps(data, sort_keys=True, indent=2)
                    return self.r.status_code,result
                else:
                    return self.r.status_code,data
            else:
                status_code = self.r.status_code
                error_rel = json.dumps(self.r.json(), sort_keys=True, indent=2)
                return status_code,error_rel
        except (KeyError, requests.exceptions.ConnectionError) as err:
            return False,err

    def process_post(self,url,body):
        try:
            self.r = requests.post("%s/%s/%s/%s" % (self.host, self.org, self.app,url),
                                   data=json.dumps(body),
                                   headers=self.headers)
            if self.r.status_code == 200:
                data1 = self.r.json()
                if data1:
                    result = json.dumps(data1, sort_keys=True, indent=2)
                    return True,result
                else:
                    err_res = json.dumps(data1, sort_keys=True, indent=2)
                    return False,err_res
            else:
                err_res = json.dumps(self.r.json(), sort_keys=True, indent=2)
                return self.r.status_code,err_res
        except requests.exceptions.ConnectionError as err:
            return False,err

    def process_del(self,url):
        try:
            self.r = requests.delete("%s/%s/%s/%s" % (self.host, self.org, self.app, url), headers=self.headers)
            if self.r.status_code == 200:
                data1 = self.r.json()
                result = json.dumps(data1, sort_keys=True, indent=2)
                return self.r.status_code,result
            else:
                status_code = self.r.status_code
                err_res = json.dumps(self.r.json(), sort_keys=True, indent=2)
                return status_code,err_res
        except requests.exceptions.ConnectionError as err:
            return False,err


    def process_put(self,url,body):
        try:
            self.r = requests.put("%s/%s/%s/%s" % (self.host, self.org, self.app,url),
                                  data=json.dumps(body),
                                  headers=self.headers)
            if self.r.status_code == 200:
                data = self.r.json()
                result = json.dumps(data, sort_keys=True, indent=2)
                return self.r.status_code,result
            else:
                status_code = self.r.status_code
                err_res = json.dumps(self.r.json(), sort_keys=True, indent=2)
                return status_code,err_res
        except  requests.exceptions.ConnectionError as err:
            return False,err