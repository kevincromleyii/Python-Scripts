# Importing library
import qrcode
 
# Data to be encoded
data = 'https://didi-food.onelink.me/ssCr/redeemCode?code=FOOD-N9HMN9&activityType=1&locale=en-US'
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('didi.png')