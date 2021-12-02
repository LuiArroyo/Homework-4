# Luis Arroyo
# PSID: 2037081
# CIS 2348

#empy list
data = []

#def name given on zybooks
def selection_sort_descend_trace(N):
    #N-1 where N is teh size
    for integers in range(len(N) - 1):
        biggest_index = integers
        for n in range(integers + 1, len(N)):
            if N[n] > N[biggest_index]:
                biggest_index = n
        N[integers], N[biggest_index] = N[biggest_index], N[integers]
        print(' ' .join ([str(f) for f in N], ),'')
    #return
    return N

#zybooks said to complete __main__
if __name__ == '__main__':
    #classifies value as an ordered_output
    ordered_output = [int(value) for value in input().split()]
    #reverse order
    selection_sort_descend_trace(ordered_output)