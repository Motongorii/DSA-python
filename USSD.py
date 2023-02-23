
#Transaction Entry
def transactionEntry():
    transcode = input("0:Nyakua Bonus\n"
                      "1:Data Deals\n"
                      "2:Daily Bundles\n"
                      "3;Weekly Bundles\n"
                      "4:GO MONTHLY\n"
                      "5:No ExpiryV\n"
                      "6:Video Bundles\n"
                      "7:Okoa Data\n"
                      "8:Lipa Mdogo\n"
                      "9:Data Plus NEW"
                      "10:Hot Minutes\n"
                      "98:MORE\n"
                      "SELECT TRANSACTION")
    if transcode == "0":
        print("1:Buy Nyakua bundles\n"
              "2:Check my target\n"
              "3:Check my Daily usage\n"
              "4:Opt out\n"
              "5:How it works\n"
              "0:Back 00:Home")
    elif transcode == "1":
        print("Mega bundles")
    elif transcode == "2":
        print("500mbs @ ksh1000\n"
              "200mbs @ ksh 400")
    elif transcode == "3":
        print("25Gb @ 1500\n"
              "15GB @ 2500")
    elif transcode == "4":
        print()
    elif transcode == "5":
        print()
    elif transcode == "6":
        print()
    elif transcode == "7":
        print()
    elif transcode == "8":
        print()
    elif transcode == "9":
        print()
    elif transcode == "10":
        print()
    elif transcode == "98":
        print()
    else:
        print("Invalid entry\n"
              "Try again")
        transactionEntry()
# function to crosscheck USSD code
def confirmUSSD():
    ussd = input("Enter USSD code")
    if ussd == "*544#":
        transactionEntry()
    else:
      print("Invalid USSD code\n"
            "Try again")
    confirmUSSD()

#calling the function
confirmUSSD()