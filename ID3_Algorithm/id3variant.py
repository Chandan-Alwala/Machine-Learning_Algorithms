import math
import sys 

# Read input files
rf = open(sys.argv[2], "r")  # Open the input partition file
wf = open(sys.argv[3], "w")  # Open the output partition file
df = open(sys.argv[1], "r")  # Open the dataset file
df_lines = df.readlines()  # Read all lines from the dataset file
total_rows_in_dataset = len(df_lines)
total_columns_in_dataset = len(df_lines[0].split())

# Function to calculate entropy of a list
def entropy(li):
    entropy = 0
    if len(li) == 0:
        return 0
    for att in ['0', '1']:
        freq = li.count(att) / len(li)
        if freq > 0:
            prob = (freq * math.log((1/freq), 2))
            entropy = entropy + prob 
    return entropy

# Function to calculate conditional entropy of an attribute
def conditional_entropy(a):
    zero_li = []; one_li = []; two_li = []
    for i in range(len(a)):
        if a[i] == '0':
            zero_li.append(target[i])
        elif a[i] == '1':
            one_li.append(target[i])
        else:
            two_li.append(target[i])
    return entropy(zero_li)*(len(zero_li)/len(a)) + entropy(one_li)*(len(one_li)/len(a))\
        + entropy(two_li)*(len(two_li)/len(a))

# Dictionary to store information about each partition and attribute
dict_F = {}; dict_att = {}

# Loop through each line in the input partition file
for rf_line in rf:
    # Process each line to calculate gain and determine the splitting attribute
    rf_line_without_id = rf_line.split()
    rf_line_without_id.pop(0)
    num = len(rf_line_without_id)
    store_lists = {}
    for i in range(total_columns_in_dataset):
        store_lists['a%s_list' % i] = []
    for attr in rf_line_without_id:
        temp = df_lines[int(attr)].split()
        for i in range(total_columns_in_dataset):
            store_lists['a%s_list' % i].append(temp[i])
    target = store_lists[list(store_lists.keys())[-1]]
    s_target = entropy(target)
    store_gain = {}
    for i in range(total_columns_in_dataset - 1):
        store_gain['gain_a%s' % i] = - conditional_entropy(store_lists['a%s_list' % i]) + s_target
    gain_max = max(store_gain.values())
    for key, value in store_gain.items():
        if value == gain_max:
            dict_att[rf_line] = 'A' + str(int(key.split('_')[1][1])+1)
            break
    dict_F[rf_line] = gain_max*(num/total_rows_in_dataset)

# Identify the partition with maximum gain
partition_elements = (max(dict_F, key=dict_F.get).split())
partition_num_to_split = partition_elements[0]
partition_elements.pop(0)
attribute_for_partition_split = dict_att[(max(dict_F, key=dict_F.get))]

att_values = []
for ele in partition_elements:
    temp = df_lines[int(ele)].split()
    att_values.append(temp[int(attribute_for_partition_split[1:])-1])

# Create a dictionary to store instances based on attribute values
temp_store = {}
for i in range(len(partition_elements)):
    if att_values[i] not in temp_store:
        temp_store[att_values[i]] = [partition_elements[i]]
    else:
        temp_store[att_values[i]].append(partition_elements[i])

# Generate new partition based on the split
split_partition = []
for key in temp_store.keys():
    split_partition.append(temp_store[key])

# Write the new partitioning to the output partition file
for rf_line in rf:
    if rf_line != partition_num_to_split:
        wf.write(rf_line)
    else:
        for i in range(len(split_partition)):
            insert = str(total_rows_in_dataset + i + 1) + ' ' + ' '.join(split_partition[i])
            wf.write(insert)
            wf.write('\n')

# Print a message indicating the split information
if len(split_partition) == 3:
    print("Partition {} was replaced with partitions {},{},{} using Attribute {}".format(partition_num_to_split, total_rows_in_dataset, total_rows_in_dataset + 1, total_rows_in_dataset + 2, int(attribute_for_partition_split[1:])-1))
elif len(split_partition) == 2:
    print("Partition {} was replaced with partitions {},{} using Attribute {}".format(partition_num_to_split, total_rows_in_dataset, total_rows_in_dataset + 1, int(attribute_for_partition_split[1:])-1))

# Close file handles
rf.close()
wf.close()
df.close()
