#import matplotlib as plt

input_file = 'study_fields.tsv'

first_year_in_data_set = 2000 
current_year = 2013
number_of_years_in_data_set = (current_year - first_year_in_data_set + 1) 
list_of_start_years = []
for j in range(0, number_of_years_in_data_set):
	list_of_start_years.append(first_year_in_data_set + j)

number_of_trials_per_year = [0 for x in xrange(0, number_of_years_in_data_set)]
with open(input_file) as clinical_trial_search: 
	next(clinical_trial_search)
	i = 0 
	for line in clinical_trial_search: 
		vals = line.split('\t')
		#vals[16] is the first recieved field, note that all of my 1200 results have the same number of fields 
		start_date = vals[16].split(' ')
		year_started = start_date[2]
		j = 0 
		for year in range(first_year_in_data_set, first_year_in_data_set + number_of_years_in_data_set): 
			if int(year) == int(year_started): 
				current_value = number_of_trials_per_year[j]
				current_value += 1
				number_of_trials_per_year[j] = current_value
			j += 1
		i +=1 
		
print number_of_trials_per_year

#from http://clinicaltrials.gov/ct2/resources/trends
total_number_per_year = [5645, 6996, 8589, 10260, 12056, 15278, 22491, 35927, 49331, 66366, 83542, 101269, 119438, 138802]

normalized_trials_per_year = []
i = 0 
for i in range(0, number_of_years_in_data_set):
	normalized_trials_per_year.append(float(number_of_trials_per_year[i])/float(total_number_per_year[i])) 
	
print normalized_trials_per_year
