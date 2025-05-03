def function():
    my_dict={"name":"raja","age":10,"college":"KLU"}
    for key,value in my_dict.items():
        print(key,value)

function()  



questions={
    "which year python was indroduced":1995,
    "python support which database ":"All database",
    "python is easy or not":"yes"
}
scroe=0

for question,answer in questions.items():
    user_answer=input(question)

    if user_answer.strip().lower()== answer.lower():
        print("your answer is correct")
        scroe+=1
    else:
        print("your answer is not correct")    

