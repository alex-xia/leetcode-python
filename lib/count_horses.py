'''
There are a lot of horses in the yard, and we want to count how many there are.  Unfortunately, we've only got a recording of the sounds from the yard.  All the horses say "neigh".  The problem is they can "neigh" many times.  The recording from the yard is sadly all mixed together.  So, we need to figure out from the overlapping sounds how many horses there could be.

For example, we've got two horses in the yard, and we hear this "neigneighh".  From this recording, we can successfully deduce there are 2 horses.  Another example is "neighneigh".  From this example, we can only tell there is one horse in the yard.

As an additional complexity, our recording might not be perfect.  If it's a bad recording, we should give "Invalid" as the response.

The input will be given as a string on one line.  The output should be printed on it's own line.

Sample Input
nenigehnieighgh

Sample Output
2
'''

# This is Python 2
import sys

def next_char(ch):
    if ch is 'n':
        return 'e'
    if ch is 'e':
        return 'i'
    if ch is 'i':
        return 'g'
    if ch is 'g':
        return 'h'
    if ch is 'h':
        return 'n'

# count_horse counts the horse from the sound string
def count_horse(sound):
    # horse_dict is a dict
    # key is the next character
    # value is an array of horse indexes
    horse_dict = {}
    horse_cnt = 0
    for c in sound:
        # if 'n' is in horse_dict
        # it means an existing horse is ready to neigh
        # otherwise a new horse must exist
        if c is 'n' and 'n' not in horse_dict:
            horse_cnt += 1
            horse_index = horse_cnt
        else:
            horse_index = horse_dict[c][-1]
            del horse_dict[c][-1]
            if len(horse_dict[c]) == 0:
                del horse_dict[c]
        next = next_char(c)
        if next not in horse_dict:
            horse_dict[next] = []
        horse_dict[next] += [horse_index]
    return horse_cnt


print count_horse('neigneighh')
print count_horse('neighneigh')
print count_horse('nenigehnieighgh')
print count_horse('nenigehnieighgh')