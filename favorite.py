from token import Token
import json
import httplib

class Favorite(Token):

    def add_favorite_file(self, file_path):
       # logf = open("My_error.txt",'a') 
       # logf.write("{0}:\n".format("123" ))

        headers = {"X-Auth-Token" : self.my_token, 
                   "User-Agent" : self.config["device_id"]}
        conn = httplib.HTTPConnection(self.config["url"])
        conn.request("POST","/fileop/v1/favorite/" + file_path,
                     "", headers)
        response = conn.getresponse()

        if response.status == 201:
            self.log.info("({0}) Add favorite file status code is {1}".format(
                response.reason, response.status) )

        if response.status != 201:
                self.log.war("({0}) Remove favorite list status code is {1}"
                .format(response.reason, response.status)) 

    def get_favorite_list(self):
        headers = {"X-Auth-Token" : self.my_token, 
                   "User-Agent" : self.config["device_id"]}
        conn = httplib.HTTPConnection(self.config["url"])
        conn.request("GET","/fileop/v1/favorite",
                     "", headers)
        response = conn.getresponse()
        favorite_list = {}
        bodys = response.read()
        bodys = json.loads(bodys)
        for i in range(len(bodys)):
            favorite_list [bodys[i]["path"] ]= bodys[i]["id"];
        self.favorite_list = favorite_list

        self.log.info("({0}) Get favorite list status code is {1}".format(
            response.reason, response.status))        
    #    print self.favorite_list

    def remove_favorite(self, file_name):
        headers = {"X-Auth-Token" : self.my_token, 
                   "User-Agent" : self.config["device_id"]}
        try:
            favorite_id = self.favorite_list[file_name]     
     #   print favorite_id
            conn = httplib.HTTPConnection(self.config["url"])
            conn.request("DELETE","/fileop/v1/favorite" + "?id=" + favorite_id,
                     "", headers)
            response = conn.getresponse()

            self.log.info("({0}) Remove favorite list status code is {1}"
                .format(response.reason, response.status)) 
            if response.status != 204:
                self.log.war("({0}) Remove favorite list status code is {1}"
                .format(response.reason, response.status)) 
        except Exception as e:   
            self.log.error("{0} Input parameter file_name maybe wrong".format(str(e)))
 

if __name__ == "__main__":
    Test = Favorite()
    Test.get_token()
    Test.add_favorite_file("test2222.jpg")
    Test.get_favorite_list()
    #Test.remove_favorite("test2.jpg")