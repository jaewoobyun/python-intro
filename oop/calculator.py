class Calculator(object): # object 는 객체 의미

    def __init__(self, first_num, second_num): # 생성자인데, 외부에서 입력바든 값을 설정하는 메소드
        self.first_num = first_num
        self.second_num = second_num

    def add(self):
        return self.first_num + self.second_num

    def sub(self):
        return self.first_num - self.second_num

    def mul(self):
        return  self.first_num * self.second_num

    def div(self):
        return  self.first_num / self.second_num

    '''
    클래스 내부에 있는 함수를 메서드라고 정의한다.
    일반메서드에서 정의한 기능을 호출해서 실제 값으로 연산하는 메서드를
    Static Method 라고 하며 @staticmethod 로 표시한다.
    '''
    @staticmethod
    def main():
        while 1: #1 == true
            menu = input('0-종료 1-계산기\n') # \n 줄바꿈
            if menu == '0':
                break
            elif menu == '1':
                first_num = int(input('첫번째 수'))
                second_num = int(input('두번째 수'))
                calc = Calculator(first_num, second_num)
                print('*' * 30)
                print(f'{calc.first_num} + {calc.second_num} = {calc.add()}')
                print(f'{calc.first_num} - {calc.second_num} = {calc.sub()}')
                print(f'{calc.first_num} * {calc.second_num} = {calc.mul()}')
                print(f'{calc.first_num} / {calc.second_num} = {calc.div()}')
                print('*' * 30)
            else:
                print('잘못된 메뉴 선택입니다.')


if __name__ == '__main__': #캡슐화
    Calculator.main()




