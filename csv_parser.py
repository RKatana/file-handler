import csv
def csv_reader(file) -> None: 
    with open(file) as buffer:
        # You can cread a head or tail expression here to get the first or last n values
        lines = csv.DictReader(buffer)
        for line in lines:
            item = {line['Student']: {
                'Django IP 1': line['Python/django week 1 IP (9327)'],
                'Django IP 2': line['Python/django week 2 IP (9328)'],
                'Django IP 3': line['Python/django week 3 IP (9329)'],
                'Django IP 4': line['Python/django week 4 IP (9330)'],
                'Attendance': line['Roll Call Attendance (9347)']
            }}
            print(item,  end='\n\n')
            
if __name__ == '__main__':
    csv_reader('final_list.csv')