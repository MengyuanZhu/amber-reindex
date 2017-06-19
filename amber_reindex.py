originalFile="2hu0.pdb"
amberFile="500ps.pdb"
modifiedFile="modified.pdb"
original=open(originalFile, "r")
amber=open(amberFile, "r")
modified=open(modifiedFile, "w")
residueIndex=0
amberResidueIndex=0
while True:
	amber_line=amber.readline()
	if not amber_line:
		break
	amber_data=amber_line.split()

	if not amber_line[0:4]=="ATOM":
		continue
	if not amber_line[22:27]== amberResidueIndex:
		newIndex=True
		while True:
			original_line=original.readline()
			if not original_line:
				break
			original_data=original_line.split()
			if not original_line[0:4]=="ATOM":
				continue
			if residueIndex==original_line[22:27]:
				continue
			else:
				if newIndex:
					residueIndex=original_line[22:27]
					newIndex=False
				else:
					break
		amberResidueIndex=amber_line[22:27]
			
	modified.write(amber_line[0:22]+residueIndex+amber_line[27:])
	

