import requests
import time

# function for interacting with the apple request.


def check_if_in_stock(SKU, zipcode):
    # in case the user doesn't use all upper case characters. Its needed for the request to work.
    SKU = SKU.upper()
    # url for the apple request
    url = f'https://www.apple.com/us-edu/shop/fulfillment-messages?searchNearby=true&parts.0={SKU}/A&location={zipcode}'
    response = requests.get(url)
    # formatting response into usable json
    json = response.json()
    # check if response was valid
    if response.status_code == 200:
        # quick check in case user mistypes the SKU/ZIP to retype it in case error is thrown.
        # there may be a better more accurate way to do this as the error message is not always the same, but generally an error here is a bad SKU/ZIP.
        if 'errorMessage' in json['body']['content']['pickupMessage']:
            print(
                'Invalid SKU or zip-code used. Please try again with a valid SKU or zip-code.')
            exit()
        # define the json pathway to the stores section
        stores = json['body']['content']['pickupMessage']['stores']
        # set a boolean for if the item is in stock. This makes it easy to print one message at the end outside of the for loop if no stores have it in stock.
        in_stock = False
        # go through each store and check the availability for current-day pick-up of the SKU at each store
        for store in stores:
            # for whatever reason, Apple uses /A at the end of the SKU parameter only within the JSON here, so I just tacked that on.
            if store['partsAvailability'][f'{SKU}/A']['pickupDisplay'] == 'available':
                # Print some obnoxiously long string to get my attention.
                print(
                    f'!!!!!!!!!!!!!!!!!!! BUY NOW AT: {store["storeName"]} !!!!!!!!!!!!!!!!!!!')
                in_stock = True
        # if it is not currently available for pick up at any store, send the OOS message.
        if in_stock == False:
            print('Out of stock at all stores.')
    # if the response was not valid, print the error message.
    else:
        print('error with apple request. please try again.')

# this function just loops the check_if_in_stock function in 15 second delays until the user quits w/ 'ctrl + c'.


def loop_check(SKU, zipcode):
    while True:
        check_if_in_stock(SKU, zipcode)
        time.sleep(15)

# main function, just asks for the SKU and zipcode and calls the loop_check function which will in turn loop the check_if_in_stock function.


def main():
    SKU = input('Enter SKU: ')
    zipcode = input('Enter zipcode: ')
    loop_check(SKU, zipcode)


# call the main function to begin.
main()
