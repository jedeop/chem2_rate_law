# chem2_rate_law
(화학2) 속도 법칙에 따라 실험 데이터로부터 반응 속도식을 계산하는 스크립트

```bash
python main.py
# [입력 데이터]
# No       element(M)      element(M)    speed(M/min)
#  0            0.02            0.02        3.68e-05 
#  1            0.04            0.02        0.000147 
#  2            0.02            0.04        7.36e-05 
#
# [결과]
# [반응 차수]
# 2.0, 1.0
# [속도 상수]
# 4.6
# [반응 속도식]
# v = 4.6 * [E0]^2.0*[E1]^1.0
#
# [반응 속도 계산하기]
# 새로운 몰농도를 순서대로 입력해주세요: 0.04 0.04
# [결과]
# 몰농도가 0.04, 0.04일 때 반응 속도: 0.0002944 M/min
```
