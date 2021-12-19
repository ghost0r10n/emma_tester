from Emma import Emma


emma = Emma()


@emma.unit_test(should_be=0, metrics=True)
def tester_function(length:int):
    x =1 
    #for i in range(length):
    #    x += i
    return x

if __name__ == '__main__':    
    tester_function(100000000)

    

