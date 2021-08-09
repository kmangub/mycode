#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )
        
        while got_charToLookup:
            if int(got_charToLookup) in  range(1,1001):
                break
            else:
                print("please provide a valid input")
                got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)
        
        # Return Houses affiliated with the character and the list of books they appear in
        houses_arr_urls=got_dj["allegiances"]

        if len(houses_arr_urls) == 0:
            print("This character is not in a house")
        else:
            for house in houses_arr_urls:
                house_resp = requests.get(house).json()
                house_name = house_resp["name"]
                print(f"This character belongs in {house_name}")

         # Return Houses affiliated with the character and the list of books they appear in
        books_arr_urls=got_dj["books"]

        if len(books_arr_urls) == 0:
            print("This character is not in a house")
        else:
            print(f"These are the list of books this character apears in:")
            for book in books_arr_urls:
                book_resp = requests.get(book).json()
                book_name = book_resp["name"]
                print(book_name)
                
                
if __name__ == "__main__":
        main()

