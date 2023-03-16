import csv
import math
 
f = open('data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
rdr.__next__()
data = list(rdr)
f.close()

print("입력 데이터: ")
print(data)

m = 0;
n = 0;
k = 0;

for i1, d1 in enumerate(data):
    for i2, d2 in enumerate(data):
        if i1 == i2:
            continue
        if float(d1[0]) == float(d2[0]):
            num1 = float(d1[1])
            num2 = float(d2[1])
            dnum = num1 / num2
            speed1 = float(d1[2])
            speed2 = float(d2[2])
            dspeed = speed1 / speed2
            n = round(math.log10(dspeed) / math.log10(dnum), 2)
        elif float(d1[1]) == float(d2[1]):
            num1 = float(d1[0])
            num2 = float(d2[0])
            dnum = num1 / num2
            speed1 = float(d1[2])
            speed2 = float(d2[2])
            dspeed = speed1 / speed2
            m = round(math.log10(dspeed) / math.log10(dnum), 2)

print(m , n)

tmp1 = float(data[0][2]) 
tmp2 = pow(float(data[0][0]), m)
tmp3 = pow(float(data[0][1]), n)
k = tmp1 / (tmp2 * tmp3)
print(tmp1, tmp2, tmp3, k)