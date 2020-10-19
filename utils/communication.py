from codecs import encode, decode
import dill
import zlib
import requests

from Character import Dummy as Character


def share(character:"Character"):
    print(f"Trying to share your character {character}...\n")
    if(not character._last_code is None):
        print(NotImplementedError())

    response = requests.post("https://pastebin.com/api/api_post.php",data={
        "api_dev_key":'779286caf706c5e329efd97a78af4bd7',
        "api_option":"paste",
        "api_paste_code":encode(zlib.compress(dill.dumps(character.share())), "base_64").decode(),
        "api_paste_private":'1',
        "api_paste_name":f"{character.level}_{character.attributes.description}",
        "api_paste_expire_date":"1H"
    })

    print("\nDONE\n")

    if(response.status_code != 200):
        print("There has been an error when uploading the character. Please notify the developer")
        print(response.text)
        return  

    code = response.text[-response.text[::-1].index('/'):]


    character._last_code = code

    print(f"Share your character code with your friends\nCODE: {code}")

def list_online():
    response = requests.post("https://pastebin.com/api/api_post.php",data={
        "api_dev_key":'779286caf706c5e329efd97a78af4bd7',
        "api_option":"list"
    })

    print(response.text)

def get_character(code:str):
    response = requests.get("https://pastebin.com/raw/"+code)

    if(response.status_code != 200):
        print("There has been an error when downloading the character. Please notify the developer")
        print(response.text)
        raise Exception()

    return Character(**dill.loads(zlib.decompress(decode(response.text.encode(), "base_64"))))
