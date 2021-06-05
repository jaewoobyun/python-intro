class Bmi(object):

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_bmi(self):
        index = self.weight / self.height ** 2 * 10000 # cm 와  m 의 값의 차이를 반영함
        if index >= 35:
            bmi = '고도 비만'
        elif index >= 30:
            bmi = '중(重)도 비만'
        elif index >= 25:
            bmi = '경도 비만'
        elif index >= 23:
            bmi = '과체중'
        elif index >= 18.5:
            bmi = '정상'
        else:
            bmi = '저체중'

        return bmi
            
    @staticmethod
    def main():
        while 1:
            menu = input('0-종료 1-BMI\n')
            if menu == '0':
                break
            elif menu == '1':
                height = int(input('키 입력'))
                weight = int(input('몸무게 입력'))
                bmi = Bmi(height, weight) # bmi 를 인스턴스(객체)라고 한다.
                print(bmi.get_bmi())
            else:
                print('메뉴 다시 설정')
                continue


Bmi.main()