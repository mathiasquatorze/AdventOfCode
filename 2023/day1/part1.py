def get_calibration_value(filename):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    calibration_values = []
    with open(filename) as file:
        for line in file:
            numbers = []
            for i in line:
                if i in digits:
                    numbers.append(i)
            
            calibration_values.append(int(numbers[0] + numbers[-1]))             
    return sum(calibration_values)

value = get_calibration_value("input.txt")
print(value)