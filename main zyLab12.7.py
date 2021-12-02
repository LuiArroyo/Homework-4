# Luis Arroyo
# PSID: 2037081
# CIS 2348

#given on zybooks
def get_age():
    adult_age = int(input())
    if 18 <= adult_age <= 75:
        return adult_age
    raise ValueError('Invalid age.')

#given on zybooks
def fat_burning_heart_rate(adult_age):
    return (220 - adult_age) * 0.7

if __name__ == "__main__":
    try:
        adult_age = get_age()
        print('Fat burning heart rate for a', adult_age, 'year-old:', fat_burning_heart_rate(adult_age), 'bpm')
    except ValueError as f:
        print(f)
        print('Could not calculate heart rate info.')
        print()