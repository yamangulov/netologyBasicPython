import json

purchase = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i != 0:
            dict_line = json.loads(line)
            purchase[dict_line['user_id']] = dict_line['category']

with open('visit_log.csv', 'r', encoding='utf-8') as f:
    with open('funnel.csv', 'w', encoding='utf-8') as f2write:
        for i, line in enumerate(f):
            line = line.strip()
            key = line.split(',')[0]
            if i == 0:
                f2write.write(line + ',category\n')
            elif(key in purchase.keys()):
                f2write.write(line + "," + purchase[key] + '\n')
