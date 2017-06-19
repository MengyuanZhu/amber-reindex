#!/usr/bin/python
import sys

def main(argv=[__name__]):
	
	if len(argv) != 4:
		print("%s <original PDB> <amber PDB> <outfile>" % argv[0])
		exit()

	originalFile=argv[1]
	amberFile=argv[2]
	modifiedFile=argv[3]
	
	original=open(originalFile, "r")
	amber=open(amberFile, "r")
	modified=open(modifiedFile, "w")

	residueIndex=0
	amberResidueIndex=0
	while True:
		amberLine=amber.readline()
		if not amberLine:
			break


		if not amberLine[0:4]=="ATOM":
			continue
		if not amberLine[22:27]== amberResidueIndex:
			newIndex=True
			while True:
				originalLine=original.readline()
				if not originalLine:
					break
	
				if not originalLine[0:4]=="ATOM":
					continue
				if residueIndex==originalLine[22:27]:
					continue
				else:
					if newIndex:
						residueIndex=originalLine[22:27]
						newIndex=False
					else:
						break
			amberResidueIndex=amberLine[22:27]
			
		modified.write(amberLine[0:22]+residueIndex+amberLine[27:])
	
if __name__ == "__main__":
    sys.exit(main(sys.argv))

