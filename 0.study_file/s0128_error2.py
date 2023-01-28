# 파일명: s0128_error2.py
import csv

def average(scores):
    sum = 0
    for score in scores:
        sum += int(score)
    avg = sum / len(scores)
    return avg
def grade(avg):
    if avg >= 90:   grd = 'A'
    elif avg >= 80: grd = 'B'
    elif avg >= 70: grd = 'C'
    elif avg >= 60: grd = 'D'
    else:           grd = 'F'
    return grd

#while True:
for n in range(1, 6):
    filename = f'csv\\class_{n}.csv'
    print(f'파일명: {filename}')
    try:
        file = open(filename, 'r')
        rows = csv.reader(file)
        for name, addr, *scores in rows:
            avg = average(scores)
            grd = grade(avg)
            print(f'{name}학생의 평균점수 {avg:.1f}점, {grd}등급입니다.')
    except FileNotFoundError:
        print(f'파일명: {filename}는 없는 파일입니다.')
    print()

