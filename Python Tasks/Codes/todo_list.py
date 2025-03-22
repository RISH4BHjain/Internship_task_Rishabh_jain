# basic todo list
def todo_list():
    tasks = []
    while True:
        print('1. Add task')
        print('2. show task')
        print('3. Mark as Complete')
        print('4. exit the todo list')
        print('\n')

         
        
        choice = int(input('choose any one of the option: '))  

        if choice == 1:   #Add task
         num_of_task = int(input('provide num of task you want to add: '))
         index_num = 1
         for i in range(0,num_of_task):
             task = input('input: ')
             tasks.append({'task':task,'progress':False,'index_count':index_num})
             index_num+=1
         print('task added successfully')
         
         print('\n')
        




        elif choice ==2:#show task
           for index , i in enumerate(tasks,1):
              if i['progress']:
                 print(f"{index}.{i['task']} - {'Complete'}")

              else:print(f"{index}.{i['task']} - {'Incomplete'}") 
           print('\n')  



        
        
        elif choice == 3:#Mark as Complete
           for index , i in enumerate(tasks,1):
                print(f"{index}: {i['task']}")

           print("which option you want to mark as done ")
           ind = int(input('index: '))

           for i in tasks:
              if ind == i['index_count'] :
                 i['progress'] = 'Completed'
                 
           for index , i in enumerate(tasks,1):
              print(f"{index}.{i['task']} - {i['progress']}")



           print('\n')

                 
           


        elif choice == 4:#exit the todo list
           exit=input('type any key to exit:')
           break



        else:print('invalid choice')


todo_list()
















