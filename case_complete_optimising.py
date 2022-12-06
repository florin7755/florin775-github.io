todos=[]

while True:
    #get uer input strip space chars from it
    user_action=input("Type add, show, edit,complete or exit: ")
    user_action=user_action.strip()
    match user_action:
       case 'add':
           todo=input("Enter a todo: ")+'\n'

           #file=open('todos.txt', 'r')
           #todos=file.readlines()
           #file.close()

           with open('todos.txt', 'r') as file:
               todos = file.readlines()

           todos.append(todo)

           #file=open('todos.txt', 'w')
           #file.writelines(todos)
           #file.close()
           with open('todos.txt', 'w') as file:
               file.writelines(todos)

       case 'show':
           #file=open('todos.txt', 'r')
           #todos=file.readlines()
           #file.close()

          with open('todos.txt', 'r') as file:
             todos = file.readlines()

          # new_todos=[item.strip('\n') for item in todos]

          for index, item in enumerate(todos):  #print(index, item)
               item=item.strip('\n') #delete empty rows beetwin lines
               row=f"{index+1}-{item}"
               print(row)
       case 'edit':
           number=int(input('Number of the todo to edit: '))
           number=number-1
           with open('todos.txt', 'r') as file:
               todos=file.readlines()
           print('Here is todos existing', todos)

           new_todo=input('Enter new todo: ')
           todos[number]=new_todo+'\n'

           #print('Here is who it will be', todos)

           with open('todos.txt', 'w') as file:
               file.writelines(todos)

       case 'complete':
           number=int(input("Number of the todo to complete: "))

           with open('todos.txt', 'r') as file:
               todos=file.readlines()
           index=number-1
           todo_to_remove=todos[index].strip('\n')
           todos.pop(index)

           with open('todos.txt', 'w') as file:
               file.writelines(todos)

           message=f"Todo {todo_to_remove} was removed from the list."
           print(message)
       case 'exit':
           break
print("Bye!")