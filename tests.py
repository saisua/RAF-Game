from Items.Item import Item
from numpy import array

def manual():
    i = Item()
    i_p = 4
    i.important_properties = array([0]*i_p)

def main():
    manual()

if __name__ == "__main__":
    main()