def title():
    print("\n1. Title:\n")
    print("Image Classification For A City Dog Show".title())


def description():
    print("\n2. Description:\n")
    print("Your city is hosting a citywide dog show and you have volunteered to help the organizing\n"
          "committee with contestant registration. Every participant that registers must submit an image\n"
          "of their dog along with biographical information about their dog. The registration system tags\n"
          "the images based upon the biographical information.\n\n"
          
          "To be able to host the dog show, the city had to cancel and reschedule an annual arts festival.\n"
          "Some tricksters that were upset about the rescheduling of the arts festival are planning on\n"
          "registering pets that aren’t actual dogs, as a means of protesting the rescheduling.\n\n"
          
          "You are planning on using your newly developed Python skills to thwart the tricksters\n"
          "scheme to upset registration.")

    
"""
1. Title:
    Image Classification for a City Dog Show

2. Description:
    Your city is hosting a citywide dog show and you have volunteered to help the organizing 
    committee with contestant registration. Every participant that registers must submit an image 
    of their dog along with biographical information about their dog. The registration system tags 
    the images based upon the biographical information.

    To be able to host the dog show, the city had to cancel and reschedule an annual arts festival. 
    Some tricksters that were upset about the rescheduling of the arts festival are planning on 
    registering pets that aren’t actual dogs, as a means of protesting the rescheduling.

    You are planning on using your newly developed Python skills to thwart the tricksters 
    scheme to upset registration.

3. Lab Goals:
    Improving your programming skills using by Python to solve a complex problem, computationally.
    Using a deep learning model to solve this complex problem.
    Having fun solving a more complex problem using Python.
    
4. Your Tasks:
    Using your Python skills, you will determine which image classification algorithm works
    the "best" on classifying images as "dogs" or "not dogs" to deal with the tricksters protesting
    the art show rescheduling.
    Additionally, you want to determine how well the "best" classification algorithm works on
    correctly identifying a dog's breed. Fortunately, the registration system will tag each photo
    with the registered dog's breed (as entered by the participant). Your program will only need
    to compare the photo's filename (which will include the breed) to the breed that the
    classification algorithm returns. For images where the breed differs, other volunteers will
    call and verify a dog's breed.
    Finally with computational tasks, there is often a trade-off between accuracy and runtime.
    The more accurate an algorithm, the higher the likelihood that it will take more time and
    use more computational resources to run. To better prepare you for discussing this and exploring
    the "best" option when solving a problem computationally, we would like you to time how long each
    algorithm takes to solve the classification problem.
    
5. Important Notes:
    For this image classification task you will be using an image classification application using 
    a deep learning model called a convolutional neural network (often abbreviated as CNN). CNNs work 
    particularly well for detecting features in images like colors, textures, and edges; then using 
    these features to identify objects in the images. You'll use a CNN that has already learned the 
    features from a giant dataset of 1.2 million images called ImageNet. There are different types 
    of CNNs that have different structures (architectures) that work better or worse depending on 
    your criteria. With this lab you'll explore the three different architectures 
    (AlexNet, VGG, and ResNet) and determine which is best for your application.
    
    We have provided you with a classifier function in classifier.py that will allow you to use 
    these CNNs to classify your images. The test_classifier.py file contains an example program that 
    demonstrates how to use the classifier function. For this lab, you will be focusing on using your 
    Python skills to complete these tasks using the classifier function; in the Neural Networks lesson 
    you will be learning more about how these algorithms work.
    
    Understand that certain breeds of dog look very similar and any of these algorithms' ability to 
    distinguish between two breeds of dog is only as good as the dataset (ImageNet) and the algorithm. 
    Meaning that the more images of two similar looking dog breeds that the algorithm has learned from, 
    the more likely the algorithm will be able to distinguish between those two breeds. This is also 
    true for you, the more images of two similar dog breeds you see in knowing their true identification; 
    the better you will become on distinguishing between those two breeds of dog. We have found the 
    following breeds to look very similar: Great Pyrenees and Kuvasz, German Shepherd and Malinois, 
    Beagle and Walker Hound, and others.
    
    Finally, note that some dog breeds, like Greyhound and Australian Shepherd, are not breeds of dog 
    that have images in ImageNet. This means the algorithms would never be able to correctly classify 
    those breeds of dog because they have never seen them before. The best the algorithms can do is to 
    classify those images as some similar looking breed of dog that does exist in ImageNet. For the images 
    you will be testing the algorithms on, only dog breeds that exist in ImageNet will be used.
    
6. Principle Objectives:
    * Correctly identify which pet images are of dogs (even if breed is misclassified) and which pet 
    images aren't of dogs (irregardless of if the image is correctly classified).
    * Correctly classify the breed of dog, for the images that are of dogs.
    * Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve the 
    objectives 1 and 2.
    * Consider the time resources required to best achieve objectives 1 and 2, and determine if 
    an alternative solution would have given a "good enough" result, given the amount of time each 
    of the algorithms takes to run.
    
7. Program Outline:
    Repeat below for all three image classification algorithms (e.g. input algorithm 
    as command line argument):

    * Time your program
        - Use Time Module to compute program runtime
    * Get program Inputs from the user
        - Use command line arguments to get user inputs
    * Create Pet Images Labels
        - Use the pet images filenames to create labels
        - Store the pet image labels in a data structure (e.g. dictionary)
    * Create Classifier Labels and Compare Labels
        - Use the Classifier function classify the images and create the classifier labels
        - Compare Classifier Labels to Pet Image Labels
        - Store Pet Labels, Classifier Labels, and their comparison in a complex data 
          structure (e.g. dictionary of lists)
    * Classifying Labels as "Dogs" or "Not Dogs"
        - Classify all Labels (Pet & Classifier) as "Dogs" or "Not Dogs" using dognames.txt file
        - Store new classifications in the complex data structure (e.g. dictionary of lists)
    * Calculate the Results
        - Use Labels and their classifications to determine how well the algorithm worked on classifying images.
    *Print the Results
    
"""

print(description())
