0,"currentTemplate":"ProblemShow","currentData":{"problem":{"background":"","description":"又到暑假了，住在城市 A 的 Car 想和朋友一起去城市旅游。  
她知道每个城市都有 $4$ 个飞机场，分别位于一个矩形的 $4$ 个顶点上，同一个城市中两个机场之间有一条笔直的高速铁路，第 $i$ 个城市中高速铁路了的单位里程价格为 $T_i$，任意两个不同城市的机场之间均有航线，所有航线单位里程的价格均为 $t$。


![](https:\/\/cdn.luogu.com.cn\/upload\/image_hosting\/lxmsezev.png)

**注意**：图中并没有标出所有的铁路与航线。


那么 Car 应如何安排到城市 B 的路线才能尽可能的节省花费呢？她发现这并不是一个简单的问题，于是她来向你请教。


找出一条从城市 A 到 B 的旅游路线，出发和到达城市中的机场可以任意选取，要求总的花费最少。
","inputFormat":"第一行为一个正整数 $n$，表示有 $n$ 组测试数据。

每组的第一行有 $4$ 个正整数 $S,t,A,B$。

$S$ 表示城市的个数，$t$ 表示飞机单位里程的价格，$A$，$B$ 分别为城市A，B 的序号。

接下来有 $S$ 行，其中第 $i$ 行均有 $7$ 个正整数$x_{i1},y_{i1},x_{i2},y_{i2},x_{i3},y_{i3},T_i$，这当中的 $(x_{i1},y_{i1}), (x_{i2},y_{i2}), (x_{i3},y_{i3})$，分别是第 $i$ 个城市中任意 $3$ 个机场的坐标，$T_i$ 为第 $i$ 个城市高速铁路单位里程的价格。
","outputFormat":"共有 $n$ 行，每行 $1$ 个数据对应测试数据。  
保留一位小数。
","samples":[["1
3 10 1 3
1 1 1 3 3 1 30
2 5 7 4 5 2 1
8 6 8 8 11 6 3","47.5"]],"hint":"【数据范围】  
对于 $100\%$ 的数据，$1\le n \le 10$，$1\le S \le 100$，$1\le A,B \le S$。

**【题目来源】**

NOIP 2001 提高组第四题","provider":{"uid":19,"name":"CCF_NOI","slogan":"","badge":null,"isAdmin":false,"isBanned":false,"color":"Gray","ccfLevel":0,"background":""},"attachments":[],"canEdit":false,"limits":{"time":[1000,1000,1000,1000,1000],"memory":[128000,128000,128000,128000,128000]},"stdCode":"","tags":[6,8,18,83],"wantsTranslation":false,"totalSubmit":16782,"totalAccepted":8725,"flag":5,"pid":"P1027","title":"[NOIP2001 提高组] Car 的旅行路线","difficulty":5,"fullScore":100,"type":"P"},"contest":null,"discussions":[{"id":642991,"title":"本地运行答案正确但交上去只有20pts","forum":{"id":33,"name":"P1027 [NOIP2001 提高组] Car 的旅行路线","slug":"P1027"}},{"id":621047,"title":"是样例的问题吗？我样例输出49.5,但是AC了？？？","forum":{"id":33,"name":"P1027 [NOIP2001 提高组] Car 的旅行路线","slug":"P1027"}},{"id":620791,"title":"建议降绿","forum":{"id":33,"name":"P1027 [NOIP2001 提高组] Car 的旅行路线","slug":"P1027"}},{"id":569413,"title":"#2#5WA求助！","forum":{"id":33,"name":"P1027 [NOIP2001 提高组] Car 的旅行路线","slug":"P1027"}},{"id":556625,"title":"数据太水","forum":{"id":33,"name":"P1027 [NOIP2001 提高组] Car 的旅行路线","slug":"P1027"}},{"id":515679,"title":"求助！样例没过，20分","forum":{"id":33,"name":"P1027 [NOIP2001 提高组] Car 的旅行路线","slug":"P1027"}}],"bookmarked":false,"vjudgeUsername":null,"recommendations":[{"pid":"P1028","title":"[NOIP2001 普及组] 数的计算","difficulty":2,"fullScore":100,"type":"P"},{"pid":"P1029","title":"[NOIP2001 普及组] 最大公约数和最小公倍数问题","difficulty":2,"fullScore":100,"type":"P"},{"pid":"P1034","title":"[NOIP2002 提高组] 矩形覆盖","difficulty":5,"fullScore":100,"type":"P"},{"pid":"P1039","title":"[NOIP2003 提高组] 侦探推理","difficulty":5,"fullScore":200,"type":"P"},{"pid":"P1041","title":"[NOIP2003 提高组] 传染病控制","difficulty":5,"fullScore":100,"type":"P"}],"lastLanguage":0,"lastCode":"","privilegedTeams":[],"userTranslation":null},"currentTitle":"[NOIP2001 提高组] Car 的旅行路线","currentTheme":null,"currentTime":1694781719