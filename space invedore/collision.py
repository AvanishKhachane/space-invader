def collision(x1, x2, y1, y2, d):
    dis = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2),0.5)
    if dis < d:
        return True
    else:
        return False
