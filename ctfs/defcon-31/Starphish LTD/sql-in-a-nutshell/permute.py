import pprint

datasplit2 = ['1953', '11', '21', '1972', '05', '23', '1965', '01', '02']

years = ['1953', '1972', '1965']
months = ['11', '05', '01']
days = ['21', '23', '02']


for month in months:
    for day in days:
        for year in years:
            print("flag{"+(month+day+year)+"}")

# pprint.pprint(datasplit2)
#
# for first in datasplit2:
#     for second in datasplit2:
#         for third in datasplit2:
#             if (first != second) and (second != third):
#                 all = first + second + third
#
#                 if (len(all) == 8):
#                     print("flag{" + all + "}")
