# BreachDB.py
BreachDB.py: Query the Rapid7 breach database for email addressess and passwords.

## Setup:  
```bash
git clone https://github.com/jgarcia-r7/BreachDB.py
pip3 install -r requirements.txt
./BreachDB.py -h
```
By default, the tool does not come with an API key configured. You can configure it by opening **BreachDB.py** in your favorite text editor and replacing 'PUT-API-KEY-HERE' (you can supply the Rapid7 API key here), otherwise you will have to supply it everytime with `-a`:  
![image](https://user-images.githubusercontent.com/81575551/161134730-a7e4862e-b2f8-48a4-a2e3-f77a897550f6.png)

## Usage:
**BreachDB.py** takes the following arguments:
```txt
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Target domain REQUIRED
  -o OUTPUT, --output OUTPUT
                        Output file name OPTIONAL (Defualt: results.txt)
  -l LIMIT, --limit LIMIT
                        Limit results  OPTIONAL (Default: 1000)
  -a APIKEY, --apikey APIKEY
                        API Key OPTIONAL (Default: R7 default api key.)
```
**BreachDB.py** gets usernames and passwords from the breach database for the domain you specify. It limits results based on what you provide for `-l`, it then writes the results to a file that you specify with `-o` and displays the top 3 most common passwords - useful for password spray attacks.
An example of standard usage:
![image](https://user-images.githubusercontent.com/81575551/161135353-b1b5113a-84f4-4353-8ec5-c254bcfdc3e1.png)

## Output
Output is configured to write in the format of `username:password`:
![image](https://user-images.githubusercontent.com/81575551/161135791-5dfcfce3-acf2-4be9-bd2d-616d4d5da06b.png)
