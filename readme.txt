#account names
fifth-third
capital-one-venture
captial-one-sig
chase-united

#upload all csv files in the files folder
perfin upload 

#get all fifth third transactions
perfin get fifth-third

#get all transactions
perfin get all

#filter fifth third
perfin get fifth-third 11/01/2015 11/30/2015

#filter all
perfin get all 11/01/2015 11/30/2015

#to csv
perfin get fifth-third -f file.csv

#to csv filtered
perfin get fifth-third 11/01/2015 11/30/2015 -f file.csv

#posting
requests.post("http://localhost:8001/api/upload-transactions/fifth-third/", data={"data": data,'type' : 'Fifth Third'})

#wordlist filtered
perfin get all -w paypal,starbucks,something -f csv.csv

#wordlist by account
perfin get fifth-third -w paypal,musical -f x.csv

#wordlist by account filtered
perfin get fifth-third 10/01/2015 10/31/2015  -w paypal,starbucks -f x.csv

#wordlist by all filtered
perfin get all 10/01/2015 10/31/2015  -w paypal,starbucks -f x.csv