def Load_F(filename):
    tmp_data = []
    with open(filename) as f:
        tmp_data = f.readlines()
    marks = ['end', 'texture', 'models', 'file', 'new']
    inited_marks = {}
    for i in tmp_data:
        for ii in marks:
            if ii.capitalize() in i.capitalize():
                inited_marks[ii] = tmp_data.index(i)
    print(inited_marks)


Load_F(r"someshithere")
