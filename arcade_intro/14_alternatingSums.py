def alternatingSums(a):
    first = sum(a[::2])
    second = sum(a) - first
    return [first, second]

a = [50, 60, 60, 45, 70]
alternatingSums(a)