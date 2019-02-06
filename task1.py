def street_info():
	tuple_list = []
	fout = open("Street_Centrelines.csv","r")
	fout.readline()
	for line in fout:
		line =  line.split(",")
		tuple_list.append((line[2],line[4],line[7],line[8]))
	


street_info()
