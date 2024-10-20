

def test_simple_stuff():
    
    L = [['settlement',20200303],['maturity',20200304]]

    # for i, x in enumerate(L):
    #     for j, a in enumerate(x):
    #         if 'bob' in a:
    #             L[i][j] = a.replace('bob', 'b')

    print(L)

    values = ['settlement',20240303]

    settlement = 20240303

    new_values = [ [i,settlement if i == 'settlement' else j] for i, j in L ]

    assert new_values == [['settlement', 20240303], ['maturity', 20200303]]