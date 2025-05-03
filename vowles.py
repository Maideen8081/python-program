def function(ref):
    vowles=[i for i in ref if i in "aeiouAEIOU"]
    print(len(vowles))
    print(vowles)

function("heuhufehufe")   


def functions(num):
    count=0
    vowles=0

    for i in num:
        if i in "aeiouAeiou":
            vowles=vowles+1

        else:
            count=count+1

    print(count)
    print(vowles)
functions("rfefenfj")            


