def num_of_bus_stops(bus_data, street_data):
	counter = 0
	for bus in  bus_data:
		if(bus[7] == "Accessible"):
			for street in  street_data:
				if(bus[9] ==  street[23]):
					if(street[10]== "ARTERIAL"):
						counter = counter + 1

	return "Number of bus_stops from street class ARTERIAL and has accessible facilities: ", counter


def local_street(bus_data, street_data):
	counter = 0
        for bus in  bus_data:
                if(bus[7] == "Non-Standard"):
                        for street in  street_data:
                                if(bus[9] ==  street[23]):
                                        if(street[10]== "LOCAL STREET"):
                                                counter = counter + 1

        return "Number of bus_stops from street class Local Steet and has Non-Standard facilities: ", counter


def inaccessible(bus_data, street_data):
	counter = 0
        for bus in  bus_data:
                if(bus[7] == "Inaccessible"):
                        for street in  street_data:
                                if(bus[9] ==  street[23]):
                                        if(street[10]== "MINOR COLLECTOR"):
                                                counter = counter + 1

        return "Number of bus_stops from street class Local Steet and has Non-Standard facilities: ", counter

bus_data = []
street_data = []
bus_file = open("Bus_Stops.csv", "r")
bus_file.readline()
for file1 in bus_file:
	file1 = file1.split(",")
	bus_data.append(file1)

street_file = open("Street_Centrelines.csv", "r")
street_file.readline()
for file2 in street_file:
	file2 = file2.split(",")
	street_data.append(file2)


num_of_bus_stops(bus_data,street_data)
local_street(bus_data,street_data)
inaccessible(bus_data,street_data)
