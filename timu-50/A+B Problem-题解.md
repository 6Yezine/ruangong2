0,"currentTemplate":"ProblemShow","currentData":{"problem":{"background":"强烈推荐[新用户必读帖](\/discuss\/show\/241461)。

**不熟悉算法竞赛的选手请看这里：**

算法竞赛中要求的输出格式中，**不能有多余的内容**，**这也包括了“请输入整数 $\bm a$ 和 $\bm b$” 这一类的提示用户输入信息的内容**。若包含了这些内容，将会被认为是 `Wrong Answer`，即洛谷上的 `WA`。在对比代码输出和标准输出时，系统将忽略每一行结尾的空格，以及最后一行之后多余的换行符。

若因此类问题出现本机（看起来）`AC`，提交 `WA` 的现象，请勿认为是洛谷评测机出了问题，而是你的代码中可能存在多余的输出信息。用户可以参考在题目末尾提供的代码。

另外**请善用应用中的在线 IDE 功能**，以避免不同平台的评测中所产生的一些问题。

还有一点很重要的是，请不要在对应的题目讨论区中发布自己的题解，请发布到题解区域中，否则将处以删除或禁言的处罚。若发现无法提交题解则表明本题题解数量过多，仍不应发布讨论。","description":"输入两个整数 $a, b$，输出它们的和（$|a|,|b| \le {10}^9$）。

注意

1. Pascal 使用 `integer` 会爆掉哦！
2. 有负数哦！
3. C\/C++ 的 main 函数必须是 `int` 类型，而且 C 最后要 `return 0`。这不仅对洛谷其他题目有效，而且也是 NOIP\/CSP\/NOI 比赛的要求！

好吧，同志们，我们就从这一题开始，向着大牛的路进发。

> 任何一个伟大的思想，都有一个微不足道的开始。
","inputFormat":"两个以空格分开的整数。","outputFormat":"一个整数。","samples":[["20 30
","50
"]],"hint":"**广告**

洛谷出品的算法教材，帮助您更简单的学习基础算法。[【官方网店绝赞热卖中！】>>>](https:\/\/item.taobao.com\/item.htm?id=637730514783)

[![](https:\/\/cdn.luogu.com.cn\/upload\/image_hosting\/njc7dlng.png)](https:\/\/item.taobao.com\/item.htm?id=637730514783)

**本题各种语言的程序范例：**

C
```c
#include <stdio.h>

int main()
{
    int a,b;
    scanf("%d%d",&a,&b);
    printf("%d\n", a+b);
    return 0;
}
```
----------------

C++
```cpp
#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int a,b;
    cin >> a >> b;
    cout << a+b << endl;
    return 0;
}
```
----------------

Pascal
```cpp
var a, b: longint;
begin
    readln(a,b);
    writeln(a+b);
end.
```
-----------------

Python2

```cpp
s = raw_input().split()
print int(s[0]) + int(s[1])
```
-----------------

Python3

```cpp
s = input().split()
print(int(s[0]) + int(s[1]))
```
-----------------

Java
```java
import java.io.*;
import java.util.*;
public class Main {
    public static void main(String args[]) throws Exception {
        Scanner cin=new Scanner(System.in);
        int a = cin.nextInt(), b = cin.nextInt();
        System.out.println(a+b);
    }
}
```
-----------------

JavaScript （Node.js）

```javascript
const fs = require('fs')
const data = fs.readFileSync('\/dev\/stdin')
const result = data.toString('ascii').trim().split(' ').map(x => parseInt(x)).reduce((a, b) => a + b, 0)
console.log(result)
process.exit() \/\/ 请注意必须在出口点处加入此行
```

-----------------

Ruby

```ruby
a, b = gets.split.map(&:to_i)
print a+b
```

-----------------

PHP

```php
<?php
$input = trim(file_get_contents("php:\/\/stdin"));
list($a, $b) = explode(' ', $input);
echo $a + $b;
```

-----------------

Rust

```rust
use std::io;

fn main(){
    let mut input=String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut s=input.trim().split(' ');

    let a:i32=s.next().unwrap()
               .parse().unwrap();
    let b:i32=s.next().unwrap()
               .parse().unwrap();
    println!("{}",a+b);
}
```

-----------------

Go

```go
package main

import "fmt"

func main() {
    var a, b int
    fmt.Scanf("%d%d", &a, &b)
    fmt.Println(a+b)
}
```

-----------------

C# Mono

```cs
using System;

public class APlusB{
    private static void Main(){
        string[] input = Console.ReadLine().Split(' ');
        Console.WriteLine(int.Parse(input[0]) + int.Parse(input[1]));
    }
}
```

------------------

Visual Basic Mono

```vb
Imports System

Module APlusB
    Sub Main()
        Dim ins As String() = Console.ReadLine().Split(New Char(){" "c})
        Console.WriteLine(Int(ins(0))+Int(ins(1)))
    End Sub
End Module
```

------------------

Kotlin

```kotlin
fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    println(a + b)
}
```

------------------

Haskell

```haskell
main = do
    [a, b] <- (map read . words) `fmap` getLine
    print (a+b)
```

------------------

Scala

```scala
object Main extends App {
    println(scala.io.StdIn.readLine().split(" ").map(_.toInt).sum)
}
```

------------------

Perl

```perl
my $in = <STDIN>;
chomp $in;
$in = [split \/[\s,]+\/, $in];
my $c = $in->[0] + $in->[1];
print "$c\n";
```
","provider":{"uid":3,"name":"洛谷","slogan":"","badge":null,"isAdmin":true,"isBanned":false,"color":"Purple","ccfLevel":0,"background":""},"attachments":[],"canEdit":false,"limits":{"time":[1000,1000,1000,1000,1000,1000,1000,1000,1000,1000],"memory":[524288,524288,524288,524288,524288,524288,524288,524288,524288,524288]},"stdCode":"#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int a,b;
	cin >> a >> b;
	cout << a+b;
	return 0;
}","tags":[1],"wantsTranslation":false,"totalSubmit":1157388,"totalAccepted":653482,"flag":5,"pid":"P1001","title":"A+B Problem","difficulty":1,"fullScore":100,"type":"P"},"contest":null,"discussions":[{"id":686131,"title":"为什么高精的AC代码这道题AC不了","forum":{"id":5,"name":"P1001 A+B Problem","slug":"P1001"}},{"id":681105,"title":"所以极限压列是什么样子的","forum":{"id":5,"name":"P1001 A+B Problem","slug":"P1001"}},{"id":680217,"title":"萌新才入门c++，求大佬改改，悬棺","forum":{"id":5,"name":"P1001 A+B Problem","slug":"P1001"}},{"id":678862,"title":"bfs CE 悬一关","forum":{"id":5,"name":"P1001 A+B Problem","slug":"P1001"}},{"id":677880,"title":"为什么会AC","forum":{"id":5,"name":"P1001 A+B Problem","slug":"P1001"}},{"id":673147,"title":"为什么会AC呢","forum":{"id":5,"name":"P1001 A+B Problem","slug":"P1001"}}],"bookmarked":false,"vjudgeUsername":null,"recommendations":[{"pid":"P1421","title":"小玉买文具","difficulty":1,"fullScore":100,"type":"P"},{"pid":"P1425","title":"小鱼的游泳时间","difficulty":1,"fullScore":100,"type":"P"},{"pid":"P1000","title":"超级玛丽游戏","difficulty":1,"fullScore":100,"type":"P"},{"pid":"P5703","title":"【深基2.例5】苹果采购","difficulty":1,"fullScore":100,"type":"P"},{"pid":"P5704","title":"【深基2.例6】字母转换","difficulty":1,"fullScore":100,"type":"P"}],"lastLanguage":0,"lastCode":"","privilegedTeams":[],"userTranslation":null},"currentTitle":"A+B Problem","currentTheme":null,"currentTime":1694781621