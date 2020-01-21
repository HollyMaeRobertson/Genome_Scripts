import sys
import stats

#sets file to read as first thing after genome_reader.py on the command line
file = sys.argv[1]

#initialise some things
seq_number = 0
seq_lengths = []
current_seq_length = 0
total_bases = [0.0, 0.0, 0.0, 0.0, 0.0]

with open(file) as f:
    for line in f:
        line = line.strip()

        #specify what happens to lines that aren't sequence
        if line[0] == ">":
            seq_number += 1
            seq_lengths.append(current_seq_length) #updates

            print("Current length: " + str(current_seq_length) +
                  "\tCurrent sequence: " + str(seq_number),
                  file=sys.stderr,
                  end = "\r") #shows what is going on

            current_seq_length = 0 #re-initialise

        #specify what happens to lines that are sequence
        else:
            length = len(line)
            current_seq_length += length #gets length of seq in bp
            
            bases = stats.number_bases_again(line, length)
            total_bases = stats.add_arrays(total_bases, bases)#how many bases

seq_lengths.append(current_seq_length)
seq_lengths.pop(0) #the first seq length is always 0 

#get percent bases using total bases
total = sum(total_bases)
percentages = [(i/total)*100 for i in total_bases]
base_names = ['A', 'T', 'C', 'G', 'N']

#print the results
print("\n\nNumber of reads: " + str(seq_number))

average_length = stats.mean(seq_lengths)
print("\nAverage read length: " + str(average_length))

print("\nBases")
for i in range(len(total_bases)):
    print("%" + str(base_names[i]) + ": " + str(percentages[i]))

n50 = stats.n_calculation(seq_lengths, 50)
print("\nN50 of sequences: " + str(n50))

n90 = stats.n_calculation(seq_lengths, 90)
print("N90 of sequences: " + str(n90))
