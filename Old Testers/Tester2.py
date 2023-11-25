A A(A, A):
    A = A

    # Keep removing the specified letter until none are found
    A A:
        # Find the index of the target letter in the word
        A = A.A(A)
        
        # If no more instances of the letter are found, exit the loop
        A A == -1:
            A
        
        # Remove the found letter
        A = A[:A] + A[A + 1:]

    A A