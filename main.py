import csv
import math

# 파일에서 데이터 읽기
data = []
with open('data.csv', 'r') as f:
    rdr = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    data = list(rdr)

# 읽은 데이터 화면에 출력
print("[입력 데이터]")
print(f'No {"      element(M)" * (len(data[0]) - 1)}    speed(M/min)')

for i, d in enumerate(data):
    print(f'{i:2}', end=' ')
    for el in d:
        print(f'{el:15}', end=' ')
    print()

# 반응 차수를 저장할 변수 준비
odr = [None for _ in data[:-1]]  # odr : order of reaction

# 반응 차수 계산
for i1, row1 in enumerate(data):
    for i2, row2 in enumerate(data):  # 2중 반복문을 통해 실험 데이터 2개를 가져옴
        if i1 == i2:  # 가져온 데이터가 같은 실험 데이터면 건너뛰기
            continue

        # 두 실험 데이터에서 각 원소의 몰농도가 같으면 0, 다르면 1
        compare = [0 if mol1 == mol2 else 1 for mol1,
                   mol2 in zip(row1[:-1], row2[:-1])]

        if sum(compare) == 1:  # 위에서 구한 리스트의 합이 1이면 (= 몰농도가 다른 원소가 1개면) => 반응 차수 계산
            i = compare.index(1)  # 몰농도가 다른 원소의 인덱스 가져오기
            mol1, mol2 = row1[i], row2[i]  # 몰농도가 다른 원소의 몰농도 값 가져오기

            dmol = mol1 / mol2  # 몰농도가 몇 배인지 계산

            speed1, speed2 = row1[-1], row2[-1]  # 두 실험의 반응 속도 가져오기
            dspeed = speed1 / speed2  # 반응 속도가 몇 배인지 계산
            odr[i] = round(math.log10(dspeed) /
                           math.log10(dmol), 2)  # 반응 차수 계산 후 저장

# 속도 상수 계산
tmp = 1
for mol, order in zip(data[0], odr):
    tmp *= pow(mol, order)  # [A]^m * [B]^n ... 부분들 계산

k = round(data[0][-1] / tmp, 2)  # 속도 상수를 계산하고 소숫점 2번째 자리까지 반올림

# 계산 결과 출력
print('')
print('[결과]')

print('[반응 차수]')
print(", ".join(map(str, odr)))

print('[속도 상수]')
print(k)

print('[반응 속도식]')
text = '*'.join([f'[E{i}]^{order}' for i, order in enumerate(odr)])
print(f'v = {k} * {text}')

# 새로운 몰농도일 때 속도 계산
print('')
print('[반응 속도 계산하기]')

mols = list(map(float, input('새로운 몰농도를 순서대로 입력해주세요: ').split()))

speed = k
for mol, order in zip(mols, odr):
    speed *= pow(mol, order)  # [A]^m * [B]^n ... 부분들 계산

print('[결과]')
mols_text = (", ".join(map(str, mols)))
print(f'몰농도가 {mols_text}일 때 반응 속도: {speed} M/min')
