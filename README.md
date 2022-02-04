# HAMMER TIME
Script to connect 3commas bots to hammertime telegram signals

# Disclaimer
**This script is meant to be used for educational purposes only. Use with real funds at your own risk**

# These signals cost money for me to host! If you are enjoying them, please consider supporting me to help keep them up and running
https://www.patreon.com/HebrewHammer

https://www.buymeacoffee.com/H3brewHammer

# Setup Instructions
1. Join the [telegram channel](https://t.me/+w8EBb3Y1Nbs4OTc5)
2. Create your [telegram keys](https://my.telegram.org/apps) and insert them into the `api_id` and `api_hash` variables in the script
3. Create [3commas keys](https://3commas.io/api_access_tokens) with **write** access and insert them into the `commas_key` and `commas_secret` variables in the script
4. Insert the **ID** of the 3commas bot you want to run the signals on into the array of the respsective dictionary in the script. Example:
```
long_bot_ids = {
    'BINANCEUS':
        [1234567, 7654321],
    'BINANCE':
        [],
    'KUCOIN':
        [9876543]
}
```
5. Run the script! When running for the first time, telegram will prompt you for your username/phonenumber (use country code, i.e '+15551234567) and you will have to insert the code it messages you.

# Hammer's current settings:
https://3commas.io/bots/7640932/shared_show?secret=2ce9ab446a
