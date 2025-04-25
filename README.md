# Assignment ACCUKNOX

Topic: Django Signals
### Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

By default django signals are executed synchronously this can be shown by the fact that if two signals are fired at almost same time then their order of execution should not get altered.
To prove it we have created 

## User Model
![models](https://github.com/user-attachments/assets/8f24abee-280b-4113-afd9-e2a887a7398e)

## app1/signals.py
![app1_signals](https://github.com/user-attachments/assets/d533b0ba-0811-45ac-ad24-43dbab9864d2)

## app1/tests.py
![app1_test](https://github.com/user-attachments/assets/0750d4dc-bb2f-4c69-890a-830d492166b4)

in above code we have fired the signals simultaneously and waited for five seconds each
the results can be confirmed by the order of execution of both signals and total time taken

## app1 Test Result
![app1_test_result](https://github.com/user-attachments/assets/e3f48939-477b-4810-9043-abaec1c374cc)

__________________________________________________________________________________________________________________________________________________________

### Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Yes, Django signals run on same thread as callerthis can be shown by confirming that the thread ID of both caller and signal are same

## User Model
![models](https://github.com/user-attachments/assets/8f24abee-280b-4113-afd9-e2a887a7398e)

## app2/signals.py
![app2_signals](https://github.com/user-attachments/assets/e00a5cca-7c31-4423-90da-bb329bf78336)

## app2/tests.py
![app2_test](https://github.com/user-attachments/assets/ffd02c3f-283b-4da9-89c4-16c855d46a46)

we got the same thread ID

## app2 Test Result
![app2_test_result](https://github.com/user-attachments/assets/a27e9299-b3a6-4854-9ea1-c85781c49b18)

__________________________________________________________________________________________________________________________________________________________

### Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Yes, Django signals run in the same database transaction as the caller this can be confirmed by adding a dummy user through post_save signal upon inserting main user data and forcefully aborting the transaction after saving the user data this will cause roll back of main transaction of insertion if the signal runs on same database transaction then the inserted dummy data will also me rolled back.

## User Model
![models](https://github.com/user-attachments/assets/8f24abee-280b-4113-afd9-e2a887a7398e)

## app3/signals.py
![app3_signals](https://github.com/user-attachments/assets/44a9f883-8cc8-4084-8009-b123b7603080)

## app3/tests.py
![app3_test](https://github.com/user-attachments/assets/98617cf4-c579-4324-8ccb-41b4d469b88d)

we neither have main user neither dummy user

## app2 Test Result
![app3_test_result](https://github.com/user-attachments/assets/219a505a-2c53-40f2-b27f-a4b715d2823c)

...................................................................................................................................................................
Topic: Custom Classes in Python

### Description: You are tasked with creating a Rectangle class with the following requirements:

1. An instance of the Rectangle class requires length:int and width:int to be initialized.
2. We can iterate over an instance of the Rectangle class 
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

To make a class iterable we can either define:
__iter__() and __next__() or Use a generator __iter__()

![image](https://github.com/user-attachments/assets/b8bed7d3-fb09-408f-9eb9-958aa83f5f3b)



