import statistics

pop_file = open("DA_P3_data_Pop_200010003.txt", "r")
Ainfo = [] # initialize empty arrays
Binfo = []
for one_line in pop_file: # get the info of each population in their respective info arrays
    line_as_array = one_line.split(", ")
    Ainfo.append(float(line_as_array[0]))
    Binfo.append(float(line_as_array[1]))

actual_mean_A = statistics.mean(Ainfo) # calculate "actual" values
actual_var_A = statistics.variance(Ainfo)
actual_mean_B = statistics.mean(Binfo)
actual_var_B = statistics.variance(Binfo)
print("Mean of A: " + str(actual_mean_A))
print("Variance of A: " + str(actual_var_A))
print("Mean of B: " + str(actual_mean_B))
print("Variance of B: " + str(actual_var_B))

samp_file = open("DA_P3_data_Samp_200010003.txt", "r") # Get sample data
samp=[]
for line in samp_file:
    samp.append(float(line))

print("Sample mean : " + str(statistics.mean(samp)))
print("Sample variance : " + str(statistics.variance(samp)))