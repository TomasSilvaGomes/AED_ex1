import csv


class Competition:
    def __init__(self, w1, w2, w3):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.csv_list = []
        self.priority_list = []
        with open('Cars_input.csv', 'r') as file:
            next(file)  # to start reading from the second line
            csv_reader = csv.reader(file)
            self.csv_list = list(csv_reader)

    # function that calculates the priority of each car including the accidents
    def priority(self):
        for row in self.csv_list:
            match row[5]:
                case 'FULL_ACCIDENT':
                    # if the car had a full accident the priority is set to a high value
                    calculator1 = (row[0], 1000)
                    self.priority_list.append(calculator1)

                case 'PARTIAL_ACCIDENT':
                    # the cars who had a partial or low accidents will set to a similar formula of the default priority,
                    # the only difference is the fuel loss and tire loss
                    calculator2 = (row[0], (((float(row[7]) * 0.01) + float(row[1])) * self.w1) + (
                            (float(row[6]) + (1 - (int(row[2]) * 0.01))) * self.w2) + (
                                           self.w3 * ((len(self.csv_list) + 1) - int(row[3]))))
                    self.priority_list.append(calculator2)

                case 'LOW_ACCIDENT':
                    calculator3 = (row[0], (((float(row[7]) * 0.01) + float(row[1])) * self.w1) + (
                            (float(row[6]) + (1 - (int(row[2]) * 0.01))) * self.w2) + (
                                           self.w3 * ((len(self.csv_list) + 1) - int(row[3]))))
                    self.priority_list.append(calculator3)

                case _:
                    # default formula of the priority
                    calculator3 = (row[0], (float(row[1]) * self.w1) + ((1 - (int(row[2]) * 0.01)) * self.w2) + (
                            self.w3 * ((len(self.csv_list) + 1) - int(row[3]))))
                    self.priority_list.append(calculator3)

    def __repr__(self):
        # Sort the list by priority in descending order, based on the priority (second element)
        self.priority()
        self.priority_list.sort(key=lambda x: x[1], reverse=True)

        # Format the output as a string
        # the priority scale is not defined in certain scale
        output = ""
        for car_id, priority in self.priority_list:
            output += f"Car ID: {car_id}, Priority: {priority:.2f}\n"
        return output


cp = Competition(0.5, 0.5, 0.1)
print(cp.__repr__())
