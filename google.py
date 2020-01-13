#The latitude of Meerut, Uttar Pradesh, India is 28.984644, and the longitude is 77.705956.

lat,long=input('enter the latitude and longitude with space in decimal form').split()
try:
    webbrowser.open(f"https://www.google.com/maps/place/{lat},{long}")
except:
    print('You can visit the URL : ',f"https://www.google.com/maps/place/{lat},{long}")