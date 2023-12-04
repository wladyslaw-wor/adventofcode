def calculate_calibration_sum(calibration_document):
    total_sum = 0

    for line in calibration_document:
        digits = [int(char) for char in line if char.isdigit()]

        if len(digits) >= 1:
            calibration_value = digits[0] * 10 + digits[-1]
            total_sum += calibration_value
    return total_sum

with open("input.txt", "r") as file:
    calibration_document = file.readlines()

result = calculate_calibration_sum(calibration_document)
print("Sum:", result)
