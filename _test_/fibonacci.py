def dynamic_fibbo(n, table=[]):
    while len(table) < n+1:
        # this does the same thing except it doesn't change the reference to `table`
        table.append(0)

    # base case
    if n <= 1:
        return n

    # recursive case
    else:
        if table[n-1] == 0:
            table[n-1] = dynamic_fibbo(n-1)

        if table[n-2] == 0:
            table[n-2] = dynamic_fibbo(n-2)

        table[n] = table[n-2] + table[n-1]
    return table[n]
