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

#report account specific summed by wordlist
perfin report fifth-third 10/01/2015 11/30/2015 -w electronic,paypal -f greg.csv

#report all summed by wordlist 
perfin report all 10/01/2015 11/30/2015 -w paypal,starbucks,electronic -f greg.csv

#filter by amount
perfin get fifth-third 10/01/2015 11/15/2015 -$ 100,5000 -f x.csv

#most used

perfin get fifth-third 11/01/2015 11/10/2015 -f win.csv
perfin get all -f win.csv
perfin get all 08/15/2015 10/31/2015 -f win.csv

perfin report all 08/01/2015 09/30/2015 -w paypal,electronic -f win.csv

perfin report all 12/01/2015 12/30/2015 -w lmcu,paypal,chase,musical,mobile,electronic,ohio,withdrawal,alert,deposit,navient -f win.csv


#----------------------------------------------
# reports by key
#----------------------------------------------

perfin report fifth-third 12/01/2015 12/30/2015 -w paypal,electronic -f fifth-third.csv

perfin report chase-united 12/01/2015 12/30/2015 -w paypal,chipotle,wrnr,fitness,phoenix,wholefds,starbucks,cvs/pharmacy,utilitie,cinemas,cinemark,yoga,oil,la,theatre,fc34,payment -f chase-united.csv




