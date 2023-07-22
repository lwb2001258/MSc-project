with open('test_result.txt') as f:
    content = f.readlines()
f = open("test_classfication.txt", 'w')
f1 = open("data/smiles_test.csv", 'w')
f.write("SMILES,active\n")
f1.write("SMILES\n")

for line in content:
    try:
        smi = line.strip().split("\t")[0]
        mean_inhibition = float(line.strip().split("\t")[1])
        if mean_inhibition < 0.1:
            active = '1'
        else:
            active = '0'
        f.write(smi+","+active+"\n")
        f1.write(smi+"\n")


    except:
        print(line)
