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

def type_maintenance():
	maintenance_dict = dict()
	fout = open("Street_Centrelines.csv","r")
	fout.readline()
	for line in  fout:
		line = line.split(",")
		maintenance_dict[line[12]] = maintenance_dict.setdefault(line[12],0) + 1
	return maintenance_dict
type_maintenance()


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



def str_class():
	str_class = []
	str_name = []
	dict1 = {}
	fout = open("Street_Centrelines.csv","r")
	fout.readline()
	i = 0
	for line in fout:
		line = line.split(",")
		dict1.setdefault(line[10],[])
		#str_class.append(line[10)
		#str_name.append(line[2])
	print(dict1)
	fout.seek(0)
	fout.readline()
	for line in fout:
		print(line)
		dict1[line[10]].append([line[2]])
	print(dict1)
	
str_class()
