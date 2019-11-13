import pickle
def read_and_parse(filename):
	f=open(filename,"r")
	line=f.readline()
	words=[]
	while(line):
		#print(line)
		line=f.readline()
		w=line.split(" ")
		for i in range(len(w)):
			w[i]=w[i].strip(" .,!?()@&\"\'\n").lower()
		if[w!=['']]:
			words.extend(w)
	return words

def statistical_analysis(word_list):
	word_dict={}
	for i in word_list:
		if i not in word_dict:
			word_dict[i]=1
		else:
			word_dict[i]+=1
	dump_file=open('word_count.pickle',"wb")
	pickle.dump(word_dict,dump_file)
	print("No of unique words",len(word_dict))
	counts=list(word_dict.values())
	counts.sort(reverse=True)
	print("most freq words: ",end="")
	for i in range(5):
		for j in word_dict:
			if word_dict[j]==counts[i]:
				print("'"+j+"'",", ",end="")
	print()
	print("least freq words: ",end="")
	count=1
	for i in range(5):
		for j in word_dict:
			if(count==5):
				break
			if word_dict[j]==counts[len(counts)-i-1]:
				count+=1
				print("'"+j+"'",", ",end="")
	print()
	print()
	print("Mean freq", sum(counts)//len(counts))
	print("Words with mean freq: ")
	for j in word_dict:
		if word_dict[j]==sum(counts)//len(counts):
			print("'"+j+"'",", ",end="")
	print()
	print()
	print("Median freq", counts[len(counts)//2])
	#Since median frequency is 1 i am not printing them as they will contain lot of words
	print()
def sort_and_dump():
	f=open('word_count.pickle','rb')
	dic=pickle.load(f)
	dic_keys=list(dic.keys())
	dic_counts=list(dic.values())
	dic_keys_sorted=sorted(dic_keys)
	dic_counts_sorted=sorted(dic_counts)
	alphabet_sort={}
	alphabet_sort_arr=[]
	for i in dic_keys_sorted:
		alphabet_sort[i]=dic[i]
		alphabet_sort_arr.append([i,dic[i]])
	
	
	rev_counts=[]
	for i in list(dic.items()):
		rev_counts.append([i[1],i[0]])
	rev_counts.sort(reverse=True)

	f1=open('alphabet_sort.pickle','wb')
	f2=open('freq_sort.pickle','wb')
	#pickle.dump(alphabet_sort)
	print("sorted alphabetically",alphabet_sort_arr[:5])
	print("sorted by counts",rev_counts[:5])
def anagram_list(word_list):
	"""
	WILL TAKE LONG TIME TO RUN
	"""
	anagram_count=[]
	count=0
	for i in word_list:
		count+=1
		print(count)
		temp=0
		temps=[i]
		for j in word_list:
			if check_anagram(i,j):
				temp+=1
				temps.append(j)

		anagram_count.append(temp)
	sort_counts=sorted(anagram_count)

	for k in range(5):
		print(temps[anagram_count.index(sort_counts[k])])
def check_anagram(a,b):
	a_dict={}
	b_dict={}

	for i in a:
		if i not in a_dict:
			a_dict[i]=1
		else:
			a_dict[i]+=1
	for i in b:
		if i not in b_dict:
			b_dict[i]=1
		else:
			b_dict[i]+=1
	if a_dict==b_dict:
		return True
	return False
#anagram_list will take long time to run
# statistical_analysis(read_and_parse("text.txt"))
# sort_and_dump()
#print(statistical_analysis(read_and_parse("text.txt")))
#sort_and_dump()
anagram_list(read_and_parse("text.txt"))
