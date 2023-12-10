#define _CRT_SECURE_NO_WARNINGS 1
#include <iostream>		//这是预处理指令 引入头文件：iostream库
using namespace std;	//使用命名空间std

//函数声明
void welcome;

int main()	//这是主函数（主函数可以返回一个int类型）
{	

	 /*
	<< 是输出操作符
	cout
	endl(endline)表示结束这一行
	输出hello world
	*/
	cout << "hello world" << endl;

	welcome();

	//等待键盘输入 类似system("pause")
	cin.get();
	cin.get();

	return 0;	//这是返回值 为0也可以不写

}