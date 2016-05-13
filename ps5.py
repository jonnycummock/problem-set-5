#! usr/env/bin python


#problem-set-5


#Q1.1 - On what chr is region with largest start position in 'lamina.bed' file? 

lamina='/Users/jonny/data-sets/bed/lamina.bed'

maxstart = 0
maxend = 0
maxchrom = ''

for line in open(lamina):
    if line.startswith('#'): continue

    fields = line.strip().split('\t')

    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])

    if start > maxstart:
        maxstart = start
        maxchrom = chrom
        maxend = end

print 'answer-1: ' + maxchrom


#Q1.2 - What is the region with the largest end position on chrY in 'lamina.bed'? Report as: chrom start end value region_length

large_end = 0

for record in open(lamina):
    if line.startswith('#'): continue

    fields = line.strip().split('\t')

    chrom = fields[0]
    start = int(fields[1])
    end - int(fields[2])
    value = float(fields[3])

    if chrom == 'chrY':
        if end > large_end:
            large_end = end
            large_start = start

print 'answer-2: %s:%s-%s' % ("chrY", large_start, large_end)


#Q2.1 - Which of the first 10 records has largest number of 'C' residues?

from collections import Counter

filename ='/Users/jonny/data-sets/fastq/SP1.fq'

line_num = 0
big_C = 0
big_seq = ''
seq_num = 0
big_qual = 0
rev_comp_list = []
num_records = 0
seq_num = 0
max_C = 0
max_qual = 0

def reverse_complement(sequence):
    comp = []
    for char in sequence:
        if char == 'A':
            comp.append('T')
        elif char == 'T':
            comp.append('A')
        elif char == 'C':
            comp.append('G')
        elif char =='G':
            comp.append('C')
        elif char == 'U':
            comp.append('A')
    return ''.join(reversed(comp))


for line in open(filename):
    line_type = line_num % 4

    if line_type == 0:
        name = line.strip()

    elif line_type == 1:
        seq = line.strip()
        seq_num += 1
    elif line_type == 3:
        qual = line.strip()

        counts = Counter(seq)
        if counts['C'] > big_C and seq_num <= 10:
            big_C = counts['C']
            big_seq = name

        sum_qual = sum([ord(i) for i in qual])
        if sum_qual > big_qual:
            big_qual = sum_qual

        if seq_num <= 10:
                rev_comp_list.append(reverse_complement(seq))

    line_num += 1

print 'answer-3: {}'.format(big_seq)
print 'answer-4: {}'.format(big_qual)
print 'answer-5: {}'.format(rev_comp_list)
