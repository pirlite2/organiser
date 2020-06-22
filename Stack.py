#! /usr/bin/python3

#******************************************************************************
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA. 
#******************************************************************************

class Stack(list):
    """
    Implementation of generic stack class
    :version:
    :author: pir
    """
   #--------------------------------------------------------------------------

    def __init__(self):
        super().__init__()

        self.noStackItems = 0

        return

    #--------------------------------------------------------------------------

    def push(self, x):

        self.append(x)
        self.noStackItems += 1

        return

    #--------------------------------------------------------------------------

    def pop_(self):
        """ Note naming as pop_ to prevent infinite-dpeth recursive calls """

        assert(self.noStackItems > 0)
        x = self.pop()
        self.noStackItems -= 1

        return x

    #--------------------------------------------------------------------------

    def peek(self):

        x = self[-1]

        return x

    #--------------------------------------------------------------------------

    def isEmpty(self):

        return (self.noStackItems == 0)

#******************************************************************************

# Main program
if __name__ == "__main__":
    
    stack = Stack()

    stack.push(1)
    print(stack.pop_())
    print(stack.isEmpty())
    print()

    stack.push(1)
    stack.push(2)
    print(stack.pop_())
    print(stack.pop_())
    print(stack.isEmpty())
    print()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop_())
    print(stack.pop_())
    print(stack.pop_())
    print(stack.isEmpty())
    print()

    stack.push(1)
    stack.push(2)
    print(stack.pop_())
    stack.push(3)
    print(stack.pop_())
    print(stack.isEmpty())
    print(stack.pop_())
    print(stack.isEmpty())
    print()

    stack.push(1)
    stack.push(2)
    print("peeking: ", stack.peek())
    print("popping: ", stack.pop_())
    print("peeking: ", stack.peek())
    print("popping: ", stack.pop_())
    print()

#******************************************************************************