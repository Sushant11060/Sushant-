try:
    #any sample code
    print("hello")

    
except TypeError:
    print("Variable is of wrong type")
except ZeroDivisionError:
    print("Can't divide by 0")
except KeyError:
    print("Not a valid key")
except NameError:
    print("Not a valid variable")
except ValueError:
    print("Variable has a wrong value")
except IndexError:
    print("Not a valid index")
except ModuleNotFoundError:
    print("No module found with that name")
except ImportError:
    print("Problem with import statement")
except FileNotFoundError:
    print("No file found with that name")
except AttributeError:
    print("There is no such attribute")
except IndentationError:
    print("Wrong indentation in code")
