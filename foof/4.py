MASTER = open("4master.dat","r")
TRANSACTION = open("4transaction.dat","r")
NEWMAST = open("4newmaster.dat","w")

MRECORD = MASTER.readline()
TRECORD = TRANSACTION.readline()

while TRECORD != "":
	if MRECORD != "":
		