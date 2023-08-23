with open('data/zinc15_actives_predict_infos.csv') as f:
    content = f.readlines()
smi_score_info = {}
for index, line in enumerate(content):
    if index!=0:
        smi = line.strip().split(',')[0]
        score = line.strip().split(',')[2]
        smi_score_info[smi] = score
with open('data/zinc15_actives_similar_neighbours.csv') as f:
    content = f.readlines()
f = open('data/zinc15_actives_similar_neighbours_score.csv', 'w')
for index, line in enumerate(content):
    if index == 0:
        text_list = line.strip().split(',')
        new_text_list = text_list[:1]+['predict_socre']+text_list[1:]
        f.write(",".join(new_text_list)+'\n')
    else:
        neighbor_list = line.strip().split(',')
        smi = line.strip().split(',')[0]
        new_neighbor_list = neighbor_list[:1] + [smi_score_info.get(smi)] + neighbor_list[1:]
        f.write(",".join(new_neighbor_list) + "\n")


