
class transaction:
	def __init__(self):
		self.items=[]
		self.total_utility=0
		self.each_utility=[]
		self.transaction_id=0


def load_dataset():
	all_items=[]

	f=open("foodmart_utility.txt","r")

	Transaction_objects=[]

	tid=0
	for each_transaction in f:
		tid=tid+1
		temp=transaction()
		S=each_transaction.split(":")
		S[0]=S[0].split(" ")
		S[2]=S[2].split(" ")

		for each_item in S[0]:
			temp.items.append(int(each_item))

		temp.total_utility=int(S[1])

		for each_util in S[2]:
			temp.each_utility.append(int(each_util))

		temp.transaction_id=tid

		Transaction_objects.append(temp)

		all_items=all_items+temp.items

	all_items=list(set(all_items))

	return Transaction_objects,all_items

T1=load_dataset()


print("items=",T1[0].items)
print("total_utility=",T1[0].total_utility)
print("each_utility=",T1[0].each_utility)
print("tid=",T1[0].transaction_id)