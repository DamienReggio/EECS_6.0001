# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    perms = []
    
    if len(sequence) == 1:
        perms.append(sequence)
        #perms.append(sequence)
    else:
        for i, letter in enumerate(sequence):
            sub_seq = sequence[:i] + sequence[i+1:]
            #print(letter + get_permutations(sub_seq))
            #perms.append(letter)
            #print(perms)
            for permed in get_permutations(sub_seq):
            #permed = get_permutations(sub_seq)
            #permed.extend(letter)
                perms.append(letter + permed)
                #perms.extend(permed)
                
    return perms

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations('111')) #delete this line and replace with your code here

