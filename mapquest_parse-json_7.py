import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Kf4MrxBifKdgiInGG6N7bWMA46ACtFPx"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + \
        urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) +
              " = A successful route call.")
        
        print("=====================================================================")
        
        print((orig) + " Information")
        print("Country: " + (json_data["route"]["locations"][0]["adminArea1"]))
        print("Province: " + (json_data["route"]["locations"][0]["adminArea3"]))
        print("Type: " + (json_data["route"]["locations"][0]["geocodeQuality"]))
        print("Geo Quality Code: "+(json_data["route"]["locations"][0]["geocodeQualityCode"]))

        print("=====================================================================")
        print((dest) + " Information")
        print("Country: " + (json_data["route"]["locations"][1]["adminArea1"]))
        print("Province: " + (json_data["route"]["locations"][1]["adminArea3"]))
        print("Type: " + (json_data["route"]["locations"][1]["geocodeQuality"]))
        print("Geo Quality Code: "+(json_data["route"]["locations"][1]["geocodeQualityCode"]))
        
        print("=====================================================================")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("Directions from " + (orig) + " to " + (dest))
        print()
        
        print("GPS Coordinate of Origin: Longitude: " +
              str(json_data["route"]["boundingBox"]["ul"]["lng"]) + ", Latitude: " + str(json_data["route"]["boundingBox"]["ul"]["lat"]))
        print("GPS Coordinate of Destination: Longitude: " +
              str(json_data["route"]["boundingBox"]["lr"]["lng"]) + ", Latitude: " + str(json_data["route"]["boundingBox"]["lr"]["lat"]))

        print()
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        
        print()
        print("Kilometers: " +
              str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        
        print()
        print("Fuel Used (Ltr): " +
              str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("=====================================================================")
        
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" +
                  str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=====================================================================")
        
        print("=====================================================================")
        print("Other Miscellaneous Information:")
        print("Will I encounter any toll road? " , (json_data["route"]["hasTollRoad"]))
        print("Will I encounter any bridge? " , (json_data["route"]["hasBridge"]))
        print("Will I encounter any tunnel? " , (json_data["route"]["hasTunnel"]))
        print("Will I encounter any highway? " , (json_data["route"]["hasHighway"]))
        print("Is there any access restriction? " , (json_data["route"]["hasAccessRestriction"]))
        print("Is there any seasonal closure? " , (json_data["route"]["hasSeasonalClosure"]))
        print("Is there any country cross? " , (json_data["route"]["hasCountryCross"]))
        print("=====================================================================\n")

    elif json_status == 402:
        print("_____________________________________________________________________")
        print("Status Code: " + str(json_status) +
              "; Invalid user inputs for one or both locations.")
        print("___________________________________________________________________\n")
    elif json_status == 611:
        print("_____________________________________________________________________")
        print("Status Code: " + str(json_status) +
              "; Missing an entry for one or both locations.")
        print("___________________________________________________________________\n")
    elif json_status == 602:
        print("_____________________________________________________________________")
        print("Status Code: " + str(json_status) + "; The route failed, normally due to mustAvoidLinkIds options being set in a way that makes the route impossible.")
        print("___________________________________________________________________\n")
    elif json_status == 500:
        print("_____________________________________________________________________")
        print("Status Code: " + str(json_status) + "; Unknown error.")
        print("___________________________________________________________________\n")
    else:
        print("_____________________________________________________________________")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("___________________________________________________________________\n")