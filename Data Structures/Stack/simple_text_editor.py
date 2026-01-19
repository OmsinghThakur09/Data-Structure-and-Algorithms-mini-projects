# program to develop simple text editor
"""
1. write function:
simple let you write your text.

2. undo function:
let you undo your text.
logic: maintain undo stack in which first element will be '' and then next elements will be users text.
whenever user enters new text the previous text will be stored on undo stack, and when user undo to text then top element
of undo stack will be the current text.

3. redo function:
let you redo your text.
logic: maintain redo stack which only will effective if user undo to text, when user undo text then current text will be
stored in redo stack and when user redo text then top element of the stack will be the current text, and when user enters
new text then redo stack will be clear.

4. show text function:
shows your current text.

5. delete function:
let you delete your text.

6.get status function:
shows editor stats
"""

from stack import Stack


class TextEditor:
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()

        self.current_text = ""
        self.undo_stack.push(self.current_text)

    def write(self, text):
        self.undo_stack.push(self.current_text)  # stores old text before entering new text
        self.current_text += ' ' + text  # adds new text

        print('written: ', text)
        print('current text:', self.current_text)

    def delete(self, num_chars):
        if num_chars == 0:
            return
        elif num_chars > len(self.current_text):
            num_chars = len(self.current_text)

        self.undo_stack.push(self.current_text)  # store before deleting
        self.current_text = self.current_text[:-num_chars]

        self.redo_stack.clear()  # after deletion redo stack is no more valid.

        print(f'Deleted: {num_chars} characters')
        print('current text:', self.current_text)

    def undo(self):
        if self.undo_stack.size() <= 1:
            print('nothing to undo!')
            return

        self.redo_stack.push(self.current_text)  # store current text

        self.current_text = self.undo_stack.peek()  # current text becomes previous one
        self.undo_stack.pop()  # remove current text

        print('undo performed!')
        print('current text:', self.current_text)

    def redo(self):
        if self.redo_stack.size() < 1:
            print('nothing to redo!')
            return

        restored_text = self.redo_stack.pop() # get the text from redo stack

        self.undo_stack.push(restored_text) # store restored text

        self.current_text = restored_text

        print('redo performed!')
        print('current text:', self.current_text)

    def show_text(self):
        print('\n'+'-'*50)
        print('current document content:')
        print('-'*50)
        print(self.current_text)
        print('-'*50)

    def get_stats(self):
        print('\n Editor Status:')
        print('current text length:', len(self.current_text))
        print('length of redo stack:', self.redo_stack.size())
        print('length of undo stack:', self.undo_stack.size())


if __name__ == '__main__':
    print('\nSimple text editor with Undo/Redo Demo\n')

    editor = TextEditor()

    print('..........write operation.........')
    editor.write('Hello')
    editor.write('World!')

    print('\n........undo operation.........')
    editor.undo()
    editor.undo()

    print('\n........redo operation..........')
    editor.redo()
    editor.redo()

    print('\n.....New text clears redo.....')
    editor.write('this')
    editor.redo()

    print('\n.......Delete Operation.......')
    editor.delete(5)
    editor.undo()

    editor.show_text()
    editor.get_stats()
