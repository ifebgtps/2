import requests, threading, datetime, sys, os, time

def main():
	global auth, maxerr, api, pos, dely
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f"\t   Simple Python requests ")
	print(f"\t   SC Made by iFeb ")
	print("="*64)
	maxerr = 0 # Avoid Ban when User AFK.
	api = str(input("url:"))
	ext = str(input("Ext: "))
	raw = str(input("Raw Data: "))
	auth = str(input("Auth Key: "))
	dely = float(input("\nDelay "))
	thr = int(input("\nThreads: "))
	print("="*64)
	for _ in range(thr):
	        threading.Thread(target=s).start()

def s():
        global maxerr
        while True:
                dt = datetime.datetime.now()
                try:
                	    raw = raw
                        headers = {
                            'authorization': auth,
                            'use_response_compression': 'true',
                            'Accept-Encoding': 'gzip',
                            'Host': api,
                            'Connection': None,
                            'User-Agent': None,
                        }
                        data
                        response = requests.get(f'http://{api}/{ext}', headers=headers, data=raw)
                        if response.status_code == 200:
                                sys.stdout.write(f"\r Sucess Send")
                                sys.stdout.flush()
                                break
                                sys.exit(0)
                         else response.status_code=500:
                         	   sys.stdout.write(f"\r Error")
                                sys.stdout.flush()
                                break
                                sys.exit(0)
                        if dely > 0: time.sleep(dely)
                except Exception as e:
                        pass

if __name__ == "__main__":
	main()
