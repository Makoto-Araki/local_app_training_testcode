from apps.hello import hello
from apps.calculator import divide, divide_custom

def main():
    #greeting = hello()
    #print(greeting)

    answer = divide(4, 2)
    print(answer)

if __name__ == "__main__":
    main()