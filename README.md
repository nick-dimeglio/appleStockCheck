# appleStockCheck

### Quick script I made to check when certain apple products come in stock for same-day pickup.

## Why would I ever use this?
Great question! Honestly, I thought something like this would be stupid too, but when I went into an Apple Store looking for a MacBook for college that I knew was out of stock, an employee gave me a heads up that stores do not know what stock they are getting until they receive it. He also went on to explain that this means that whenever they get a shipment in, they update it on the website and just have the product in stock until someone grabs it. I realized that I wanted to be that someone, and so this script was born. Instead of patiently waiting the 2-3 months until the product arrives on my order, I figured I'd see if I can grab one sooner. If you are in the same boat, give it a shot and good luck!

## How to use:

### Get your desired SKU
- First off, go to apple's website and look for the product you want.

- Next, right click the page and hit "View page source"

- Press CTRL + F or whatever your "find" keybinds are on your respective OS and search for 'SKU' (without quotations).

- Whatever is to the right of "sku" is your desired SKU. However, please remove the /A at the end of the SKU as that is not extraneous with respect to the SKU. (For instance, the MacBook Pro 14" in Space Gray that I made this script to try and get has a SKU of MKGP3LL.)

## Run the script
- I'd recommend running this from a dedicated terminal window as it relies on catching your attention with an obnoxiously long and loud string of characters once it finds something.
- Eventually, I'd like to add some external notification. I'll likely get around to this in a bit.

## Enter requested information
- Enter the SKU and ZIP-code as directed, and the script will begin running indefinitely. It will check the stores around your zipcode for a same-day pickup opportunity every 15 seconds.

## Exit whenever ready
- To exit, just use CTRL + C or whatever your console exit/interrupt keybind is. Or just close the window. They both have the same magical effect.
