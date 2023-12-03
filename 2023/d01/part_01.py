def calculate_calibration_sum(calibration_document):
    total_sum = 0

    for line in calibration_document:
        first_digit = int(next(char for char in line if char.isdigit()))
        last_digit = int(next(char for char in reversed(line) if char.isdigit()))
        calibration_value = first_digit * 10 + last_digit

        # print(calibration_value)
        total_sum += calibration_value

    return total_sum

with open("input.txt", "r") as file:
    calibration_document = file.readlines()

result = calculate_calibration_sum(calibration_document)

print("Sum:", result)
