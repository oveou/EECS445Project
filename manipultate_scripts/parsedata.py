# !/usr/bin/env python
import csv

def readData(data_file, header):	
	data_reader = csv.DictReader(data_file,header,delimiter='\t')
	return data_reader

def select(row):
	if row['MARRIED'] == '1':
		return True
	if (row['S2']) == '1' or (row['S2']) == '2':
		return True
	return False

def checkSucc(row):
	if (row['w4_q5'] == '1') or (row['w4_q1'] == '1'):
		return 1

	if ((row['w4_q9']) == '1') or (row['w4_q3'] == '2') or (row['w4_q3'] == '1') or (row['W3_Q3'] == '2') or (row['W3_Q3'] == '1') or (row['W3_Q9'] == '1') or (row['W3_Q9'] == '3') or (row['W2_Q3'] == '1') or (row['W2_Q3'] == '2') or (row['W2_Q9'] == '1') or (row['W2_Q9'] == '3'):
		return -1
	return 0

def main():
	data_file = open('../data/30103-0001-Data.tsv', 'rU')
	header = next(data_file).strip().split('\t')
	output_file = open('../data/classify_suc_or_not.tsv','wb')
	data_reader = readData(data_file, header)
	
	data = []
	for row in data_reader:
		if checkSucc(row):
			row['success'] = checkSucc(row)
			data.append(row)
	fieldnames = sorted(list(set(k for d in data for k in d)))
	dict_writer = csv.DictWriter(output_file,fieldnames=fieldnames, delimiter='\t')
	dict_writer.writeheader()
	dict_writer.writerows(data)
	data_file.close()
	output_file.close()

if __name__ == '__main__':
    main()