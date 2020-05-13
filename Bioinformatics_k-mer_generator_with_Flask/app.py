import os
#importing libraries
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename


#creating instance of the class
app = Flask(__name__)

file_id = "output.txt"

def generate_kmers(start, end):
	for record in fileA[start:end]:
		#file_id = "Fflaviviridae/Output_kmers_All-" + str(start) + "-" +  str(end) + ".txt"
		nr_sequence = record.seq
		seq_len = len(nr_sequence)
		kmer = 9
		count = 0
		temp = []
		for seq in list(range(seq_len-(kmer-1))):
			count += 1
			my_kmer = (nr_sequence[seq:seq+kmer])
			temp.append(str(my_kmer))
		with open(file_id, 'a') as f:
			f.writelines("%s\n" % kmer for kmer in temp)




#to tell flask what url shoud trigger the function index()
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/file-downloads', methods = ['GET', 'POST'])  
def upload():
	if request.method == 'POST':
		fasta_file = request.files['file']
		fasta_file.save(secure_filename(fasta_file.filename))
		# fileA = list(SeqIO.parse(fasta_file,"fasta"))
		# n = len(fileA)
		# pool = ProcessPoolExecutor(12)
		# futures = []
		# perCPUSize = math.ceil(n/12)
		# for i in range(0,12):
		# 	futures.append(pool.submit(generate_kmers, i * perCPUSize, (i+1) * perCPUSize))  

		return 'file uploaded'


if __name__ == '__main__':
	app.run(debug=True)