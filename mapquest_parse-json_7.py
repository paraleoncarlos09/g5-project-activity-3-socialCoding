import sys
import urllib.parse
import requests
from colored import fg                      
from colored import bg


#list of colors
color = fg('dark_olive_green_3a')
color2 = fg('deep_sky_blue_3a')
color1 = fg('white')
color3 = fg('red_3b')
back = bg('dark_olive_green_3a')
back1 = bg('dark_green_sea')
back2 = bg('white')
back3 = bg('light_sky_blue_3a')
color4 = fg('light_sky_blue_3b')


main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Kf4MrxBifKdgiInGG6N7bWMA46ACtFPx"

print()
print(color1 + back2 + '\033[1m' + "                                                                                   " + '\033[0m')
print(color1 + back1 + '\033[1m' + "                                  MAP QUEST                                        " + '\033[0m')
print(color1 + back1 + '\033[1m' + "                                 by: GROUP V                                       " + '\033[0m')
print(color1 + back1 + '\033[1m' + "                       BIBERA  GARCIA  PARALEON  REYES                             " + '\033[0m')
print(color1 + back2 + '\033[1m' + "                                                                                   " + '\033[0m')

while True:
    
    #User input for the location & destination and validation of inputs.
    orig = input(color2 + '\033[1m' + "\nStarting Location: " + '\033[0m')                              #Fix: Should not accept integer or numeric input
    if orig == "quit" or orig == "q":                                                                   #Bold Text: '\033[0m'
        print((color3 + '\033[1m' + "\nProgram Terminated" + '\033[0m') )
        break
    dest = input(color2 + '\033[1m' + "Destination: "  + '\033[0m')
    print()
    if dest == "quit" or dest == "q":
        print((color3 + '\033[1m' + "\nProgram Terminated" + '\033[0m') )
        break
    
    if (orig.isnumeric() or dest.isnumeric())== False:                                                  #Fixed: added condition for numeric input                  
        #Generation and printing of URL
        url = main_api + \
            urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
        print("URL: " + (url)+ "\n")
        
        #Json data request
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        
        #Successful route call
        if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            #Origin information
            print("===================================================================================")
            print()
            print(color3 + '\033[1m' + (orig) + " Information                                                              " + '\033[0m')
            print("Country: " + '\033[1m' + (json_data["route"]["locations"][0]["adminArea1"]) + '\033[0m')                                     #fix error: list indices must be intergers or slices, not str
            print("Province: " + '\033[1m' + (json_data["route"]["locations"][0]["adminArea3"]) + '\033[0m')                                    #fixed: added array
            print("Type: " + '\033[1m' + (json_data["route"]["locations"][0]["geocodeQuality"]) + '\033[0m')                                    #[0] - origin
            print("Geo Quality Code: " + '\033[1m' + (json_data["route"]["locations"][0]["geocodeQualityCode"]) + '\033[0m')
            #Destination information
            
            print()
            print(color3 + '\033[1m' + (dest) + " Information" + '\033[0m')
            print("Country: " + '\033[1m' + (json_data["route"]["locations"][1]["adminArea1"]) + '\033[0m')                                     #fix error: list indices must be intergers or slices, not str
            print("Province: " + '\033[1m' + (json_data["route"]["locations"][1]["adminArea3"]) + '\033[0m')                                    #fixed: added array
            print("Type: " + '\033[1m' + (json_data["route"]["locations"][1]["geocodeQuality"]) + '\033[0m')                                    #[1] - destination
            print("Geo Quality Code: " + '\033[1m' + (json_data["route"]["locations"][1]["geocodeQualityCode"]) + '\033[0m')
            print()
            print("===================================================================================")
            print()
            
            #Printing of the directions from the origin to the destination
            print('\033[1m' + color3 + "Directions from " + (orig) + " to " + (dest) + '\033[0m')
            print()
            #GPS coordinates 
            print('\033[4m' + "GPS Coordinate of Origin" + '\033[0m'"\nLongitude: "  +  '\033[1m' +     
                str(json_data["route"]["boundingBox"]["ul"]["lng"]) + '\033[0m' "\nLatitude: " + '\033[1m' + str(json_data["route"]["boundingBox"]["ul"]["lat"]) + '\033[0m')          #longitude working, add latitude
            
            print('\033[4m' + "\nGPS Coordinate of Destination" + '\033[0m' + "\nLongitude: "  + '\033[1m' +
                str(json_data["route"]["boundingBox"]["lr"]["lng"]) + '\033[0m' + "\nLatitude: " + '\033[1m' + str(json_data["route"]["boundingBox"]["lr"]["lat"]) + '\033[0m')          #latitude added
            #Printing of travel information
            print()
            print("Trip Duration: " + '\033[1m' + color4 + (json_data["route"]["formattedTime"]) + '\033[0m')
            print("Kilometers: " + '\033[1m' + color4 +
                str("{:.2f}".format((json_data["route"]["distance"])*1.61)) + '\033[0m')
            
            print()
            #print("Fuel Used (Ltr): " +                                                            #fuelused not working
            #    str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        
            print("===================================================================================")
            print()
            
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" +
                    str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                
            
            #Other miscellaneous information about travel
            print()
            print("===================================================================================")
            print()
            print('\033[1;3m' + color3 + "Other Miscellaneous Information:\n" + '\033[0m')
            print("Will I encounter any toll road? " + '\033[1m' + color4 + str(json_data["route"]["hasTollRoad"]) + '\033[0m')
            print("Will I encounter any bridge? " + '\033[1m' + color4 + str(json_data["route"]["hasBridge"]) + '\033[0m')
            print("Will I encounter any tunnel? " + '\033[1m' + color4 + str(json_data["route"]["hasTunnel"]) + '\033[0m') 
            print("Will I encounter any highway? " + '\033[1m' + color4 + str(json_data["route"]["hasHighway"]) + '\033[0m')
            
            #print("Is there any access restriction? " , (json_data["route"]["hasAccessRestriction"]))             #added some other miscellaneous information
                                                                                                                   #not working
            
            print("Is there any seasonal closure? " + '\033[1m' + color4 + str(json_data["route"]["hasSeasonalClosure"]) + '\033[0m')
            print("Is there any country cross? " + '\033[1m' + color4 + str(json_data["route"]["hasCountryCross"]) + '\033[0m')
            print()
            print("===================================================================================")
            
            
        #Unsuccessful route call (error codes)                                                                    #done fixing the output
        elif json_status == 402:
            print(color3 + '\033[1m' + "***Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.***" + '\033[0m')
        elif json_status == 611:
            print(color3 +  '\033[1m' + "***Status Code: " + str(json_status) + "; Missing an entry for one or both locations.***" + '\033[0m')
        elif json_status == 602:
            print(color3 + '\033[1m' +  "***Status Code: " + str(json_status) + "; The route failed, normally due to mustAvoidLinkIds options being set in a way that makes the route impossible.***" + '\033[0m')
        elif json_status == 500:
            print(color3 + '\033[1m' + "***Status Code: " + str(json_status) + "; Unknown error.***" + '\033[0m')
        else:
            print("***For Staus Code: " + str(json_status) + "; Refer to: https://developer.mapquest.com/documentation/directions-api/status-codes***")
    else:
        print(color3 + '\033[1m' + "***Invalid input. Input must be a string.***" + '\033[0m')                    #output if the inputted values are integer or numeric
        continue
sys.exit()