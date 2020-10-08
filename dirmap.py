#ToBeatElit3
from requests import get
from sys import argv

def bruteforce(url, wordlist):
	with open(wordlist, "r+") as my_file:
		for line in my_file:
			stripped_line = line.strip()
			my_url = f"{url}/{stripped_line}"
	
			http_request = get(my_url)
			status = http_request.status_code

def main():
	try: bruteforce(argv[1], argv[2])
	except Exception as ex: print(f"Usage : python {argv[0]} [url] [wordlist]\n{ex}")

if __name__ == "__main__": main()
