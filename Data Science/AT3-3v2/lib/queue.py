# Thanks wikipedia :) (https://en.wikipedia.org/wiki/Amortized_analysis)

class Queue:
    # Define the constructor method that initializes two empty lists
    def __init__(self):
        self.input = [] # This list will store the elements that are enqueued
        self.output = [] # This list will store the elements that are dequeued

    # Define a method named enqueue that takes an element as a parameter
    def enqueue(self, element):
        self.input.append(element) # Append the element to the input list

    # Define a method named dequeue that returns the first element that was enqueued
    def dequeue(self):
        if not self.output: # If the output list is empty
            while self.input: # While the input list is not empty
                self.output.append(self.input.pop()) # Pop the last element from the input list and append it to the output list

        return self.output.pop() # Pop and return the last element from the output list

    # ---------------
    # Added functions
    #----------------
    
    def is_empty(self):
        if len(self.input) == 0 and len(self.output) == 0:
            return True

        return False
    
    def get_queue(self):
        return self.input + self.output
    
    # Remove the latest retrieved element from the queue
    def remove(self):
        _ = self.output.pop()
    
    def dequeue_preserve(self):
        if not self.output: # If the output list is empty
            while self.input: # While the input list is not empty
                self.output.append(self.input.pop()) # Pop the last element from the input list and append it to the output list

        return self.output[-1] # return the last element in output without removing it.