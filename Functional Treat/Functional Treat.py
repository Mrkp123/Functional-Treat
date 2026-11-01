dataset = []
summary = []

def welcome():
    """Display a welcome message."""

    print("=" * 50)
    print(" DATA ANALYZER AND TRANSFORMATION")
    print("=" * 50)

def menu():
    """Display main menu."""

    print("\nmain menu")
    print("1. Input data")
    print("2. View data summary")
    print("3. calculate factorial")
    print("4. filter data")
    print("5. sort data")
    print("6. dataset statistics")
    print("7. show function documentation")
    print("8. exit")


def  input_data():
    """input 1D or 2D Data"""

    global dataset

    print("\n1. 1D list")
    print("2. 2D list")

    choice = input("enter choice : ")

    if choice == "1":

        data = list(map(int,input("enter numbers : ").split())) 

        dataset = data

        print("data stored successfully")

    elif choice == "2":

        rows = int(input("enter number of rows : "))
        cols = int(input("enter number of columns : "))

        matrix = []

        for i in range(rows):

            row = list(map(int,input(f"row {i+1} : ").split()))

            matrix.append(row)

        dataset = matrix

        print("2D data stored successfully")

    else:
        print("invalid choice")


def data_summary():
    """Display summary using built-in functions..."""

    global summary
    global dataset

    if dataset == []:
        print("No data available. ")
        return
    if isinstance(dataset[0], list):

        flat = []

        for row in dataset:
            flat.extend(row)

    else:
        flat = dataset


    total = len(flat)
    minimum = min(flat)
    maximum = max(flat)
    total_sum = sum(flat)
    average = total_sum / total 

    summary = {
        "total : total,"
        "minimum : minimum,"
        "maximum : maximum,"
        "sum : total_sum,"
        "average : average"
    }

    print("\nData Summary")
    print("total:", total)
    print("minimum:", minimum)
    print("maximum:",maximum)
    print("sum:", total_sum)
    print("average:",round(average,2))

def factorial(n):
    """calculate factorial using recursion."""

    if n == 0 or n == 1:
        return 1
    return n * factorial (n - 1)

def filter_data():
    """filter data using lambda function."""

    global dataset

    if dataset == []:
        print("no data available.")
        return
    if isinstance(dataset[0],list):
        flat = []

        for row in dataset:
            flat.extend(row)

    else:
        flat = dataset

    value = int(input("enter threshold value: "))

    result = list(filter(lambda x: x >= value, flat))

    print("filtered data" , result)

def sort_data():
    """sort dataset using sort() and sorted()."""

    global dataset

    if dataset == []:
        print("NO data available")
        return

    if isinstance(dataset[0], list):
        flat = []

        for row in dataset:
            flat.extend(row)

    else:
        flat = dataset.copy()

    print("original sort():", flat)

    flat.sort()
    print("using sort():", flat)

    sorted_data = sorted(flat,reverse=True)
    print("using sorted() descending:", sorted_data)

def dataset_statistics():
    """display dataset statistics."""

    global dataset

    if dataset == []:
        print("NO data available.")
        return
    if isinstance(dataset[0], list):
        flat = []

        for row in dataset:
            flat.extend(row)

    else:
        flat = dataset

    even = [x for x in flat if x % 2 == 0]
    odd = [x for x in flat if x % 2 != 0]

    print("\nDataset Statistics...")
    print("total elements:", len(flat))
    print("even elements:", even)
    print("odd elements:", odd)
    print("highest number:", max(flat))
    print("lowest number:", min(flat))

def show_documentation():
    """show function documentation."""

    print("\nFunction Documentation..")
    print("1." , input_data._doc_)
    print("2." , data_summary._doc_)
    print("3." , factorial._doc_)
    print("4." , filter_data._doc_)
    print("5." , sort_data._doc_)
    print("6." , dataset_statistics._doc_)
    

welcome()


while True:

    menu()
    choice = input("enter your choice : ")
    
    print("you entered :", choice)

    if choice == "1":
        input_data()

    elif choice == "2":
        data_summary()

    elif choice == "3":
        num = int(input("enter a number: "))
        print("factorial =", factorial(num))

    elif choice == "4":
        filter_data()

    elif choice == "5":
        sort_data()

    elif choice == "6":
        dataset_statistics()

    elif choice == "7":
        show_documentation()

    elif choice == "8":
        print("Thank you  all of you ")
        break
    else:
        print("Invalid choice. please enter a valid option.")
        