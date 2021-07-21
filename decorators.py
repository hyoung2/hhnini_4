

def decorator(func):
    def decorated(input_text):
        print('함수 시작!') #함수 이전에 실행되는 구문 /함수의 앞을 꾸며줌
        func(input_text)
        print('함수 끝!') #함수 이후에 실행되는 구문 /함수의 뒤를 꾸며줌
    return decorated


@decorator
def hello_world(input_text):
    print(input_text)



hello_world('Hello World!')





def tri_area(tri):
    tri = (a * b) / 2
    return tri

def squ_area(squ):
    squ = a * b
    return squ
a = int(input())
b = int(input())


def decorator(func):
    def decorated(tri, squ):
        if a >=0 and b >= 0:
            return func(tri, squ)
        else :
            return ValueError('Input must be positive value')

