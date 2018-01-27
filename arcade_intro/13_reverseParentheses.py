def reverseParentheses(s):
    lefts = []
    brackets = []

    for i in range(len(s)):
        if s[i] == '(':
            lefts.append(i)
        elif s[i] == ')':
            left = lefts.pop()
            brackets.append((left, i))
    print(brackets)

    for i in brackets:
        l_br, r_br = i
        segment = s[l_br:r_br]
        new_segment = segment[::-1]
        s = s[:l_br] + new_segment + s[r_br:]
    s = s.replace('(', '').replace(')', '')
    return s

s = "a(bcdefghijkl(mno)p)q"
print(reverseParentheses(s))