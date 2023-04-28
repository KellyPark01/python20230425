#둘다 선언
from pandas import Series, DataFrame
import pandas as pd

myCampus = Series( [100,200,300,400,500],
    index=["2023-04-25", "2023-04-26", "2023-04-27", "2023-04-28","2023-04-29"])
type(myCampus)

#슬라이싱
myCampus["2023-04-26"]  # 인덱스가 날짜로 바꿔치기 된 것이다.