#include<stdio.h>
#include<stdlib.h>

int main()
{
    system("python3 ./check.py > test.csv");
    system("python3 ./MLP.py");
}
