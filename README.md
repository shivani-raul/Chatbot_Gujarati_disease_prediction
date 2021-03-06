# Disease Prediction in Gujrati
## Cloud Chatbot

The proposed disease prediction chatbot can interact with the users, and give them a realistic experience of talking with a medical expert. It can be an alternative in the future to the current practice of visiting a hospital and making an appointment with a doctor to get a diagnosis. Primarily the focus is to provide assistance to the people who cannot speak or understand or read in english or hindi language but in one specific language that is gujrati. 

The Gujarati language dataset is prepared manually which includes symptoms, diseases, descriptions of diseases, reasons, treatments, and home remedies. The features considered are the Parts of Speech (POS) tag of the current word, the previous word and the next word in addition to the words themselves. The input text also undergoes POS tagging before prediction for better results. The system is designed with efficient accuracy.

![workflow-dfd](https://user-images.githubusercontent.com/71781405/118617759-90831880-b7e0-11eb-8a6b-ed3d3c34cd31.PNG)
#### Algorithm
● Step 1 : Take input from the user. (Either Symptoms to know disease or enter disease name to know details of it. 

● Step 2 : Tokenize the sentence into words. 

● Step 3 : If first word is ‘રોગ’, then for the other words find the disease name from the disease list and print its details like, reasons, treatments , home remedies etc. 

● Step 4 : If first word is not ‘રોગ’, then apply stemming on each word of the sentence. 

● Step 5 : Load POS dataset and apply stemming on each word of POS tag 

● Step 6 : Make dictionary of stem word as a key and its tag as value 

● Step 7 : Get the POS tag of each word from that dictionary. 

● Step 8 : Collect all nouns from that sentence and put them in one list called symptoms list.(Because we have considered all symptoms as nouns). 

● Step 9 : Fetch symptoms from symptoms list and get their maximum matching symptom name from the dataset. 

● Step 10 : Train the RandomForest model on a training data set. 

● Step 11 : Define an empty array S of length of no. of symptoms and initialize it with zero. 

● Step 12 : Put one in an array where the symptom matches with the input symptom. ● Step 13 : Predict disease based on this array. 

● Step 14 : If symptoms are related to more than one disease, then the bot will ask other relatedsymptoms. 

● Step 15 : Take input from the user yes/no/stop. (yes - if the symptom is related to his illness, no - if the symptom is not related to his illness and stop - if he doesn't want to do more clarification.) 

● Step 16 : Based on these inputs update array S. 


● Step 17 : Predict the final disease. 

● Step 18 : Take input from the user yes/no - whether he/she wants to get details of the disease or not. 

● Step 19 : If input is yes : Display all details of the disease. Else : Display Thank You 

### Learning
The chatbot acts as a user application. The user of this application can specify their symptoms or disease (if they already know) to the chatbot and in turn, the chatbot will specify the health measures to be taken. General information about symptoms and diseases are available in the dataset and thus our chatbot can provide information about disease and treatment to the user.

The concept of Natural Language Processing is used to design an interactive chatbot to retrieve symptoms provided by the user. The prediction model can be designed using Machine learning algorithms such as KNN, Random Forest and Decision Tree. All the algorithms were applied on the same dataset and based on the confidence and accuracy rate, the best model is selected which was Random Forest.
