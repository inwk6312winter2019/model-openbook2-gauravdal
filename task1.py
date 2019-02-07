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
	str_class= []
	fout = open("Street_Centrelines.csv","r")
	fout.readline()
	i = 0
	for line in fout:
		line = line.split(",")
		str_class.append(line[10])

	return str_class
str_class()
