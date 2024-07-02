# CSV Email Reader/Writer
#### Video Demo: https://youtu.be/bZNN_3xxGQQ
#### Description:
The essense of my final project for CS50P is essentialy a CSV email reader/writer, that reads two csv's files and gets an email adress from one of them and puts them into the other one.

There were many elements that went into this project. One of them was the fact that using the open function in python and creating mutiple functions in order to handle different parts of the process. With the first function being a read_csv function that takes in a file name as its argument. Whatever file it reads is passed through the command line terminal window. The function then reads the csv file gets the headers and data therin, and returns those values.

After the comapre_and_modify_data function is executed. This custom function takes in data1(the first csv file arg that is passed), headers1(The headers of theat first csv file), data2(the second csv file that is passed), headers2(the headers from that second csv file), key_column_name(the column names that we are looking for in the second csv file), target_column_name(the name of hte column that we are looking for in the first csv file). The main purpose of the program is to look for specific header and column names, and if they match to one another, to get an email address from the first csv file(data1) and put it into the corrsesponding csv file(data2).

From there one csv_writer function is operated in which it writes headers and rows into data2(the second csv file.)

Finally, the main function is executed wherein its purpose is to basically get all of the values that the previous functions return and put them together. It gets the name of the files that the user inputs as arguments in the command line terminal, it then passes those values into the specific functions. It also provides values for the certain column name/headers that we are looking for. It also then gives the values in which for the program to write into an output file that is automatically genereated with all of the changes made.

In the end a new csv file of "output.csv" is generated which has all of the modified changes into the dir that the code/program was executed from.
