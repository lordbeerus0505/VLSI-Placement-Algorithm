import matplotlib.pyplot as plt

f=open("sample.txt","r")
data=f.readlines()
count=1
new_data_x=[]
new_data_y=[]
for d in data:
    # print(d)
    d=d.split("\t")
    print(d[1])
    count+=1
    new_data_x.append(count)
    new_data_y.append(d[1])
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(new_data_x, new_data_y, color='r')
ax.set_xlabel('Grades Range')
ax.set_ylabel('Grades Scored')
ax.set_title('scatter plot')
plt.show()
# print(data)
