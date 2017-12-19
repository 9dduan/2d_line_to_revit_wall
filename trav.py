ylist = IN[0]
xlist = IN[1]
MaxWidth = IN[2]
trans = IN[3]

def dom_inter(m,n):
	collector = []
	for item in m:
		count = 0
		i = 0
		while i >= 0 and i < len(n) -1:
			if item - n[i] > 0 and n[i+1] - item >= 0:
				count += 1			
				break
			else: i += 2
		if count > 0:
			collector.append(item)

	for item1 in n:
		count = 0
		i = 0
		while i >= 0 and i < len(m) -1:
			if item1 - m[i] >= 0 and m[i+1] - item1 > 0:
				count += 1
				break
			else: i += 2
			
		if count > 0:
			collector.append(item1)
			
	if len(collector)<=1:
		return [0]
	else:
		output = sorted(collector)
		if output[0] == output[-1]:
			return [0]
		else:
			return sorted(collector)

def dom_minus(m,n):
	collector = []
	_temp = m
	
	if n == [0]:
		return m
	
	else:
		for item in n:
			_temp.append(item)
		temp = sorted(_temp)

		i = 0
		while i >= 0 and i < len(temp) - 1:
			if abs(temp[i] - temp[i+1]) > 0:
				collector.append(temp[i])
				collector.append(temp[i+1])
				i += 2
#			elif abs(temp[i] - temp[i+1]) == 0:
#				collector.append(temp[i])
#				i += 2
				
			else: i+= 2
	
		return collector




col = []

val_trav = []

def _trav(arr,n,p,q):
	global col
#	global val_trav
	
	_range = range(n-1)
	for k in range(len(_range)):
		_range[k] = _range[k]+1
		
	for i in _range:
		
		 
		if i==1:
			
			inter = dom_inter(arr[0],arr[1])
			
			arr[1] = dom_minus(arr[1],inter)
			
			arr[0] = dom_minus(arr[0],inter)
			
			col.append([inter,(xlist[p][1]+xlist[p][0])*0.5,(abs(xlist[p][1]-xlist[p][0])),q])
			
#		else:
			 
#			if abs(xlist[k][i][0]-xlist[k][i-j][0])>IN[2]:
#				break
			
		else:
			
			j=1
			
			while j > 0 and j <= i:
				
				if abs((xlist[p][i])-(xlist[p][i-j])) > MaxWidth:
					
					break
					
				else:
				  	
				  	local_trav = val_trav[i]
				  	
				  	if local_trav == 1e5:
				  		
				  		local_trav = _trav(arr,i,p,q)
				  		
				  		val_trav[i] = local_trav
				
						inter = dom_inter(arr[i], local_trav[i-j])
				
						arr[i-j] = dom_minus(local_trav[i-j],inter)
				
						arr[i] = dom_minus(arr[i],inter)
				
						col.append([inter,(xlist[p][i]+xlist[p][i-j])*0.5,abs(xlist[p][i]-xlist[p][i-j]),q])
				
						j+=1
					
					elif local_trav != 1e5:
						
						inter = dom_inter(arr[i], local_trav[i-j])
				
						arr[i-j] = dom_minus(local_trav[i-j],inter)
				
						arr[i] = dom_minus(arr[i],inter)
				
						col.append([inter,(xlist[p][i]+xlist[p][i-j])*0.5,abs(xlist[p][i]-xlist[p][i-j]),q])
				
						j+=1
			
	return arr
	
#print _trav(list,len(list))
#Assign your output to the OUT variable.

for z in range(len(ylist)):
	for zz in range(len(ylist[z])):
		val_trav.append(1e5)	
		
	_trav(ylist[z],len(ylist[z]),z,trans[z])
	val_trav = []

OUT = filter(lambda x: len(x[0]) > 1, col)