#problem1
def street_info():
	tuple_list = []
	fout = open("Street_Centrelines.csv","r")
	fout.readline()
	for line in fout:
		line =  line.split(",")
		tuple_list.append((line[2],line[4],line[7],line[8]))

	#print(tuple_list)
	return tuple_list

street_info()
#problem2
def type_maintenance():
	maintenance_dict = dict()
	fout = open("Street_Centrelines.csv","r")
	fout.readline()
	for line in  fout:
		line = line.split(",")
		maintenance_dict[line[12]] = maintenance_dict.setdefault(line[12],0) + 1
	return maintenance_dict
type_maintenance()

#problem3
def unique_owner():
	owner = []
	fout = open("Street_Centrelines.csv","r")
	fout.readline()
	for line in fout:
		line = line.split(",")
		owner.append(line[11])
	owner =  list(set(owner))
	return owner

unique_owner()


#problem4
def str_class():
	str_class = []
	str_name = []
	dict1 = {}
	fout = open("Street_Centrelines.csv","r")
	fout.readline()

	for line in fout:
		line = line.split(",")
		if(line[10] != None or  line[10] != ""):
			dict1.setdefault(line[10],[])
		#str_class.append(line[10)
		#str_name.append(line[2])
	fout.close()
	#closed the file because in later code, the file object is not reading file
	fout = open("Street_Centrelines.csv","r")
	fout.readline()
	for line in fout:
		line = line.split(",")
		dict1[line[10]].append(line[2])
	#print(dict1["ARTERIAL"][len(dict1["ARTERIAL"])-1])
	return dict1
str_class()
