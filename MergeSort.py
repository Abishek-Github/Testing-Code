def mergesort(l):
    if len(l) > 1:
        m = len(l) // 2
        L = l[:m]
        R = l[m:]
        mrg(L)
        mrg(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            l[k] = R[j]
            j += 1
            k += 1

# Example usage
lst = [34, 7, 23, 32, 5, 62]
mrg(lst)
print(lst)
