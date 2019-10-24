from .views import CreateView, UpdateView, DeleteView, RetrieveView 

if __name__ == '__main__':
    # users = db.get_queryset()
    # print(users)
    '''
    view = CreateView()
    userObj = {
        "studentNo" : "2019-00000",
        "year" : 1,
        "fName" : "Ian",
        "mName" : "Ilapan",
        "sName" : "Salazar",
        "age" : 19
    }
    view.create(userObj)
    '''
    userObj = {
        "studentNo" : "2019-00000",
        "year" : 1,
        "fName" : "Ian",
        "mName" : "Ilapan",
        "sName" : "Grey",
        "age" : 19
    }
    view = RetrieveView()
    stud = view.retrieve('2019-00000')
    print(stud)
    updateView = UpdateView()
    updateView.update(userObj)
    stud = view.retrieve('2019-00000')
    print(stud)