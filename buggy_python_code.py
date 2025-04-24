import sys 
import os
import yaml
import urllib.request
import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person(object):
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    if urllib_version != "3":
        raise ValueError("zle")
    
    # Whitelist of allowed domains
    allowed_domains = ["example.com", "google.com"]
    
    # Validate and parse the URL
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        raise ValueError("Invalid URL format")
    
    # Check if the domain is in the whitelist
    domain = parsed_url.netloc.split(':')[0]  # Exclude port if present
    if domain not in allowed_domains:
        raise ValueError("Domain not allowed")
    
    try: 
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except Exception as e:
        print("Exception", e)


def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data
    
def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")


if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice  = input("Select vulnerability: ")
    if choice == "1": 
        new_person = Person("Vickie")  
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)

