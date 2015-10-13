#! /usr/bin/env python3
import json, math
class CustomersWithinDistance:
    def __init__(self):
        self.customers_list = []
        self.customers_within_distance_list = []
        try:
            with open("gistfile1.txt", "r") as json_file:
                for customer_data in json_file:
                    self.addCustomerToCustomersList(customer_data)
        except IOError as e:
            print("Failed to open customers json file!\n" + str(e))
        except:
            print("Unexpected error!")
        self.setConstants()
    def setConstants(self):
        self.OFFICE_LAT = math.radians(53.3381985)
        self.OFFICE_LONG = math.radians(-6.2592576)
        self.EARTH_RADIUS = 6371 # km
    def oneLineOfJsonToDict(self, customer_data):
        return json.loads(customer_data)
    def addCustomerToCustomersList(self, customer_data):
        customer_data = self.oneLineOfJsonToDict(customer_data)
        customer_data = self.castStringsToDigits(customer_data)
        self.customers_list.append(customer_data)
    def castStringsToDigits(self, customer_data):
        customer_data["user_id"] = int(customer_data["user_id"])
        customer_data["latitude"] = float(customer_data["latitude"])
        customer_data["longitude"] = float(customer_data["longitude"])
        return customer_data
    def calculateDistanceFromOffice(self, latitude, longitude):
        latitude = math.radians(latitude)
        longitude = math.radians(longitude)
        longitude_delta = math.fabs(self.OFFICE_LONG - longitude)
        angle_expression1 = math.sin(latitude) * math.sin(self.OFFICE_LAT)
        angle_expression2 = math.cos(latitude) * math.cos(self.OFFICE_LAT) \
                            * math.cos(longitude_delta)
        central_angle = math.acos(angle_expression1 + angle_expression2)
        distance = self.EARTH_RADIUS * central_angle
        return distance
    def findAllCustomersWithin100km(self):
        for customer in self.customers_list:
            distance = self.calculateDistanceFromOffice(customer["latitude"], customer["longitude"])
            if distance < 100:
                self.customers_within_distance_list.append(customer)
    def sortCustomersWithinDistanceList(self):
        return sorted(self.customers_within_distance_list, key=lambda k: k['user_id'])
    def printSortedListOfCustomersWithinDistance(self):
        self.findAllCustomersWithin100km()
        for customer in self.sortCustomersWithinDistanceList():
            print("Name: " + customer["name"] + " User ID: " + str(customer["user_id"]))
