def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    you = sorted([yourLeft, yourRight])
    friend = sorted([friendsLeft, friendsRight])
    return you == friend
