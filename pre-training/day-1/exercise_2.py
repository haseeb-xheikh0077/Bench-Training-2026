
def grade_classifier(score):
    if score >= 90:
        return "Distinction"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"

# Test with 5 values
print(grade_classifier(95))
print(grade_classifier(72))
print(grade_classifier(60))
print(grade_classifier(45))
print(grade_classifier(38))

print("---------------------------------")

scores = [45, 72, 91, 60, 38, 85]

for score in scores:
    result = grade_classifier(score)
    print(f"Score: {score} → Grade: {result}")
