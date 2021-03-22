def get_indegree(graph):
	degree = {}
	for key,value in graph:
		for item in value:
			current = degree.get(item,0)+1
			degree.update({item:current})
	for key,value in graph:
		if key not in degree.keys():
			degree[key] = 0
	return degree

def get_outdegree(graph):
	degree = {}
	for key,value in graph:
		degree.update({key:len(value)})
		for item in value:
			if item not in degree.keys():
				degree[item] = 0
	return degree
	
def build_debrujin_graph(kmers):
	#kmers = sorted(kmers)
	kmerMap = {}
	for kmer in kmers:
		left_kmer = kmer[:-1]
		right_kmer = kmer[1:]
		if left_kmer not in kmerMap:
			kmerMap[left_kmer] = []
		kmerMap.get(left_kmer).append(right_kmer)

	# to keep track of the order build an adj list not a dictionary
	adj_list = []
	keys = kmerMap.keys()
	values = kmerMap.values()
	keys = sorted(keys)
	for key in keys:
		adj_list.append((key,sorted(kmerMap[key])))
	return adj_list

def print_graph(graph):
	for k,v in graph:
    		print (k + ": " + str(v))

def find_maximal_paths(graph):
	contigs = []
	outdegree = get_outdegree(graph)
	indegree = get_indegree(graph) 

	for key, value in graph:
		if not ((outdegree[key] == 1) and (indegree[key] == 1)): # starting node condition
			if (outdegree[key] > 0):
				nonbranchingpath = []
				nonbranchingpath.append(key)
				nonbranchingpath.append(value[0])
				i = 1
				#print len(value)
				new = value[0]
				# if intermediate node is in(v) = out(v) = 1 
				while((outdegree[new] == 1) and (indegree[new] == 1)):
					nonbranchingpath.append(new)
					new = omer(graph, new)
					# if there's no non branching node we stop
					if not ((outdegree[new] == 1) and (indegree[new] == 1) ):
						nonbranchingpath.append(new)
				k = 1	
				while(k<len(value)): # do not miss the residual vertices if we finish searching for non branching nodes
					temp = []
					temp.append(key)
					temp.append(value[k])
					contigs.append(temp)
					k+=1
				contigs.append(nonbranchingpath)
	return contigs

# we merge overlapping area in two strings
def merge(s1, s2):
    i = 0
    while not s2.startswith(s1[i:]):
        i += 1
    return s1[:i] + s2

def create_contigs(paths):
	contigs = []
	for path in paths:
		i = 1
		contig = path[0]
		while(i<len(path)):
			contig = merge(contig,path[i])

			i+=1
		contigs.append(contig)
	return contigs
		
def writeList(contigs):
	f = open("contigs.txt","w")
	for contig in contigs:
		f.write(contig + "\n")
	f.close()

def main():
	import sys
	file_name= sys.argv[1] 
	kmers = [line.rstrip('\n') for line in open(file_name)]
	debrujin_graph = build_debrujin_graph(kmers)
	maximal_paths = find_maximal_paths(debrujin_graph)
	contigs = sorted(create_contigs(maximal_paths))
	writeList(contigs)
	
if __name__ == "__main__":
    main()