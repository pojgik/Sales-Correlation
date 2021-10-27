import pandas as pd
import traceback
import numpy
import math
data = {'Hot dogs': [45,37,42,35,39],
        'Ketchup': [38,31,26,28,33],
        'Canned stew': [10,15,17,21,12],
        'Bagged ice': [43,22,33,38,44],
        'Hot chocolate': [5,4,2,13,7]
        }
def filter_data(input_data): #filters data to remove values outside the range of -0.99 to 0.99
    try:
        filtered_data = {}
        x = 0
        for i in input_data.keys(): #Sorts through dict to find/remove self-correlation values
            inner_data = {}
            for j in input_data[i].keys(): #
                #print(j)
                if input_data[i][j] != 1 and input_data[i][j] != -1: #Adds all values that are not -1 or 1 to a new dictionary
                    x = input_data[i][j]
                    inner_data[j] = x
            filtered_data[i] = inner_data
        return filtered_data
    except Exception as e:
        print('Error:')
        print(e)
        traceback.print_exc()

def most_correlated(raw_data): #Find the items that are most and least correlated and say something about them - Change so that it instead finds which item is least correlated with all other items
    try:    
        new_data = pd.DataFrame.from_dict(raw_data)
        data_correlation = new_data.corr()
        filtered_correlation = filter_data(data_correlation.to_dict())
        #print(filtered_correlation)
        inner_data = {}
        x = 0
        xx = 2
        largest_name = ''
        biggest_name = ''
        y = 0
        yy = 0
        z = 0
        zx = 0
        Distances = {}
        largest = {}
        smallest = {}
        story_high = ''
        story_low = ''

       # for k in filtered_correlation.keys():
           # for l in filtered_correlation[k].keys():
           #     inner_data[l] = L2_Calc(find_share(raw_data,k),find_share(raw_data,l))
       # print(Distances)

        for i in filtered_correlation.keys(): #Sort through and find which two items have the highest correlation.
            for j in filtered_correlation[i].keys(): #Sort through each individual dict to find if it has a value higher than the current highest. If so, add to other dict.
                #print (j)
                if largest.__len__() < 5 and filtered_correlation[i][j] > 0: #Add first five values to largest.
                    x = filtered_correlation[i][j]
                    largest[i+' and '+j] = [x, (find_share(data,i)+find_share(data,j))]
                elif largest.__len__() == 5: #Once there are 5 values, find lowest value in largest, compare with current value, and if it is greater, replace it.
                    for key in largest:
                        if largest[key][0] < xx:
                            xx = largest[key][0]
                            largest_name = key
                    if filtered_correlation[i][j] > largest[largest_name][0] and filtered_correlation[i][j] > 0:
                        x = filtered_correlation[i][j]
                        largest[i+' and '+j] = [x, (find_share(data,i)+find_share(data,j))]
                        del largest[largest_name]
                        xx = 2
               # filtered_correlation[i][j] > x:
                   # x = filtered_correlation[i][j]
                   # largest[i+' and '+j] = [x, (find_share(data,i)+find_share(data,j))]
        #print(largest)
        for key in largest: #Sort through dict of highest to find the highest dollar value
            if largest[key][1] > y:
                y = largest[key][1]
                story_high = key
        #print(f'highest = {y}')
        
        for a in filtered_correlation.keys(): #Sort through each individual dict to find which two items are most anti-correlated.
            for b in filtered_correlation[a].keys(): #Sort through each individual dict to find if it has a value lower than the current lowest. If so, add to other dict.
                #print (b)
                if smallest.__len__() < 5 and filtered_correlation[a][b] < 0: #Add first five values to largest.
                    x = filtered_correlation[i][j]
                    smallest[a+' and '+b] = [x, (find_share(data,i)+find_share(data,j))]
                elif smallest.__len__() == 5 and filtered_correlation[a][b] < 0: #Once there are 5 values, find lowest value in largest, compare with current value, and if it is greater, replace it.
                    for key in smallest:
                        if smallest[key][0] < xx:
                            xx = smallest[key][0]
                            largest_name = key
                    if filtered_correlation[a][b] > smallest[largest_name][0]:
                        smallest[a+' and '+b] = [x, (find_share(data,i)+find_share(data,j))]
                        del smallest[largest_name]
                        xx = 2
                if filtered_correlation[a][b] < z:
                    z = filtered_correlation[a][b]
                    smallest[a+' and '+b] = [z, (find_share(data,a)+find_share(data,b))]
        #print(smallest)
        for key in smallest: #Sort through dict of lowest to find the highest share of sales in it, and then write the story.
            if smallest[key][1] > zx:
                zx = smallest[key][1]
                story_low = key
        #print(f'lowest = {zx}')

        return f'{story_high} sold very well together, with a correlation of {largest[story_high][0]} while {story_low} were anti correlated by {smallest[story_low][0]}, meaning while one sold well the other did not.' #Change phrasing to be more descriptive
    except Exception as e:
        print('Error:')
        print(e)
        traceback.print_exc()

def find_share(sales, sales_key):
    total = 0
    share_count = 0
    share = 0
    for a in sales.values():
        for b in a:
            total = total + b
    for i in sales[sales_key]:
        share_count = share_count + i
    return share_count

def L2_Calc(Vector1,Vector2):
    diff = []
    squares = []
    for i in range(0,len(Vector1)-1):
        diff.append(abs(Vector1[i]-Vector2[i]))
    for j in diff:
        squares.append(j*j)
    x = math.sqrt(sum(squares))
    return x



sales_data = pd.DataFrame(data,columns=['Hot dogs','Ketchup','Canned stew','Bagged ice','Hot chocolate'])
data_correlation = sales_data.corr()
print('Sales Data:')
print(sales_data)
print()
print('Sales Data Correlation:')
print(data_correlation)
print()
print(most_correlated(data))

#print(most_correlated(data))

#print(find_share(data,'Hot dogs'))
#most_correlated(data)