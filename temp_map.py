
#lat,long=41.403389, 2.174028
lat,long=input().split()
try:
    webbrowser.open(f"https://www.google.com/maps/place/{lat},{long}")
except:
    print('You can visit the URL : ',f"https://www.google.com/maps/place/{lat},{long}")