from token import Token
import httplib
from file import File
from favorite import Favorite

class Main(File, Favorite):
    pass
    #logf = open("My_error.txt",'r+') 


    
if __name__ == "__main__":
    main =  Main()
    main.get_token();

    #main.add_favorite_file("test22.jpg")
    #main.get_favorite_list()
    #main.remove_favorite("/test22.jpg")
    #main.upload_file("C:\\Users\\kevin.chang\\Desktop\\MyPython\\API\\abc123.jpg", "test22.jpg")
