# Annotate
TagMe目前是科学界最好的实体链接工具之一，具有非常好的性能，特别是在注释短文本时（即由几十个术语组成的那些）。
简单来讲这个工具主要解决一段文本当中的概念标注问题，任意一段文本当中需要提取相关的概念来对整段文本进行分析，因此筛选出来的概念既要满足“可查询”还要满足“无二义性”，可查询在这里本文要保证概念可以在维基百科当中找到对应的页面，例如概念“Artificial neural network”其实就是概念“Neural Network”更正式的定义，也就是概念“Neural Network”在维基百科当中没有其页面，但是“Artificial neural network”有，因此当文章当中出现概念“Neural Network”时我们要想办法把它转化成“Artificial neural network”使之能够查询和计算。再者就是无二义性，例如概念“Apple”包含的含义有很多，其中就有指代“水果苹果”或者“苹果公司”，要想知道其真正含义要结合其上下文，如果指代苹果公司，那么应该把该概念转化成“Apple Inc.”，该概念就可以明确表达苹果公司的含义。
详细的使用过程或者说明可见我写的博客：
https://blog.csdn.net/qq_43549752/article/details/88912835?tdsourcetag=s_pcqq_aiomsg
