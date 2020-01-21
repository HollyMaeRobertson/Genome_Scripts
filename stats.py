
def mean(numbers):
    '''takes an array and returns the mean'''
    total = 0
    for i in numbers:
        total += i
    mean = total/len(numbers)
    return(mean)

def number_bases(line, length):
    '''takes a FASTA file and a letter and returns % of the file that letter'''
    bases = [0.0, 0.0, 0.0, 0.0, 0.0]
    
    for i in range(length):
        if line[i] == 'A':
            bases[0] += 1
        elif line[i] == 'T':
            bases[1] += 1
        elif line[i] == 'C':
            bases[2] += 1
        elif line[i] == 'G':
            bases[3] += 1
        else:
            bases[4] += 1
            
    return bases

def number_bases_again(line, length):
    bases = [0.0, 0.0, 0.0, 0.0, 0.0]
    base_names = ['A', 'T', 'C', 'G', 'N']

    for i in range(len(bases)):
        bases[i] = line.count(base_names[i])
    
    return bases

def add_arrays(array1, array2):
    sum_array = [0.0] * len(array1)
    for i in range(len(array1)):
        sum_array[i] = array1[i] + array2[i]
    return sum_array

def n_calculation(sequence_lengths, number):
    sequence_lengths.sort(reverse = True)
    sequence_number = sum(sequence_lengths)
    index = (number/100) * sequence_number

    sequence_sum = 0
    i=0
    while sequence_sum < index:
        sequence_sum += sequence_lengths[i]
        i += 1

    n_number = sequence_lengths[i-1]
    return n_number
