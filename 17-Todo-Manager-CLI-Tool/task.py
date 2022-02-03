'''
TITLE: Task Manager CLI Tool
AUTHOR: Nivedhitha D
DESCRIPTION: A command-line program to help you manage your tasks.
USAGE:
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistic
'''

# Importing the required libraries and modules
import sys
import os.path
from queue import PriorityQueue

# List of helper functions for each command

def taskHelp():
    '''
    Shows usage.
    '''

    taskhelpText = \
        """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
    sys.stdout.buffer.write(taskhelpText.encode('utf8'))

def taskAdd(priority, taskText):
    '''
    Add a new item with priority 2 and text "hello world" to the list.
    '''

    if os.path.isfile('task.txt'):
        with open('task.txt', 'r') as taskFileOriginal:
            data = taskFileOriginal.read()
        with open('task.txt', 'w') as taskFileModified:
            taskFileModified.write(priority + " " + taskText + '\n' + data)
    else:
        with open('task.txt', 'w') as taskFile:
            taskFile.write(priority + " " + taskText + '\n')
    sys.stdout.buffer.write('Added task: "{}" with priority {}'.format(taskText, priority).encode('utf8'))

def taskList():
    '''
    Sho the incomplete priority list items sorted by priority in ascending order.
    '''

    if os.path.isfile('task.txt'):
        with open('task.txt', 'r') as taskFileOriginal:
            data = taskFileOriginal.readlines()
            q = PriorityQueue()
            printData = ''
        for line in data:
            priority, taskText = line.split(' ', 1)
            q.put((priority, taskText))

        countTask = 1
        while(not q.empty()):
            priority, taskText = q.get()
            taskText = taskText[:-1]
            printData += f'{countTask}. {taskText} [{priority}]\n'
            countTask += 1
        sys.stdout.buffer.write(printData.encode('utf8'))
    else:
        sys.stdout.buffer.write('There are no pending tasks!'.encode('utf8'))

def taskDel(taskIndex):
    '''
    Delete the incomplete item with the given index (taskIndex).
    '''

    if os.path.isfile('task.txt'):
        with open('task.txt', 'r') as taskFileOriginal:
            data = taskFileOriginal.readlines()
        count = len(data)
        if taskIndex > count or taskIndex <= 0:
            sys.stdout.buffer.write('Error: task with index #{} does not exist. Nothing deleted.'.format(taskIndex).encode('utf8'))
        else:
            with open('task.txt', 'w') as taskFileModified:
                for line in data:
                    if count != taskIndex:
                        taskFileModified.write(line)
                    count -= 1
            sys.stdout.buffer.write('Deleted task #{}'.format(taskIndex).encode('utf8'))
    else:
        sys.stdout.buffer.write('Error: task with index #{} does not exist. Nothing deleted.'.format(taskIndex).encode('utf8'))

def taskDone(taskIndex):
    '''
    Mark the incomplete item with the given index (taskIndex) as complete.
    '''

    if os.path.isfile('task.txt'):
        with open('task.txt', 'r') as taskFileOriginal:
            data = taskFileOriginal.readlines()
        count = len(data)
        if taskIndex > count or taskIndex <= 0:
            sys.stdout.buffer.write('Error: no incomplete item with index #{} exists.'.format(taskIndex).encode('utf8'))
        else:
            with open('task.txt', 'w') as taskFileModified:
                if os.path.isfile('completed.txt'):
                    with open('completed.txt', 'r') as doneFileOri:
                        doneData = doneFileOri.read()
                    with open('completed.txt', 'w') as doneFileMod:
                        for line in data:
                            if count == taskIndex:
                                doneFileMod.write(line)
                            else:
                                taskFileModified.write(line)
                            count -= 1
                        doneFileMod.write(doneData)
                else:
                    with open('completed.txt', 'w') as doneFileMod:
                        for line in data:
                            if count == taskIndex:
                                doneFileMod.write(line)
                            else:
                                taskFileModified.write(line)
                            count -= 1
            sys.stdout.buffer.write('Marked item as done.'.format(taskIndex).encode('utf8'))
    else:
        sys.stdout.buffer.write('Error: no incomplete item with index #0 exists.'.format(taskIndex).encode('utf8'))

def taskReport():
    '''
    Report statistics of pending and completed task lists
    '''

    if os.path.isfile('task.txt'):
        with open('task.txt', 'r') as taskFile:
            taskData = taskFile.readlines()
            q = PriorityQueue()
            printData = ''
        for line in taskData:
            priority, taskText = line.split(' ', 1)
            q.put((priority, taskText))

        countTask = 1
        while(not q.empty()):
            priority, taskText = q.get()
            taskText = taskText[:-1]
            printData += f'{countTask}. {taskText} [{priority}]\n'
            countTask += 1
        countTask -= 1
        sys.stdout.buffer.write(f'Pending : {countTask}\n'.encode('utf8'))
        sys.stdout.buffer.write(printData.encode('utf8'))

    sys.stdout.buffer.write("\n".encode('utf8'))

    if os.path.isfile('completed.txt'):
        with open('completed.txt', 'r') as doneFile:
            doneData = doneFile.readlines()
        countDone = 1
        printData = ''
        for line in reversed(doneData):
            priority, taskText = line.split(' ', 1)
            taskText = taskText[:-1]
            printData += f'{countDone}. {taskText}\n'
            countDone += 1
        countDone -= 1
        sys.stdout.buffer.write(f'Completed : {countDone}\n'.encode('utf8'))
        sys.stdout.buffer.write(printData.encode('utf8'))

# The menu function that calls the corresponding helper for the command entered by the user
def taskMenu():

    if len(sys.argv) == 1:
        taskHelp()
        
    elif sys.argv[1] == 'help':
        if len(sys.argv) == 2:
            taskHelp()
        else:
            sys.stdout.buffer.write('Too Many Arguments for help! Please use "./task help" for Usage Information'.encode('utf8'))

    elif sys.argv[1] == 'add':
        if len(sys.argv) == 4:
            taskAdd(sys.argv[2], ' '.join(sys.argv[3:]))
        else:
            sys.stdout.buffer.write('Error: Missing tasks string. Nothing added!'.encode('utf8'))

    elif sys.argv[1] == 'ls':
        if len(sys.argv) == 2:
            taskList()
        else:
            sys.stdout.buffer.write('Too Many Arguments for ls! Please use "./task help" for Usage Information'.encode('utf8'))

    elif sys.argv[1] == 'del':
        if len(sys.argv) == 3:
            try:
                val = int(sys.argv[2])
                taskDel(int(sys.argv[2]))
            except ValueError:
                sys.stdout.buffer.write('Given arguement for del is not an integer! Please use "./task help" for Usage Information'.encode('utf8'))
        else:
            sys.stdout.buffer.write('Error: Missing NUMBER for deleting tasks.'.encode('utf8'))

    elif sys.argv[1] == 'done':
        if len(sys.argv) == 3:
            try:
                val = int(sys.argv[2])
                taskDone(int(sys.argv[2]))
            except ValueError:
                sys.stdout.buffer.write('Given arguement for done is not an integer! Please use "./task help" for Usage Information'.encode('utf8'))
        else:
            sys.stdout.buffer.write('Error: Missing NUMBER for marking tasks as done.'.encode('utf8'))

    elif sys.argv[1] == 'report':
        if len(sys.argv) == 2:
            taskReport()
        else:
            sys.stdout.buffer.write('Too Many Arguments for report! Please use "./task help" for Usage Information'.encode('utf8'))
    else:
        sys.stdout.buffer.write('Option Not Available. Please use "./task help" for Usage Information'.encode('utf8'))

# Execution begins here
if __name__ == '__main__':
    taskMenu()
