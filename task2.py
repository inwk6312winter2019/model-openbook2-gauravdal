def num_of_bus_stops():
	bus_file = open("Bus_Stops.csv", "r")
	bus_file.readline()
	street_file = open("Street_Centrelines.csv", "r")
	street_file.readline()
	counter = 0
	for bus in  bus_file:
		bus = bus.split(",")
		if(bus[7] == "Accessible"):
			for street in  street_file:
				street = street.split(",")
				if(bus[9] ==  street[23]):
					if(street[10]== "ARTERIAL"):
						counter = counter + 1
						street_file.seek(1)
	print("Number of bus_stops from street class ARTERIAL and has accessible facilities: ", counter)

num_of_bus_stops()
